from os.path import exists
from veron_nepveux_project.scrapping import Voiture, formalisation, scrap_marque


def test_Voiture():
    resultat = Voiture(
        marque="Fiat",
        modele="PANDA",
        carburant="Essence",
        prix=10690,
        kilometrage=42500,
        garantie_kilometrage="non garanti",
        boite_de_vitesse="Manuelle",
        transmission=2,
        couleur="Noir",
        garantie="SPOTICAR PREMIUM",
        date_mise_circulation=2018,
        puissance=69,
        silhouette="Citadine",
        nb_places=5,
        utilisation_prec="NA",
        puissance_fiscale=4,
        critair=1,
        ptac="NA",
        nb_portes=5,
    )
    attendu = Voiture(
        marque="Fiat",
        modele="PANDA",
        carburant="Essence",
        prix=10690,
        kilometrage=42500,
        garantie_kilometrage="non garanti",
        boite_de_vitesse="Manuelle",
        transmission=2,
        couleur="Noir",
        garantie="SPOTICAR PREMIUM",
        date_mise_circulation=2018,
        puissance=69,
        silhouette="Citadine",
        nb_places=5,
        utilisation_prec="NA",
        puissance_fiscale=4,
        critair=1,
        ptac="NA",
        nb_portes=5,
    )

    assert attendu == resultat


def test_formalisation():
    resultat = formalisation(
        marque="fiat",
        modele="FIAT PANDA",
        carburant="Essence",
        prix="10 690 €",
        kilometrage="42 500 km",
        garantie_kilometrage="non garanti",
        boite_de_vitesse="Manuelle",
        transmission="2 roues motrice",
        couleur="Noir",
        garantie="SPOTICAR PREMIUM",
        date_mise_circulation="01/2018",
        puissance="69 cv",
        silhouette="Citadine",
        nb_places="5 places",
        utilisation_prec="Ex-Particulier",
        puissance_fiscale="4 cv",
        critair="critair 1",
        ptac="1500 kg",
        nb_portes="5",
    )
    attendu = (
        "fiat",
        "PANDA",
        "Essence",
        10690,
        42500,
        "non garanti",
        "Manuelle",
        2,
        "Noir",
        "SPOTICAR PREMIUM",
        2018,
        69,
        "Citadine",
        5,
        "Ex-Particulier",
        4,
        1,
        1500,
        5,
    )
    assert attendu == resultat


def test_scrap_marque():
    scrap_marque("https://www.spoticar.fr", ("audi", "bmw"), 3)
    assert exists("donnees_audi.json") and exists("donnees_bmw.json")


# Ce test est aussi fonctionnel pour les cookies et recolt_data
# Il permet aussi de comprendre lors de son exécution du choix des marques (manque de données)
def test_recolt_data():
    pass


def test_accept_cookies():
    pass
