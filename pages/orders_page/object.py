from core.data_classes import Config
from core.base_page import BaseScreen
from pages.orders_page.elements import OrdersPageEle
from assertpy import assert_that
from selenium.common.exceptions import NoSuchElementException



class OrdersPageObj(BaseScreen):
    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = "my-account/orders/"
        self.orders_page_ele = OrdersPageEle


    # Page actions

    def open(self):
        self.log.info(f"Open the {self.url} page")
        self.driver.get(self.url)


    # Page assertions

    def verify_page_URL(self):
        self.log.info("Verify the page URL")
        current_url = self.driver.current_url
        assert_that(current_url).contains("/my-account/orders/")

    def verify_orders_list_is_displayed(self):
        self.log.info("Verify the orders table and order list is displayed")
        assert self.se_helper.get_element(self.OrdersPageEle.orders_table).is_displayed() and self.se_helper.get_element(self.OrdersPageEle.order_number).is_displayed()



