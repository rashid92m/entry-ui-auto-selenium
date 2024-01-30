from core.form_element import FormElement


class LoginPageEle:
    input_username = FormElement("XPATH", "//.[@id='username']", "Username textbox")
    input_password = FormElement("XPATH", "//.[@id='password']", "Password textbox")
    login_button = FormElement("XPATH", "//.[@name='login']", "login button")
