from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from config.config import BASE_URL


class LoginPage(BasePage):

    def open(self):
        self.page.goto(f"{BASE_URL}/login")

    def login(self, email, password):

        self.fill(
            LoginLocators.EMAIL,
            email
        )

        self.fill(
            LoginLocators.PASSWORD,
            password
        )

        self.click(
            LoginLocators.LOGIN_BUTTON
        )

    def is_dashboard_visible(self):

        return self.is_visible(
            LoginLocators.DASHBOARD
        )