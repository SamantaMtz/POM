import os
from dotenv import load_dotenv
from screens.HomeScreen import HomeScreen
from screens.LoginScreen import LoginScreen

load_dotenv("..\\utils\\.env")


def test_exitoso(driver):  # este driver sale del fixture
    username = os.getenv("USERNAME_SAUCE")
    password = os.getenv("PASSWORD_SAUCE")
    print("username", username)
    # username = "bob@example.com"
    # password = 10203040
    home_screen = HomeScreen(driver)
    home_screen.ir_a_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert home_screen.elemento_es_mostrado(*home_screen.lbl_products)


def test_usuario_incorrecto(driver):
    username = os.getenv("USERNAME_SAUCE_USR_INC")
    password = os.getenv("PASSWORD_SAUCE_USR_INC")
    home_screen = HomeScreen(driver)
    home_screen.ir_a_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_msj_error)


def test_password_incorrecto(driver):
    username = "bob@example.com"
    password = "passincorrecto"
    home_screen = HomeScreen(driver)
    home_screen.ir_a_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_msj_error)


def test_username_empty(driver):
    username = ""
    password = 10203040
    home_screen = HomeScreen(driver)
    home_screen.ir_a_login()
    login_screen = LoginScreen(driver)
    login_screen.login(username, password)
    assert login_screen.elemento_es_mostrado(*login_screen.lbl_msj_usrname_req)
