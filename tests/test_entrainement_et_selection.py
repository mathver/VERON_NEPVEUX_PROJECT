from veron_nepveux_project.entrainement_et_selection import Dataframes, remplit_class
import pytest


def test_Dataframes():
    result = Dataframes(1, 2, 3, 4, 5, 6)
    attendu = Dataframes(X=1, X_tr=2, X_te=3, y=4, y_tr=5, y_te=6)
    assert result == attendu


def test_remplit_class():
    result = remplit_class()
    assert isinstance(
        result, Dataframes
    )  # Je vois pas comment la tester autrement à cause des 4 valeurs pas défaut


def test_elastic_net():
    pass


def test_knn():
    pass


def test_rd_foret():
    pass


def test_svr():
    pass


def test_multi_layer_regressor():
    pass


def test_selection_modele():
    pass


def test_save_meilleur_estimateur():
    pass


def test_charge_meilleur_estimateur():
    pass


def test_prix_predit_voiture():
    pass
