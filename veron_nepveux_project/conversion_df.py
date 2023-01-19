"""
Description : 

Librairie python permettant la création et la modification d'un dataframe utilisable 
par la bibliothèque sklearn à partir des données scrapper précedemment.
"""

from serde.json import from_json
from scrapping import Voiture
import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin


def data_frame_modele(
    fichier_peugeot: str = "donnees_peugeot.json",
    fichier_citroen: str = "donnees_citroen.json",
    fichier_fiat: str = "donnees_fiat.json",
    fichier_opel: str = "donnees_opel.json",
) -> dict:
    """
    # Description

    Fonction permettant de convertir des fichiers de données au format json contenant des objets de la classe `Voiture` en dataframe 
    compatible avec les modèles du module `sklearn`.
    
    ## Paramètres

    - fichier_peugeot (str): Fichier contenant les données de la marque Peugeot.\\
    Valeur par défault : "donnees_peugeot.json"
    - fichier_citroen (str): Fichier contenant les données de la marque Citroën.\\
    Valeur par défault : "donnees_citroen.json"
    
    ## Sortie 

    Deux dictionnaire crée par la fonction `data_frame_sklearn` permettant l'implémentation dans sklearn.
    """
    df = assemblage_donnees(
        fichier_peugeot, fichier_citroen, fichier_fiat, fichier_opel
    )
    data_fin = data_frame_dummies(df)
    return data_frame_sklearn(data_fin)


def assemblage_donnees(
    fichier_peugeot: str, fichier_citroen: str, fichier_fiat: str, fichier_opel: str
) -> pd.core.frame.DataFrame:
    """
    # Description

    Fonction permettant l'assemblage des différents fichiers json de données concernant les voitures (`Voiture`) pour créer un 
    seul `dataframe` exploitable dans les autres fonctions.
    
    ## Paramètres

    - fichier_peugeot (str): Fichier contenant les données de la marque Peugeot.\\
    Valeur par défault : "donnees_peugeot.json"
    - fichier_citroen (str): Fichier contenant les données de la marque Citroën.\\
    Valeur par défault : "donnees_citroen.json"
    
    ## Sortie 

    Un dataframe du module `pandas` contenant toutes les données disponibles.
    """
    df1 = data_frame_pandas(fichier_peugeot)
    df2 = data_frame_pandas(fichier_citroen)
    df3 = data_frame_pandas(fichier_fiat)
    df4 = data_frame_pandas(fichier_opel)
    df = pd.concat([df1, df2, df3, df4], ignore_index=True)
    return df


def _ouverture_fichier(donnees: str) -> str:
    """
    # Description

    Fonction permettant d'ouvrir le fichier json pour en extraitre les données après.
    
    ## Paramètres
    - donnees (str): Fichier contenant les données de la marque Peugeot.\\
    Valeur par défault : "donnees_peugeot.json"
    
    ## Sortie 

    Une chaîne de caractères des données contenues dans le fichier json.
    """
    with open(donnees, "r") as fichier:
        contenu_fichier = fichier.read()
    return contenu_fichier


def _reconstitution_fichier(contenu: str) -> list[Voiture]:
    """
    # Description

    Fonction permettant de reconstituer une liste d'objets de classe `Voiture` à partir de la chaîne de caractères extraite
    du fichier json.

    ## Paramètres
    - contenu (str): Chaîne de caractère contenant des objets de classe `Voiture`.

    ## Sortie

    Une liste d'objets de classe `Voiture`
    """
    return from_json(list[Voiture], contenu)


def data_frame_pandas(fichier) -> pd.core.frame.DataFrame:
    """
    # Description

    Fonction permettant de constituer un dataframe du module `pandas` à partir d'un fichier json contenant différents objets de la 
    classe `Voiture`.
    
    ## Paramètres
    - fichier (str): fichier json contenant les données.\\
        Valeur par défaut : 'donnees_peugeot.json'
    
    ## Sortie 

    Un dataframe du module `pandas`.
    """
    contenu = _ouverture_fichier(fichier)
    df = _reconstitution_fichier(contenu)
    df = pd.DataFrame(df)
    df = data_frame_imputation(df)
    return df


def data_frame_imputation(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """
    # Description

    Fonction permettant d'imputer les valeurs manquantes `NaN` d'un dataframe.

    Les données numériques sont imputées selon la moyenne, les données catégorielles selon la valeur majoritaire.

    ## Paramètres
    - df (pd.core.frame.DataFrame) : dataframe du module `pandas`.

    ## Sortie

    Un dataframe du module `pandas` sans données manquantes.
    """
    df = df.replace("NA", np.NaN)
    df = DataFrameImputer().fit_transform(df)
    return df


def data_frame_dummies(df: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """
    # Description

    Fonction permettant de transformer les variables catégorielles en variables dichotomique.

    On notera la création d'un certain nombre de colonnes par la fonction pour la création de ces variables.

    ## Paramètres
    - df (pd.core.frame.DataFrame) : dataframe du module `pandas`.

    ## Sortie

    Un dataframe du module `pandas` avec des variables dichotomique pour remplacer les catégorielles.
    """
    df_marque = pd.get_dummies(df["marque"])
    df_mod = pd.get_dummies(df["modele"])
    df_garkil = pd.get_dummies(df["garantie_kilometrage"])
    df_carbu = pd.get_dummies(df["carburant"])
    df_bdv = pd.get_dummies(df["boite_de_vitesse"])
    df_couleur = pd.get_dummies(df["couleur"])
    df_sil = pd.get_dummies(df["silhouette"])
    df_trans = pd.get_dummies(df["transmission"])
    df_gar = pd.get_dummies(df["garantie"])
    df_utilprec = pd.get_dummies(df["utilisation_prec"])
    df = pd.concat(
        [
            df,
            df_marque,
            df_mod,
            df_garkil,
            df_carbu,
            df_bdv,
            df_couleur,
            df_sil,
            df_trans,
            df_gar,
            df_utilprec,
        ],
        axis=1,
    )
    del df["marque"]
    del df["modele"]
    del df["garantie_kilometrage"]
    del df["carburant"]
    del df["boite_de_vitesse"]
    del df["couleur"]
    del df["silhouette"]
    del df["transmission"]
    del df["garantie"]
    del df["utilisation_prec"]
    return df


def data_frame_sklearn(df: pd.core.frame.DataFrame) -> dict:
    """
    # Description

    Fonction permettant de transformer un dataframe en données compatibles avec `sklearn`.

    ## Paramètres
    - df (pd.core.frame.DataFrame) : dataframe du module `pandas`.

    ## Sortie

    Deux dictionnaires permettant la compatibilité avec le module `sklearn`.

    X contient les variables, et y contient les prix.
    """
    X = df.loc[:, df.columns != "prix"].to_numpy()  # tout sauf le prix
    y = df["prix"].to_numpy()
    return X, y


class DataFrameImputer(TransformerMixin):
    """
    # Description
    Classe permettant de faciliter l'imputation des données dans la fonction `data_frame_imputation`.
    """

    def __init__(self):
        pass

    def fit(self, df, y=None):
        self.fill = pd.Series(
            [
                df[c].value_counts().index[0]
                if df[c].dtype == np.dtype("O")
                else df[c].mean().round()
                for c in df
            ],
            index=df.columns,
        )
        return self

    def transform(self, df, y=None):
        return df.fillna(self.fill)
