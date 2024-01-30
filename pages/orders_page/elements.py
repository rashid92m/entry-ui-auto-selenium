from core.form_element import FormElement


class OrdersPageEle:
    orders_table = FormElement("XPATH", '//table[@class="woocommerce-MyAccount-orders shop_table shop_table_responsive my_account_orders account-orders-table"]', "Order number")
    order_number = FormElement("XPATH", "//tr[@class='order'][1]", "first Order number")
