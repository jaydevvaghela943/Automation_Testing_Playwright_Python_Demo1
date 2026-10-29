class BasePage:

    def __init__(self, page):
        self.page = page

    def visit(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def type(self, locator, text):
        self.page.locator(locator).type(text)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def wait(self, time):
        self.page.wait_for_timeout(time)

    def screenshot(self, name):
        self.page.screenshot(path=f"screenshots/{name}.png")