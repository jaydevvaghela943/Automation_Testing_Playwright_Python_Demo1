from pages.login_page import LoginPage


def test_valid_login(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "admin@test.com",
        "password123"
    )

    assert login.is_dashboard_visible()