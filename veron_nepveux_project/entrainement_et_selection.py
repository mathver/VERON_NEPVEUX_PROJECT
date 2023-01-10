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
from .conversion_df import data_frame_modele
from serde import serde


@serde
@dataclass
class Dataframes:
    X:np.ndarray
    X_tr: np.ndarray
    X_te : np.ndarray
    y: np.ndarray
    y_tr: np.ndarray
    y_te : np.ndarray

def remplit_class(fichier : str = "donnees.json"):
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
 
def selection_modele(fichier: str = "donnees.json"):
    ...