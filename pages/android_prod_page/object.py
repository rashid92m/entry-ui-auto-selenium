from core.data_classes import Config
from core.base_page import BaseScreen
from pages.android_prod_page.elements import AndroidProdPageEle
from assertpy import assert_that


class AndroidProdPageObj(BaseScreen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = "shop"
        self.android_prod_page_ele = AndroidProdPageEle

    # Page actions

    # Page assertions

    def verify_page_url(self):
        self.log.info("Verify the page url")
        url = self.driver.current_url
        assert_that(url).contains("product-category/android")
