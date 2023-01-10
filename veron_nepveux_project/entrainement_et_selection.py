"""
Description : 

Librairie ayant pour but d'entrainer et de selectionner le modèle le plus adéquat pour les données


"""
import numpy as np
from sklearn.model_selection import train_test_split,RandomizedSearchCV, GridSearchCV
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
from dataclasses import dataclass
from conversion_df import data_frame_modele, data_frame_pandas, data_frame_dummies, data_frame_sklearn
from serde import serde
from pickle import load, dump
from scrapping import Voiture
import pandas as pd
from time import sleep
from serde.json import to_json, from_json
STOCKAGE = "./stockage/"




@serde
@dataclass
class Dataframes:
    X:np.ndarray
    X_tr: np.ndarray
    X_te : np.ndarray
    y: np.ndarray
    y_tr: np.ndarray
    y_te : np.ndarray

def remplit_class(fichier : str = "donnees.json") -> Dataframes:
    X,y = data_frame_modele(fichier)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y)
    return Dataframes(
        X= X,
        X_tr = X_tr,
        X_te = X_te,
        y = y,
        y_tr = y_tr,
        y_te = y_te,
    )

def elastic_net(X_tr : np.ndarray, y_tr : np.ndarray):
    
    en = ElasticNet()
    en_gs = GridSearchCV(
    en,
    {
        "alpha": [2 ** p  for p in range(-6, 6)],
        "l1_ratio": (0.01, 0.25, 0.5, 0.75, 1),
    }   
    )
    en_gs.fit(X_tr, y_tr) 
    return en_gs.best_estimator_,en_gs.best_score_, en_gs.cv_results_

def knn(X_tr : np.ndarray, y_tr : np.ndarray):
    
    knr = KNeighborsRegressor()
    knr_gs = GridSearchCV(
        knr,
        {
            "n_neighbors": range(5, 15),
            "weights": ("uniform", "distance"),
        }
    )
    knr_gs.fit(X_tr, y_tr)
    return knr_gs.best_estimator_,knr_gs.best_score_, knr_gs.cv_results_

def rd_foret(X_tr : np.ndarray, y_tr : np.ndarray):
    
    rfr = RandomForestRegressor()
    rfr_gs = GridSearchCV(
        rfr,
        {   
            "n_estimators": (8 , 16, 32, 64, 128, 256),
        }
    )
    rfr_gs.fit(X_tr, y_tr)
    return rfr_gs.best_estimator_,rfr_gs.best_score_, rfr_gs.cv_results_

def svr_(X_tr : np.ndarray, y_tr : np.ndarray):
    
    svr = SVR()
    svr_gs = GridSearchCV(
        svr,
        {
            "C": (0.1, 1.0, 10),
            "epsilon": (0.1, 1.0, 10),
        }
    )
    svr_gs.fit(X_tr, y_tr)

    return svr_gs.best_estimator_,svr_gs.best_score_, svr_gs.cv_results_

def multi_layer_regressor(X_tr : np.ndarray, y_tr : np.ndarray):
    
    pln = Pipeline(
        [
            ("mise_echelle", MinMaxScaler()),
            ("neurones", MLPRegressor()),
        ]
    )
    pln_gs = GridSearchCV(
        pln,
        {
            "neurones__alpha": 10.0 ** -np.arange(1, 7),
            'neurones__hidden_layer_sizes': ((25,), (50, ), (100,), (20, 20)),
        }
    )
    pln_gs.fit(X_tr, y_tr)
    
    return pln_gs.best_estimator_,pln_gs.best_score_, pln_gs.cv_results_
 
def selection_modele(fichier: str = "donnees_peugeot.json"):
    dfs = remplit_class(fichier)
    pln_gs_be,pln_gs_bs,pln_gs_cv = multi_layer_regressor(dfs.X_tr,dfs.y_tr)
    svr_gs_be,svr_gs_bs,svr_gs_cv = svr_(dfs.X_tr,dfs.y_tr)
    rfr_gs_be,rfr_gs_bs,rfr_gs_cv = rd_foret(dfs.X_tr,dfs.y_tr)
    knr_gs_be,knr_gs_bs,knr_gs_cv = knn(dfs.X_tr,dfs.y_tr)
    en_gs_be,en_gs_bs,en_gs_cv = elastic_net(dfs.X_tr,dfs.y_tr)
    dict_modeles = {'pln_gs_be' : pln_gs_bs,
                    'svr_gs_be' : svr_gs_bs,
                    'rfr_gs_be' : rfr_gs_bs,
                    'knr_gs_be' : knr_gs_bs,
                    'en_gs_be' : en_gs_bs
                    }
    meilleur_estimateur = eval(
        max(
            dict_modeles,
            key = dict_modeles.get
        )
    )
    return save_meilleur_estimateur(meilleur_estimateur)


def save_meilleur_estimateur(meilleur_estimateur: Pipeline): 
    path = "meilleur_estimateur.pkl"
    with open(path, "wb") as file: 
        dump(obj=meilleur_estimateur, file=file)
    

def charge_meilleur_estimateur(): 
    """Load best estimator from backup directory."""
    path =  "meilleur_estimateur.pkl"
    with open(path, "rb") as file: 
        est = load(file=file)
    return est 

def prix_predit_voiture(marque, modele, carburant, prix, kilometrage, garantie_kilometrage, boite_de_vitesse, transmission, couleur,
        garantie, date_mise_circulation, puissance, silhouette, nb_places, utilisation_prec,
        puissance_fiscale, critair, ptac, nb_portes):
    list_car = []
    car = Voiture(marque, modele, carburant, prix, kilometrage, garantie_kilometrage, boite_de_vitesse, transmission, couleur,
        garantie, date_mise_circulation, puissance, silhouette, nb_places, utilisation_prec,
        puissance_fiscale, critair, ptac, nb_portes)

    list_car.append(car)
    est = charge_meilleur_estimateur()

    f = open('donnees_temp.json', "w")
    f.write(to_json(list_car))
    sleep(4)
    car_df = data_frame_pandas('donnees_temp.json')
    df = data_frame_pandas(f'donnees_{marque}.json')
    df_fin = pd.concat([df, car_df], ignore_index = True)
    df_fin_cat = data_frame_dummies(df_fin)
    X_pred, y_pred = data_frame_sklearn(df_fin_cat)
    est_prix = pd.DataFrame(est.predict(X_pred)).iloc[-1][0].round()

    return est_prix, y_pred[-1]



prix_predit_voiture("Peugeot", "2008", "Essence", 30000, 60000, "garantie", "Automatique", 2, "Noir", "SPOTICAR PREMIUM", 2020, 130, "SUV-4x4", 5, "Ex-Particulier", 6, 2, 1500, 3)