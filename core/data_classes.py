from logging import Logger
from dataclasses import dataclass
from selenium.webdriver import Remote


@dataclass
class Element:
    by: str
    value: str
    name: str


@dataclass
class Config:
    log: Logger
    driver: Remote
