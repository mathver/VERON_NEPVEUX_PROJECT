from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from serde import serde
from serde.json import to_json, from_json
from dataclasses import dataclass
from time import sleep


@serde
@dataclass
class Voiture:
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


def accept_cookies(driver: webdriver.chrome.webdriver.WebDriver):
    """Accept cookies on Spoticar pages."""
    button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "_psaihm_id_accept_all_btn"))
    )
    button.click()


def recolt_data(driver):
    car_list = dict()
    for i in range(1, 100):
        if i % 12 == 0:
            driver.find_element(
                By.CSS_SELECTOR, "#see-more-results > .tags-and-alerts-button-text"
            ).click()
        site = f".reskin-product-card:nth-child({i}) .title"
        driver.find_element(By.CSS_SELECTOR, site).click()
        sleep(8)
        home_page = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        sleep(4)

        modele = (driver.find_element(By.CSS_SELECTOR, ".product-line").text,)
        carburant = driver.find_element(
            By.CSS_SELECTOR, ".field_vo_fuel > .title-data"
        ).text
        prix = driver.find_element(By.CSS_SELECTOR, ".price-taxe-div > span").text
        kilometrage = (
            driver.find_element(
                By.CSS_SELECTOR, ".psa-fiche-vo-characteristics-list-km > .title-data"
            ).text,
        )
        garantie_kilometrage = (
            driver.find_element(
                By.CSS_SELECTOR, ".garantie-tooltip > .title-data"
            ).text,
        )
        boite_de_vitesse = (
            driver.find_element(
                By.CSS_SELECTOR, ".field_vo_gear_box > .title-data"
            ).text,
        )

        try:
            transmission = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-transmission > .title-data",
            ).text
        except NoSuchElementException:
            transmission = "NA"
        try:
            couleur = (
                driver.find_element(
                    By.CSS_SELECTOR,
                    ".psa-fiche-vo-characteristics-list-color > .title-data",
                ).text,
            )
        except NoSuchElementException:
            couleur = "NA"
        garantie = (
            driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-warranty > .title-data",
            ).text,
        )
        date_mise_circulation = (
            driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-entry-into-service > .title-data",
            ).text,
        )
        puissance = (
            driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-din-power > .title-data",
            ).text,
        )
        silhouette = (
            driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-silhouette > .title-data",
            ).text,
        )
        nb_places = (
            driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-nbPlaces > .title-data",
            ).text,
        )

        try:
            utilisation_prec = driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-origin > .title-data",
            ).text
        except NoSuchElementException:
            utilisation_prec = "NA"

        puissance_fiscale = (
            driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-fiscal-power > .title-data",
            ).text,
        )
        critair = (
            driver.find_element(
                By.CSS_SELECTOR,
                ".psa-fiche-vo-characteristics-list-green-zone > .title-data",
            ).text,
        )

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

        car_list[f"car{i}"] = Voiture(
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

        driver.execute_script("window.close('');")
        driver.switch_to.window(home_page)
        sleep(3)
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

    modele = modele[0][8:]
    carburant = carburant
    kilometrage = int(str(kilometrage[0][:-3]).replace(" ", ""))
    prix = int(str(prix[:-2].replace(" ", "")))
    garantie_kilometrage = garantie_kilometrage[0]
    boite_de_vitesse = boite_de_vitesse[0]
    if transmission == "NA":
        pass
    else:
        transmission = transmission[0]
    if couleur == "NA":
        couleur = couleur
    else:
        couleur = couleur[0]

    garantie = garantie[0]
    date_mise_circulation = int(date_mise_circulation[0][3:])
    puissance = int(str(puissance[0][:-3]).replace(" ", ""))
    silhouette = silhouette[0]
    nb_places = int(nb_places[0])
    puissance_fiscale = int(str(puissance_fiscale[0][:-3]).replace(" ", ""))
    critair = critair[0][len(critair[0]) - 1]

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


def acces_site(URL):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    sleep(2)
    accept_cookies(driver)
    sleep(3)
    driver.find_element(By.ID, "search-input-filter-home").click()
    sleep(2)
    driver.find_element(By.ID, "search-input-filter-home").send_keys(
        "Peugeot" + Keys.ENTER
    )
    sleep(5)
    driver.find_element(By.ID, "count").click()
    sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    resultat = recolt_data(driver)
    return resultat
