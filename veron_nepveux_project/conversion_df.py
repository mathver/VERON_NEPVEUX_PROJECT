"""
Description : 

Librairie python permettant la création et la modification d'un data frame utilisable 
par la bibliothèque sklearn

"""

from serde.json import  from_json
from scrapping import Voiture
import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin


def data_frame(fichier : str = "donnees.json", modele_choisi : str = "non"):
    df = ouverture_fichier(fichier)
    reconstitue = reconstitution_fichier(df)
    df_panda = dataframe_pandas(reconstitue)
    data_dumm = data_frame_dummies(df_panda)
    data_no_NA = data_frame_sans_NA(data_dumm)
    return data_frame_sklearn(data_no_NA)

def ouverture_fichier(donnees ="donnees.json") :
    with open(donnees, "r") as fichier:
        contenu_fichier = fichier.read()
    return contenu_fichier

def reconstitution_fichier(fichier = "donnees.json")-> list[Voiture]:
    return(
        from_json(list[Voiture],fichier)
    )

def dataframe_pandas(fichier = "donnees.json") -> pd.core.frame.DataFrame:
    return(
        pd.DataFrame(fichier)
    )

def data_frame_sans_NA(df : pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    df.replace('NA', np.NaN)
    df = DataFrameImputer().fit_transform(df)
    return(df)

def data_frame_dummies(df : pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    df_mod = pd.get_dummies(df["modele"])
    df_garkil = pd.get_dummies(df["garantie_kilometrage"])
    df_carbu = pd.get_dummies(df["carburant"])
    df_bdv = pd.get_dummies(df["boite_de_vitesse"])
    df_couleur = pd.get_dummies(df["couleur"])
    df_sil = pd.get_dummies(df["silhouette"])
    df_trans = pd.get_dummies(df["transmission"])
    df_gar = pd.get_dummies(df["garantie"])
    df_utilprec = pd.get_dummies(df["utilisation_prec"])
    df = pd.concat([df, df_mod, df_garkil, df_carbu, df_bdv, df_couleur, df_sil,df_trans, df_gar, df_utilprec], axis = 1)
    del df['modele']
    del df['garantie_kilometrage']
    del df['carburant']
    del df['boite_de_vitesse']
    del df['couleur']
    del df['silhouette']
    del df['transmission']
    del df['garantie']
    del df['utilisation_prec']
    return(df)
    

def data_frame_sklearn(df : pd.core.frame.DataFrame) -> dict:
    
    return(
        {'X': df.loc[:, df.columns != 'prix'].to_numpy(), 'y' : df['prix'].to_numpy(), 'df_entier': df.to_numpy()}
    )
    

class DataFrameImputer(TransformerMixin):

    def __init__(self):
        """Impute missing values.

        Columns of dtype object are imputed with the most frequent value 
        in column.

        Columns of other types are imputed with mean of column.

        """
    def fit(self, df, y=None):

        self.fill = pd.Series([df[c].value_counts().index[0]
            if df[c].dtype == np.dtype('O') else df[c].mean() for c in df],
            index=df.columns)

        return self

    def transform(self, df, y=None):
        return df.fillna(self.fill)

#df = DataFrameImputer().fit_transform(df)
