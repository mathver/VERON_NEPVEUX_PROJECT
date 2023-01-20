import numpy as np
import pandas as pd
import veron_nepveux_project.conversion_df as conv
from veron_nepveux_project.scraping import Voiture


def test_dataframe_modele():
    realite = conv.data_frame_modele()[0][0]
    prevu = np.array(
        [
            7.5967e04,
            2.0190e03,
            1.3000e02,
            5.0000e00,
            6.0000e00,
            2.0000e00,
            1.8900e03,
            5.0000e00,
            0.0000e00,
            1.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            1.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            1.0000e00,
            1.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            1.0000e00,
            0.0000e00,
            1.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            1.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            1.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            1.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            1.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
            0.0000e00,
        ]
    )
    assert np.all(realite == prevu)


def test_assemblage():
    df = conv.assemblage_donnees()
    realite = df.iloc[0:1]
    predit = pd.DataFrame.from_dict(
        {
            "marque": {0: "Peugeot"},
            "modele": {0: "308"},
            "carburant": {0: "Diesel"},
            "prix": {0: 20290},
            "kilometrage": {0: 75967.0},
            "garantie_kilometrage": {0: "non garanti"},
            "boite_de_vitesse": {0: "Automatique"},
            "transmission": {0: 2.0},
            "couleur": {0: "Blanc"},
            "garantie": {0: "SPOTICAR PREMIUM"},
            "date_mise_circulation": {0: 2019},
            "puissance": {0: 130.0},
            "silhouette": {0: "Berline"},
            "nb_places": {0: 5.0},
            "utilisation_prec": {0: "Ex-Loueur"},
            "puissance_fiscale": {0: 6.0},
            "critair": {0: 2.0},
            "ptac": {0: 1890.0},
            "nb_portes": {0: 5.0},
        }
    )

    assert pd.testing.assert_frame_equal(realite, predit) is None


def test_ouverture_fichier():
    realite = conv._ouverture_fichier("./veron_nepveux_project/donnees_peugeot.json")[
        1:398
    ]
    predit = """{"marque":"Peugeot","modele":"308","carburant":"Diesel",
    "prix":20290,"kilometrage":75967,
    "garantie_kilometrage":"non garanti","boite_de_vitesse":"Automatique","transmission":2,
    "couleur":"Blanc","garantie":"SPOTICAR PREMIUM","date_mise_circulation":2019,"puissance":130,
    "silhouette":"Berline","nb_places":5,"utilisation_prec":"Ex-Loueur",
    "puissance_fiscale":6,"critair":2,"ptac":1890,"nb_portes":5}"""
    assert predit == realite


def test_reconstitution_fichier():
    realite = conv._reconstitution_fichier(
        """[{"marque":"Peugeot","modele":"308","carburant":"Diesel","prix":20290,
        "kilometrage":75967,"garantie_kilometrage":"non garanti","boite_de_vitesse":"Automatique",
        "transmission":2,"couleur":"Blanc","garantie":"SPOTICAR PREMIUM",
        "date_mise_circulation":2019,
        "puissance":130,"silhouette":"Berline","nb_places":5,"utilisation_prec":"Ex-Loueur",
        "puissance_fiscale":6,"critair":2,"ptac":1890,"nb_portes":5}]"""
    )
    predit = [
        Voiture(
            marque="Peugeot",
            modele="308",
            carburant="Diesel",
            prix=20290,
            kilometrage=75967,
            garantie_kilometrage="non garanti",
            boite_de_vitesse="Automatique",
            transmission=2,
            couleur="Blanc",
            garantie="SPOTICAR PREMIUM",
            date_mise_circulation=2019,
            puissance=130,
            silhouette="Berline",
            nb_places=5,
            utilisation_prec="Ex-Loueur",
            puissance_fiscale=6,
            critair=2,
            ptac=1890,
            nb_portes=5,
        )
    ]
    assert realite == predit


def test_data_frame_pandas():
    realite = conv.data_frame_pandas(
        "./veron_nepveux_project/donnees_peugeot.json"
    ).iloc[0:2]
    predit = pd.DataFrame.from_dict(
        {
            "marque": {0: "Peugeot", 1: "Peugeot"},
            "modele": {0: "308", 1: "3008"},
            "carburant": {0: "Diesel", 1: "Diesel"},
            "prix": {0: 20290, 1: 31900},
            "kilometrage": {0: 75967, 1: 29066},
            "garantie_kilometrage": {0: "non garanti", 1: "non garanti"},
            "boite_de_vitesse": {0: "Automatique", 1: "Manuelle"},
            "transmission": {0: 2.0, 1: 2.0},
            "couleur": {0: "Blanc", 1: "Gris"},
            "garantie": {0: "SPOTICAR PREMIUM", 1: "SPOTICAR PREMIUM"},
            "date_mise_circulation": {0: 2019, 1: 2021},
            "puissance": {0: 130.0, 1: 130.0},
            "silhouette": {0: "Berline", 1: "SUV-4x4"},
            "nb_places": {0: 5.0, 1: 5.0},
            "utilisation_prec": {0: "Ex-Loueur", 1: "Ex-Loueur"},
            "puissance_fiscale": {0: 6.0, 1: 7.0},
            "critair": {0: 2.0, 1: 2.0},
            "ptac": {0: 1890.0, 1: 1875.0},
            "nb_portes": {0: 5.0, 1: 5.0},
        }
    )
    assert pd.testing.assert_frame_equal(predit, realite) is None


