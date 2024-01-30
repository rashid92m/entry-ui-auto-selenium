# import os
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.edge.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from core.data_classes import Logger, Config, Remote
from core import logger

# os.environ['WDM_SSL_VERIFY'] = '0'


@fixture(scope="session")
def log() -> Logger:
    return logger.log()


@fixture(scope="session")
def driver() -> Remote:

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    yield driver
    driver.quit()


@fixture(scope="session")
def config(log, driver) -> Config:
    return Config(log, driver)
