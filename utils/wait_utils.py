def wait_for_loader(page):

    page.locator(
        ".loading"
    ).wait_for(
        state="hidden"
    )