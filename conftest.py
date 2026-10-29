import pytest
from playwright.sync_api import sync_playwright
from config.config import HEADLESS


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:
        
        if BROWSER == "chromium":
            browser = p.chromium.launch()

        elif BROWSER == "firefox":
            browser = p.firefox.launch()

        elif BROWSER == "webkit":
            browser = p.webkit.launch()
        )
        
        headless=HEADLESS

        page = browser.new_page()

        yield page

        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs["page"]

        page.screenshot(
            path=f"screenshots/{item.name}.png"
        )

@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=HEADLESS
        )

        context = browser.new_context(
            record_video_dir="videos/"
        )

        page = context.new_page()

        yield page

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs["page"]

        page.screenshot(
            path=f"screenshots/{item.name}.png"
        )