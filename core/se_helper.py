from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from core.data_classes import Config, Element


class SeleniumHelper:
    def __init__(self, config: Config):
        self.__config = config

    def get_element(self, element: Element) -> WebElement:
        try:
            match element.by:
                case "ID":
                    return self.__config.driver.find_element(By.ID, element.value)
                case "XPATH":
                    return self.__config.driver.find_element(By.XPATH, element.value)
                case "LINK_TEXT":
                    return self.__config.driver.find_element(By.LINK_TEXT, element.value)
                case "PARTIAL_LINK_TEXT":
                    return self.__config.driver.find_element(By.PARTIAL_LINK_TEXT, element.value)
                case "NAME":
                    return self.__config.driver.find_element(By.NAME, element.value)
                case "TAG_NAME":
                    return self.__config.driver.find_element(By.TAG_NAME, element.value)
                case "CLASS_NAME":
                    return self.__config.driver.find_element(By.CLASS_NAME, element.value)
                case "CSS_SELECTOR":
                    return self.__config.driver.find_element(By.CSS_SELECTOR, element.value)
                case _:
                    self.__config.log.warning("Selector not supported !!!")
                    return None
        except NoSuchElementException as err:
            raise err
