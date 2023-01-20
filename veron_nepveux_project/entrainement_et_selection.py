"""
Librairie ayant pour but d'entrainer et de sélectionner le modèle le plus adéquat pour les données.
"""
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
from dataclasses import dataclass
from veron_nepveux_project.conversion_df import (
    data_frame_modele,
    data_frame_pandas,
    data_frame_dummies,
    data_frame_sklearn,
    assemblage_donnees,
)
from serde import serde
from pickle import load, dump
from veron_nepveux_project.scraping import Voiture
import pandas as pd
from serde.json import to_json
from typing import Any, Union
import os

STOCKAGE = "./stockage/"


@serde
@dataclass
class Dataframes:
    """
    # Description

    Dataclass permettant le création d'un dataframe compatible
    avec le module `sklearn` contenant les données originelles
    et les splits d'entraînements et de tests des modèles.
    """

    X: np.ndarray
    X_tr: np.ndarray
    X_te: np.ndarray
    y: np.ndarray
    y_tr: np.ndarray
    y_te: np.ndarray


def remplit_class(
    fichier_peugeot: str = "./veron_nepveux_project/donnees_peugeot.json",
    fichier_citroen: str = "./veron_nepveux_project/donnees_citroen.json",
    fichier_fiat: str = "./veron_nepveux_project/donnees_fiat.json",
    fichier_opel: str = "./veron_nepveux_project/donnees_opel.json",
) -> Dataframes:
    """
    # Description

    Fonction permettant la création d'un objet de classe
    `Dataframes` à partir des fichiers de données json.

    ## Paramètres

    - fichier_peugeot (str): Fichier json contenant les données de la marque Peugeot.
    - fichier_citroen (str): Fichier json contenant les données de la marque Citroën.

    ## Sortie

    Un objet de classe Dataframes.
    """
    X, y = data_frame_modele(
        fichier_peugeot, fichier_citroen, fichier_fiat, fichier_opel
    )
    X_tr, X_te, y_tr, y_te = train_test_split(X, y)
    return Dataframes(
        X=X,
        X_tr=X_tr,
        X_te=X_te,
        y=y,
        y_tr=y_tr,
        y_te=y_te,
    )


def elastic_net(X_tr: np.ndarray, y_tr: np.ndarray) -> Union[Any, Any, Any]:
    """
    # Description

    Fonction permettant le calcul du modèle ElasticNet sur les données précedemment choisies.

    ## Paramètres

    - X_tr (np.ndarray): Split d'entraînement des données concernant les variables.
    - y_tr (np.ndarray): Split d'entraînement des données concernant le prix.

    ## Sortie

    Retourne le meilleur estimateur, le meilleur score et les meilleurs paramètres du modèle.
    """
    en = ElasticNet()
    en_gs = GridSearchCV(
        en,
        {
            "alpha": [2**p for p in range(-6, 6)],
            "l1_ratio": (0.01, 0.25, 0.5, 0.75, 1),
        },
    )
    en_gs.fit(X_tr, y_tr)
    return en_gs.best_estimator_, en_gs.best_score_, en_gs.cv_results_


def knn(X_tr: np.ndarray, y_tr: np.ndarray) -> Union[Any, Any, Any]:
    """
    # Description

    Fonction permettant le calcul du modèle KNN sur les données précedemment choisies.

    ## Paramètres

    - X_tr (np.ndarray): Split d'entraînement des données concernant les variables.
    - y_tr (np.ndarray): Split d'entraînement des données concernant le prix.

    ## Sortie

    Retourne le meilleur estimateur, le meilleur score et les meilleurs paramètres du modèle.
    """
    knr = KNeighborsRegressor()
    knr_gs = GridSearchCV(
        knr,
        {
            "n_neighbors": range(5, 15),
            "weights": ("uniform", "distance"),
        },
    )
    knr_gs.fit(X_tr, y_tr)
    return knr_gs.best_estimator_, knr_gs.best_score_, knr_gs.cv_results_