def test_data_frame_imputation():
    df = conv.data_frame_pandas("./veron_nepveux_project/donnees_peugeot.json").iloc[
        0:2
    ]
    realite = conv.data_frame_imputation(df)
    predit = pd.DataFrame.from_dict(
        {
            "marque": {0: "Peugeot", 1: "Peugeot"},
            "modele": {0: "308", 1: "3008"},
            "carburant": {0: "Diesel", 1: "Diesel"},
            "prix": {0: 20290, 1: 31900},
            "kilometrage": {0: 75967, 1: 29066},
            "garantie_kilometrage": {0: "non garanti", 1: "non garanti"},
            "boite_de_vitesse": {0: "Automatique", 1: "Manuelle"},
            "transmission": {0: 2.0, 1: 2.0},
            "couleur": {0: "Blanc", 1: "Gris"},
            "garantie": {0: "SPOTICAR PREMIUM", 1: "SPOTICAR PREMIUM"},
            "date_mise_circulation": {0: 2019, 1: 2021},
            "puissance": {0: 130.0, 1: 130.0},
            "silhouette": {0: "Berline", 1: "SUV-4x4"},
            "nb_places": {0: 5.0, 1: 5.0},
            "utilisation_prec": {0: "Ex-Loueur", 1: "Ex-Loueur"},
            "puissance_fiscale": {0: 6.0, 1: 7.0},
            "critair": {0: 2.0, 1: 2.0},
            "ptac": {0: 1890.0, 1: 1875.0},
            "nb_portes": {0: 5.0, 1: 5.0},
        }
    )
    assert pd.testing.assert_frame_equal(predit, realite) is None


def test_data_frame_dummies():
    df = conv.data_frame_pandas("./veron_nepveux_project/donnees_peugeot.json").iloc[
        0:2
    ]
    realite = conv.data_frame_dummies(df)
    predit = pd.DataFrame.from_dict(
        {
            "prix": {0: 20290, 1: 31900},
            "kilometrage": {0: 75967, 1: 29066},
            "date_mise_circulation": {0: 2019, 1: 2021},
            "puissance": {0: 130.0, 1: 130.0},
            "nb_places": {0: 5.0, 1: 5.0},
            "puissance_fiscale": {0: 6.0, 1: 7.0},
            "critair": {0: 2.0, 1: 2.0},
            "ptac": {0: 1890.0, 1: 1875.0},
            "nb_portes": {0: 5.0, 1: 5.0},
            "Peugeot": {0: 1, 1: 1},
            "3008": {0: 0, 1: 1},
            "308": {0: 1, 1: 0},
            "non garanti": {0: 1, 1: 1},
            "Diesel": {0: 1, 1: 1},
            "Automatique": {0: 1, 1: 0},
            "Manuelle": {0: 0, 1: 1},
            "Blanc": {0: 1, 1: 0},
            "Gris": {0: 0, 1: 1},
            "Berline": {0: 1, 1: 0},
            "SUV-4x4": {0: 0, 1: 1},
            2.0: {0: 1, 1: 1},
            "SPOTICAR PREMIUM": {0: 1, 1: 1},
            "Ex-Loueur": {0: 1, 1: 1},
        }
    )
    assert pd.testing.assert_frame_equal(predit, realite, check_dtype=False) is None


def test_data_frame_sklearn():
    df = conv.data_frame_pandas("./veron_nepveux_project/donnees_peugeot.json").iloc[
        0:2
    ]
    realite_X, realite_y = conv.data_frame_sklearn(df)
    predit_x = np.array(
        [
            [
                "Peugeot",
                "308",
                "Diesel",
                75967,
                "non garanti",
                "Automatique",
                2.0,
                "Blanc",
                "SPOTICAR PREMIUM",
                2019,
                130.0,
                "Berline",
                5.0,
                "Ex-Loueur",
                6.0,
                2.0,
                1890.0,
                5.0,
            ],
            [
                "Peugeot",
                "3008",
                "Diesel",
                29066,
                "non garanti",
                "Manuelle",
                2.0,
                "Gris",
                "SPOTICAR PREMIUM",
                2021,
                130.0,
                "SUV-4x4",
                5.0,
                "Ex-Loueur",
                7.0,
                2.0,
                1875.0,
                5.0,
            ],
        ],
        dtype=object,
    )
    predit_y = np.array([20290, 31900], dtype=np.int64)

    assert np.all(realite_X == predit_x) and np.all(realite_y == predit_y)
