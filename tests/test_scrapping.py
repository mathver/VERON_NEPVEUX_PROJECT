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

from veron_nepveux_project.scrapping import formalisation, scrap_marque