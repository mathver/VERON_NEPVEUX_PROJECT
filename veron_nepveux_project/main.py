"""
Librairie qui permet la création d'une interface en ligne de commande pour l'ensemble du programme.
"""

import typer
from scrapping import scrap_marque


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


@app.command()
def estimation():
    """
    Commande permettant d'ouvrir l'UI pour l'estimation du prix du véhicule de l'utilisateur.
    """
    import interface_estimation

    interface_estimation


if __name__ == "__main__":
    app()
