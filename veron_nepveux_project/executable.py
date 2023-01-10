from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn
import os
import typer
from scrapping import acces_site
import interface_estimation

URL = "https://www.spoticar.fr"

app = typer.Typer(pretty_exceptions_show_locals=True)


@app.callback()
def callback():
    """
    This application allows the user to scrap data about car on the car seller Spoticar and to test the price of its own against the market.
    """


@app.command()
def scrapping():
    """
    The fonction which allow the user to scrap data on the Spoticar website about Peugeot branded car.
    The limit of data is 600 and depend on your internet connection, time for 600 data is estimate to be 2 hours.
    """
    acces_site()


@app.command()
def estimating():
    """
    This command allow the user to estimate his car by filling a form with the parameter and compare it to the database and the model estimate previously.
    """
    interface_estimation.app()


if __name__ == "__main__":
    app()
