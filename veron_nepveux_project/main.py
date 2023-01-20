"""
Librairie qui permet la création d'une interface en ligne de commande pour l'ensemble du programme.
"""

import typer
from veron_nepveux_project.scraping import scrap_marque
from veron_nepveux_project.entrainement_et_selection import selection_modele


app = typer.Typer()


@app.callback()
def callback():
    """
    Programme pour exécuter le scraping et lancer l'UI pour l'estimation du prix du véhicule.
    """


@app.command()
def scraping():
    """
    Commande permettant l'exécution du programme de scraping
    sur les quatre marques pour recréer une base de données.

    Les marques disponibles sont : Peugeot, Citroën, Opel et Fiat.
    """
    scrap_marque("https://www.spoticar.fr", ("peugeot", "citroen", "opel", "fiat"))
    selection_modele()


@app.command()
def estimation():
    """
    Commande permettant d'ouvrir l'UI pour l'estimation du prix du véhicule de l'utilisateur.
    """
    import veron_nepveux_project.interface_estimation as interface_estimation

    interface_estimation


if __name__ == "__main__":
    app()
