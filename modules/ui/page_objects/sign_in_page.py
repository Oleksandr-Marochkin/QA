from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.NAME, "commit")
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class TriolanSelectDnipro(BasePage):
    URL = "https://triolan.com/index.aspx?lng=uk&reg=kiev"

    def go_to(self):
        self.driver.get(TriolanSelectDnipro.URL)

    def select_dnipro(self):
        list_elem = self.driver.find_element(
            By.ID, "select2-repRegionsHolder-container"
        )
        list_elem.click()

        list_dnipro = self.driver.find_element(
            By.XPATH, "/html/body/span/span/span[2]/ul/li[4]"
        )
        list_dnipro.click()

    def check_url(self, expected_url):
        return self.driver.current_url == expected_url


class SignInAmazon(BasePage):
    URL = "https://www.amazon.com/"

    def go_to(self):
        self.driver.get(SignInAmazon.URL)

    def try_login(self):
        login_elem = self.driver.find_element(By.ID, "nav-cart")
        login_elem.click()

        # cont_elem = self.driver.find_element(By.ID, "continue")
        # cont_elem.click()

        # pass_elem = self.driver.find_element(By.ID, "ap_password")
        # pass_elem.send_keys(password)

        # sign_btn = self.driver.find_element(By.ID, "signInSubmit")
        # sign_btn.click()

    # def check_title(self, expected_title):
    # return self.driver.title == expected_title


class SignInRozetka(BasePage):
    URL = "https://rozetka.com.ua/ua/"

    def go_to(self):
        self.driver.get(SignInRozetka.URL)

    def try_login(self, email, password):
        login_btn = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user/button",
        )
        login_btn.click()

        email_elem = self.driver.find_element(By.ID, "auth_email")
        email_elem.send_keys(email)

        pass_elem = self.driver.find_element(By.ID, "auth_pass")
        pass_elem.send_keys(password)

        btn_elem = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[1]",
        )
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class SignInBrides(BasePage):
    URL = "https://www.army-of-brides.com/login.html"

    def go_to(self):
        self.driver.get(SignInBrides.URL)

    def try_login(self, email, password):
        email_elem = self.driver.find_element(By.NAME, "login")
        email_elem.send_keys(email)

        pass_elem = self.driver.find_element(By.NAME, "password")
        pass_elem.send_keys(password)

        btn_elem = self.driver.find_element(
            By.XPATH, '//*[@id="one"]/ul/li/form[2]/div/p[3]/input'
        )
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class SearchInBridesById(BasePage):
    URL = "https://www.army-of-brides.com"

    def go_to(self):
        self.driver.get(SearchInBridesById.URL)

    def try_search(self, id):
        id_elem = self.driver.find_element(By.XPATH, '//*[@id="new"]/form/div/input[1]')
        id_elem.send_keys(id)

        btn_elem = self.driver.find_element(
            By.XPATH, '//*[@id="new"]/form/div/input[3]'
        )
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class SearchOrderNP(BasePage):
    URL = "https://tracking.novaposhta.ua/#/uk/"

    def go_to(self):
        self.driver.get(SearchOrderNP.URL)

    def try_search(self, number):
        id_elem = self.driver.find_element(By.ID, "en")
        id_elem.send_keys(number)

        btn_elem = self.driver.find_element(
            By.ID, "np-number-input-desktop-btn-search-en"
        )
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
