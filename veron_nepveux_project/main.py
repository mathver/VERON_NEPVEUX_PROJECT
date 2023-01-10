"""
Librairie qui permet la création d'une interface en ligne de commande pour l'ensemble du programme.
"""

import typer
from scrapping import scrap_marque

app = typer.Typer()


@app.callback()
def callback():
    """
    Programme pour exécuter le scrapping et l'estimation.
    """


@app.command()
def scrapping():
    scrap_marque('https://spoticar.fr', 'Peugeot')


@app.command()
def estimation():
    import interface_estimation

if __name__ == "__main__":
    app()