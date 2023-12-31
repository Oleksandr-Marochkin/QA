from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page import TriolanSelectDnipro
from modules.ui.page_objects.sign_in_page import SignInAmazon
from modules.ui.page_objects.sign_in_page import SignInRozetka
from modules.ui.page_objects.sign_in_page import SignInBrides
from modules.ui.page_objects.sign_in_page import SearchInBridesById
from modules.ui.page_objects.sign_in_page import SearchOrderNP
import pytest
import time


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()

    sign_in_page.go_to()
    sign_in_page.select_dnipro("page_object@gmail.com", "wrong password")
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    sign_in_page.close()


@pytest.mark.ui_Trio
def test_triolan_select_dnipro():
    sign_in_page = TriolanSelectDnipro()

    sign_in_page.go_to()
    sign_in_page.select_dnipro()
    assert sign_in_page.check_url("https://triolan.com/index.aspx?lng=uk&reg=dn")
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
    # time.sleep(3)
    sign_in_page.close()


@pytest.mark.ui_Army
def test_check_incorrect_rozetka_login():
    sign_in_page = SignInBrides()

    sign_in_page.go_to()
    sign_in_page.try_login("test@test.com", "password")
    assert sign_in_page.check_title("Army of Brides :: register at men online catalog")
    # time.sleep(3)


@pytest.mark.ui_Army
def test_check_search_by_id():
    sign_in_page = SearchInBridesById()

    sign_in_page.go_to()
    sign_in_page.try_search("test")
    assert sign_in_page.check_title(
        "Search Engine :: find your bride at Army Of Brides"
    )
    # time.sleep(3)


@pytest.mark.ui_NP
def test_check_order_by_number():
    sign_in_page = SearchOrderNP()

    sign_in_page.go_to()
    sign_in_page.try_search("1111111111111")
    assert sign_in_page.check_title("Трекінг посилки | Nova Global")
    # time.sleep(3)
