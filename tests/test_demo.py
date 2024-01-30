from pytest import mark
from core.data_classes import Config
from pages.home_page.object import HomePageObj
from pages.login_page.object import LoginPageObj
from pages.my_account_page.object import MyAccountPageObj
from pages.orders_page.object import OrdersPageObj


username = "student@world.com"
password = "student@world.com"

@mark.demo
def test_view_orders(config: Config):
    config.log.info("Test user view orders on clicking orders link")

    #open the homepage: http://practice.automationtesting.in/
    home_page = HomePageObj(config)
    home_page.open()
    home_page.verify_page_title()

    #3.	Click on My Account Menu to login
    home_page.click_my_account()

    login_page = LoginPageObj(config)
    login_page.verify_page_title()

    #4.	Enter registered username in username textbox
    login_page.enter_username(username=username)

    #5.	Enter password in password textbox
    login_page.enter_password(username=password)

    #6.	Click on login button
    login_page.click_login()

    #7.	User must successfully login to the web page
    my_account_page = MyAccountPageObj(config)
    my_account_page.verify_page_title()

    #8.	Click on Myaccount link
    #9.	Click on Orders link
    my_account_page.click_orders()

    #10. User must view their orders on clicking orders link
    my_orders_page = OrdersPageObj(config)
    my_orders_page.verify_orders_list_is_displayed()



















