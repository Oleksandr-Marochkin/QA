from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page import SignInTriolan
from modules.ui.page_objects.sign_in_page import SignInAmazon
from modules.ui.page_objects.sign_in_page import SignInRozetka
from modules.ui.page_objects.sign_in_page import SignInBrides
import pytest
import time


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()

    sign_in_page.go_to()
    sign_in_page.try_login("page_object@gmail.com", "wrong password")
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    sign_in_page.close()


@pytest.mark.ui_Trio
def test_check_triolan_login():
    sign_in_page = SignInTriolan()

    sign_in_page.go_to()
    sign_in_page.try_login("test", "test")
    assert sign_in_page.check_title("Triolan - Особистий кабінет")
    time.sleep(3)
    sign_in_page.close()


@pytest.mark.ui_Amazon
def test_check_incorrect_amazon_login():
    sign_in_page = SignInAmazon()

    sign_in_page.go_to()
    sign_in_page.try_login()
    # assert sign_in_page.check_title("Amazon Sign-In")
    # time.sleep(3)
    # sign_in_page.close()


@pytest.mark.ui_Roz
def test_check_incorrect_rozetka_login():
    sign_in_page = SignInRozetka()

    sign_in_page.go_to()
    sign_in_page.try_login("test@test.com", "password")
    assert sign_in_page.check_title(
        "Інтернет-магазин ROZETKA™: офіційний сайт найпопулярнішого онлайн-гіпермаркету в Україні"
    )
    time.sleep(3)
    sign_in_page.close()


@pytest.mark.ui_Army
def test_check_incorrect_rozetka_login():
    sign_in_page = SignInBrides()

    sign_in_page.go_to()
    sign_in_page.try_login("test@test.com", "password")
    assert sign_in_page.check_title("Army of Brides :: register at men online catalog")
    # time.sleep(3)
