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


class SignInTriolan(BasePage):
    URL = "https://triolan.name/LP.aspx"

    def go_to(self):
        self.driver.get(SignInTriolan.URL)

    def try_login(self, number, password):
        radio1_elem = self.driver.find_element(By.ID, "rb1")
        radio1_elem.click()
        number_elem = self.driver.find_element(By.NAME, "login2$tbAgreement")
        number_elem.send_keys(number)
        pass_elem = self.driver.find_element(By.NAME, "login2$tbPassword")
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.NAME, "login2$btnLoginByAgr")
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class SignInAmazon(BasePage):
    URL = "https://www.amazon.com/"

    def go_to(self):
        self.driver.get(SignInAmazon.URL)

    def try_login(self):
        email_elem = self.driver.find_element(By.ID, "nav-link-accountList")
        email_elem.click()

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
