"""
Librairie de scrapping permettant la récupération de données sur le site spoticar pour différentes marques de voiture, et transformant les données en fichier .json. 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from serde import serde
from serde.json import to_json
from dataclasses import dataclass
from time import sleep


@serde
@dataclass
class Voiture:
    marque: str
    modele: str
    carburant: str
    prix: int
    kilometrage: int
    garantie_kilometrage: str
    boite_de_vitesse: str
    transmission: int
    couleur: str
    garantie: str
    date_mise_circulation: int
    puissance: int
    silhouette: str
    nb_places: int
    utilisation_prec: str
    puissance_fiscale: int
    critair: int
    ptac: int
    nb_portes: int


URL = "https://www.spoticar.fr"


def accept_cookies(driver: webdriver.chrome.webdriver.WebDriver):
    """Accept cookies on Spoticar pages."""
    button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "_psaihm_id_accept_all_btn"))
    )
    button.click()


def recolt_data(driver, marque):
    car_list = list()
    for i in range(1, 6):
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
):
    if modele == "NA":
        modele = modele
    else:
        modele = modele[8:]

    carburant = carburant

    if kilometrage == "NA":
        kilometrage = kilometrage
    else:
        try:
            kilometrage = int(str(kilometrage[:-3]).replace(" ", ""))
        except:
            kilometrage = kilometrage

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


def scrap_marque(URL: str, marque: str):
    driver = webdriver.Chrome()
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
    resultat = recolt_data(driver, marque)
    f = open(f"donnees_{marque}.json", "w")
    f.write(to_json(resultat))
