from core.data_classes import Logger, Remote, Config
from core.se_helper import SeleniumHelper


class BaseScreen:
    def __init__(self, config: Config):
        self.__config = config
        self.__base_url = "https://practice.automationtesting.in"
        self.__resource_url = ""
        self.__url = ""
        self.__se_helper = None

    @property
    def log(self) -> Logger:
        return self.__config.log

    @property
    def driver(self) -> Remote:
        return self.__config.driver

    @property
    def resource_url(self) -> str:
        return self.__resource_url

    @resource_url.setter
    def resource_url(self, resource_url: str):
        self.__resource_url = resource_url

    @property
    def url(self) -> str:
        self.__url = "/".join([self.__base_url, self.resource_url])
        return self.__url.format()

    @property
    def se_helper(self) -> SeleniumHelper:
        self.__se_helper = SeleniumHelper(self.__config)
        return self.__se_helper