def rd_foret(X_tr: np.ndarray, y_tr: np.ndarray) -> Union[Any, Any, Any]:
    """
    # Description

    Fonction permettant le calcul du modèle Random Forest sur les données précedemment choisies.

    ## Paramètres

    - X_tr (np.ndarray): Split d'entraînement des données concernant les variables.
    - y_tr (np.ndarray): Split d'entraînement des données concernant le prix.

    ## Sortie

    Retourne le meilleur estimateur, le meilleur score et les meilleurs paramètres du modèle.
    """
    rfr = RandomForestRegressor()
    rfr_gs = GridSearchCV(
        rfr,
        {
            "n_estimators": (8, 16, 32, 64, 128, 256, 512),
        },
    )
    rfr_gs.fit(X_tr, y_tr)
    return rfr_gs.best_estimator_, rfr_gs.best_score_, rfr_gs.cv_results_


def svr_(X_tr: np.ndarray, y_tr: np.ndarray) -> Union[Any, Any, Any]:
    """
    # Description

    Fonction permettant le calcul du modèle SVR sur les données précedemment choisies.

    ## Paramètres

    - X_tr (np.ndarray): Split d'entraînement des données concernant les variables.
    - y_tr (np.ndarray): Split d'entraînement des données concernant le prix.

    ## Sortie

    Retourne le meilleur estimateur, le meilleur score et les meilleurs paramètres du modèle.
    """
    svr = SVR()
    svr_gs = GridSearchCV(
        svr,
        {
            "C": (0.1, 1.0, 10),
            "epsilon": (0.1, 1.0, 10),
        },
    )
    svr_gs.fit(X_tr, y_tr)

    return svr_gs.best_estimator_, svr_gs.best_score_, svr_gs.cv_results_


def multi_layer_regressor(X_tr: np.ndarray, y_tr: np.ndarray) -> Union[Any, Any, Any]:
    """
    # Description

    Fonction permettant le calcul du modèle de régression multi-couches
    (réseau neuronal artificiel) sur les données précedemment choisies.

    ## Paramètres

    - X_tr (np.ndarray): Split d'entraînement des données concernant les variables.
    - y_tr (np.ndarray): Split d'entraînement des données concernant le prix.

    ## Sortie

    Retourne le meilleur estimateur, le meilleur score et les meilleurs paramètres du modèle.
    """
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
            "neurones__hidden_layer_sizes": ((25,), (50,), (100,), (20, 20)),
        },
    )
    pln_gs.fit(X_tr, y_tr)

    return pln_gs.best_estimator_, pln_gs.best_score_, pln_gs.cv_results_


def selection_modele() -> None:
    """
    # Description

    Fonction permettant de choisir parmi les modèles estimés le plus adaptés aux données.

    ## Sortie

    Retourne le meilleur modèle parmi ceux estimés.
    """
    dfs = remplit_class()
    pln_gs_be, pln_gs_bs, pln_gs_cv = multi_layer_regressor(dfs.X_tr, dfs.y_tr)
    svr_gs_be, svr_gs_bs, svr_gs_cv = svr_(dfs.X_tr, dfs.y_tr)
    rfr_gs_be, rfr_gs_bs, rfr_gs_cv = rd_foret(dfs.X_tr, dfs.y_tr)
    knr_gs_be, knr_gs_bs, knr_gs_cv = knn(dfs.X_tr, dfs.y_tr)
    en_gs_be, en_gs_bs, en_gs_cv = elastic_net(dfs.X_tr, dfs.y_tr)
    duo_estimateur_score = [
        [pln_gs_bs, svr_gs_bs, rfr_gs_bs, knr_gs_bs, en_gs_bs],
        [pln_gs_be, svr_gs_be, rfr_gs_be, knr_gs_be, en_gs_be],
    ]
    a = 0.0
    for i in duo_estimateur_score[0]:
        if a < i:
            a = i

    meilleur_estimateur = duo_estimateur_score[1][duo_estimateur_score[0].index(a)]
    test_surapprentissage = meilleur_estimateur.score(dfs.X_te, dfs.y_te)
    if abs(a - test_surapprentissage) > 0.15:
        raise ValueError("Le modèle est en surapprentissage")
    return save_meilleur_estimateur(meilleur_estimateur)


