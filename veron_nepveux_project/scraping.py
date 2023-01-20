"""
Librairie de scrapping permettant la récupération de données
sur le site spoticar pour différentes marques de voiture,
et transformant les données en fichier .json.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from serde import serde
from serde.json import to_json
from dataclasses import dataclass
from time import sleep
from typing import Union
import veron_nepveux_project.scraping


@serde
@dataclass
class Voiture:
    """
    # Description

    Dataclasse permettant de créer un objet `Voiture` prenant un certain nombre de paramètres.

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
    """

    marque: str
    modele: str
    carburant: str
    prix: int | str
    kilometrage: int | str
    garantie_kilometrage: str
    boite_de_vitesse: str
    transmission: int | str
    couleur: str
    garantie: str
    date_mise_circulation: int | str
    puissance: int | str
    silhouette: str
    nb_places: int | str
    utilisation_prec: str
    puissance_fiscale: int | str
    critair: int | str
    ptac: int | str
    nb_portes: int | str


URL = "https://www.spoticar.fr"


def accept_cookies(driver: webdriver.chrome.webdriver.WebDriver) -> None:
    """
    # Description

    Fonction permettant d'accepter les cookies une fois le site ouvert.

    ## Paramètres

    - driver (webdriver.chrome.webdriver.WebDriver): Driver utilisé
    avec `Selenium` pour ouvrir la page web.
    """
    button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "_psaihm_id_accept_all_btn"))
    )
    button.click()


def recolt_data(
    driver: webdriver.chrome.webdriver.WebDriver, marque: str, max: int
) -> list[Voiture]:
    """
    # Description

    Fonction permettant la récupération des données sur chaque fiche véhicule
    du site pour ensuite créer un fichier json par marque
    de véhicule.

    ## Paramètres

    - driver (webdriver.chrome.webdriver.WebDriver):  driver utilisé avec
    `Selenium` pour ouvrir la page web.
    - marque (str): marque des véhicules à scraper.

    ## Sortie

    Une liste d'objet `Voiture`

    """
    car_list = list()
    for i in range(1, max):
        if i % 12 == 0:
            driver.find_element(
                By.CSS_SELECTOR, "#see-more-results > .tags-and-alerts-button-text"
            ).click()
            sleep(3)
        sleep(1)
        site = f".reskin-product-card:nth-child({i}) .title"
        driver.find_element(By.CSS_SELECTOR, site).click()
        sleep(2)
        home_page = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        try:
            modele = driver.find_element(By.CSS_SELECTOR, ".product-line").text
        except NoSuchElementException:
            modele = "NA"

        try:
            carburant = driver.find_element(
                By.CSS_SELECTOR, ".field_vo_fuel > .title-data"
            ).text
        except NoSuchElementException:
            carburant = "NA"

        try:
            prix = driver.find_element(By.CSS_SELECTOR, ".price-taxe-div > span").text
        except NoSuchElementException:
            prix = "NA"

        try:
            kilometrage = driver.find_element(
                By.CSS_SELECTOR, ".psa-fiche-vo-characteristics-list-km > .title-data"
            ).text
        except NoSuchElementException:
            kilometrage = "NA"

        try:
            garantie_kilometrage = driver.find_element(
                By.CSS_SELECTOR, ".garantie-tooltip > .title-data"
            ).text
        except NoSuchElementException:
            garantie = "NA"

        try:
            boite_de_vitesse = driver.find_element(
                By.CSS_SELECTOR, ".field_vo_gear_box > .title-data"
            ).text
        except NoSuchElementException:
            boite_de_vitesse = "NA"

        try:
            transmission = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-transmission > .title-data",
            ).text
        except NoSuchElementException:
            transmission = "NA"

        try:
            couleur = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-color > .title-data",
            ).text
        except NoSuchElementException:
            couleur = "NA"

        try:
            garantie = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-warranty > .title-data",
            ).text
        except NoSuchElementException:
            garantie = "NA"

        try:
            date_mise_circulation = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-entry-into-service > .title-data",
            ).text
        except NoSuchElementException:
            date_mise_circulation = "NA"

        try:
            puissance = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-din-power > .title-data",
            ).text
        except NoSuchElementException:
            puissance = "NA"

        try:
            silhouette = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-silhouette > .title-data",
            ).text
        except NoSuchElementException:
            silhouette = "NA"

        try:
            nb_places = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-nbPlaces > .title-data",
            ).text
        except NoSuchElementException:
            nb_places = "NA"

        try:
            utilisation_prec = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-origin > .title-data",
            ).text
        except NoSuchElementException:
            utilisation_prec = "NA"

        try:
            puissance_fiscale = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-fiscal-power > .title-data",
            ).text
        except NoSuchElementException:
            puissance_fiscale = "NA"

        try:
            critair = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-green-zone > .title-data",
            ).text
        except NoSuchElementException:
            critair = "NA"

        try:
            ptac = driver.find_element(
                By.CSS_SELECTOR, ".psa-fiche-vo-characteristics-list-ptac > .title-data"
            ).text
        except NoSuchElementException:
            ptac = "NA"

        try:
            nb_portes = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-nb-portes > .title-data",
            ).text
        except NoSuchElementException:
            nb_portes = "NA"

        (
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
        ) = formalisation(
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
        car_list.append(car)
        try:
            driver.find_element(By.CSS_SELECTOR, ".a.ng-binding").click()
        except NoSuchElementException:
            pass
        driver.switch_to.window(window_after)
        try:
            driver.execute_script("window.close('');")
        except WebDriverException:
            pass
        driver.switch_to.window(home_page)
        sleep(0.5)
    driver.quit()
    return car_list


def formalisation(
    marque: str,
    modele: str,
    carburant: str,
    prix: str,
    kilometrage: str,
    garantie_kilometrage: str,
    boite_de_vitesse: str,
    transmission: str,
    couleur: str,
    garantie: str,
    date_mise_circulation: str,
    puissance: str,
    silhouette: str,
    nb_places: str,
    utilisation_prec: str,
    puissance_fiscale: str,
    critair: str,
    ptac: str,
    nb_portes: str,
) -> Union[str, int]:
    """
    # Description

    Fonction permettant la formalisation des données récupérées pour
    chaque véhicule en ne gardant que les nombres pour les valeurs
    numériques, et des catégories pour le reste.

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

    Les variables typées de la bonne façon.
    """
    if modele == "NA":
        modele = modele
    elif marque == "peugeot":
        modele = modele[8:]
    elif marque == "citroen":
        modele = modele[8:]
    else:
        modele = modele[5:]

    carburant = carburant

    if kilometrage == "NA":
        kilometrage = kilometrage
    else:
        kilometrage = int(str(kilometrage[:-3]).replace(" ", ""))

    if prix == "NA":
        prix = prix
    else:
        prix = int(str(prix[:-2].replace(" ", "")))

    if garantie_kilometrage == "NA":
        garantie_kilometrage = garantie_kilometrage
    else:
        garantie_kilometrage = garantie_kilometrage

    if boite_de_vitesse == "NA":
        boite_de_vitesse = boite_de_vitesse
    else:
        boite_de_vitesse = boite_de_vitesse

    if transmission == "NA":
        pass
    else:
        transmission = int(transmission[0])

    if couleur == "NA":
        couleur = couleur
    else:
        couleur = couleur

    if garantie == "NA":
        garantie = garantie
    else:
        garantie = garantie

    if date_mise_circulation == "NA":
        date_mise_circulation = date_mise_circulation
    else:
        date_mise_circulation = int(date_mise_circulation[3:])

    if puissance == "NA":
        puissance = puissance
    else:
        puissance = int(str(puissance[:-3]).replace(" ", ""))

    if silhouette == "NA":
        silhouette = silhouette
    else:
        silhouette = silhouette

    if nb_places == "NA":
        nb_places = nb_places
    else:
        nb_places = int(nb_places[0])

    if puissance_fiscale == "NA":
        puissance_fiscale = puissance_fiscale
    else:
        puissance_fiscale = int(str(puissance_fiscale[:-3]).replace(" ", ""))

    if critair == "NA":
        critair = critair
    else:
        critair = int(critair[7:])

    if ptac == "NA":
        ptac = ptac
    else:
        ptac = int(str(ptac[:-3]))

    if nb_portes == "NA":
        nb_portes = nb_portes
    else:
        nb_portes = int(nb_portes)

    if utilisation_prec == "NA":
        utilisation_prec = utilisation_prec
    else:
        utilisation_prec = utilisation_prec

    return (
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


def scrap_marque(URL: str, marques: list[str], max: int = 601) -> str:
    """
    # Description

    Fonction permettant d'ouvrir la page web, d'accéder aux fiches véhicules,
    de récupérer les données et de les stocker. La fonction
    se répète sur les quatres marques (Peugeot, Citroën, Opel et Fiat).

    ## Paramètres

    - URL (str): URL du site web
    - marques (list[str]): liste des marques à scraper.

    ## Sortie

    Quatre fichiers json chacun correspondant à une marque et composés d'objets de la classe `Voiture`.
    """
    for marque in marques:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        driver.maximize_window()
        driver.get(URL)
        sleep(2)
        accept_cookies(driver)
        sleep(3)
        driver.find_element(By.ID, "search-input-filter-home").click()
        sleep(2)
        driver.find_element(By.ID, "search-input-filter-home").send_keys(
            f"{marque}" + Keys.ENTER
        )
        sleep(5)
        driver.find_element(By.ID, "count").click()
        sleep(5)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        resultat = recolt_data(driver, marque, max)
        path = veron_nepveux_project.scraping.__file__[:-11]
        f = open(path + f"donnees_{marque}.json", "w")
        f.write(to_json(resultat))