def save_meilleur_estimateur(meilleur_estimateur: Pipeline) -> None:
    """
    # Description

    Fonction permettant de sauvegarder le meilleur modèle au format pkl (pickle).

    ## Paramètre

    - meilleur_estimateur (Pipeline): le meilleur modèle trouvé.

    ## Sortie

    Retourne un fichier pkl contenant le modèle.
    """
    path = "veron_nepveux_project/meilleur_estimateur.pkl"
    with open(path, "wb") as file:
        dump(obj=meilleur_estimateur, file=file)


def charge_meilleur_estimateur() -> Any:
    """
    # Description

    Fonction permettant de charger le meilleur modèle au format pkl (pickle).

    ## Sortie

    Retourne le modèle extrait du fichier pkl.
    """
    dir = os.path.dirname(os.path.realpath("entrainement_et_selection.py"))
    filename = os.path.join(dir, "meilleur_estimateur.pkl")

    filename = filename.replace("\\", "/")

    with open(filename, "rb") as file:
        est = load(file=file)
    return est


def prix_predit_voiture(
    marque,
    modele,
    carburant,
    prix,
    kilometrage,
    garantie_kilometrage,
    boite_de_vitesse,
    transmission,
    couleur,
    garantie,
    date_mise_circulation,
    puissance,
    silhouette,
    nb_places,
    utilisation_prec,
    puissance_fiscale,
    critair,
    ptac,
    nb_portes,
) -> int:
    """
    # Description

    Fonction permettant de prédire le prix d'un véhicule à partir de ces caractéristiques.

    ## Paramètres

    - marque (str): marque du véhicule (Peugeot, Citroën, Opel ou Fiat).
    - modele (str): Modèle du véhicule, dépendant de la marque.
    - carburant (str): Type de carburant du véhicule.
    - prix (int): Prix du véhicule.
    - kilometrage (int): Kilométrage du véhicule.
    - garantie_kilometrage (str): Est-ce que le kilométrage est garanti ou non ?
    - boite_de_vitesse (str): Type de boîte de vitesse (manuelle ou automatique).
    - transmission (int): Type de transmission (2 ou 4 roues motrices).
    - couleur (str): Couleur du véhicule.
    - garantie (str): Type de garantie proposé par le site vendeur.
    - date_mise_circulation (int): Année de la mise en circulation du véhicule.
    - puissance (int): Puissance du véhicule en chevaux.
    - silhouette (str): Silhouette du véhicule (SUV, citadine, berline, ...).
    - nb_places (int): Nombre de places du véhicules.
    - utilisation_prec (str): Utilisation précédente du véhicule.
    - puissance_fiscale (int): Puissance fiscale du véhicule en chevaux fiscaux.
    - critair (int): Indice Crit'Air du véhicule.
    - ptac (int): PTAC du véhicule.
    - nb_portes (int): Nombre de portes du véhicules (coffre inclus).

    ## Sortie

    Retourne le prix prédit par le modèle et le prix d'origine.
    """
    car = Voiture(
        marque,
        modele,
        carburant,
        prix,
        kilometrage,
        garantie_kilometrage,
        boite_de_vitesse,
        transmission,
        couleur,
        garantie,
        date_mise_circulation,
        puissance,
        silhouette,
        nb_places,
        utilisation_prec,
        puissance_fiscale,
        critair,
        ptac,
        nb_portes,
    )
    list_car = []
    est = charge_meilleur_estimateur()
    list_car.append(car)
    f = open("veron_nepveux_project/donnees_UI.json", "w")
    f.write(to_json(list_car))
    f.close()
    car_df = data_frame_pandas("veron_nepveux_project/donnees_UI.json")
    df = assemblage_donnees(
        fichier_peugeot="veron_nepveux_project/donnees_peugeot.json",
        fichier_citroen="veron_nepveux_project/donnees_citroen.json",
        fichier_fiat="veron_nepveux_project/donnees_fiat.json",
        fichier_opel="veron_nepveux_project/donnees_opel.json",
    )
    df_fin = pd.concat([df, car_df], ignore_index=True)
    df_fin_cat = data_frame_dummies(df_fin)
    X_pred, y_pred = data_frame_sklearn(df_fin_cat)
    est_prix = pd.DataFrame(est.predict(X_pred)).iloc[-1][0].round()

    return est_prix, y_pred[-1]
