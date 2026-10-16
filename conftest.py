import pytest
from playwright.sync_api import sync_playwright

# Add command-line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests: chromium, firefox, or webkit"
    )
    parser.addoption(
        "--headed",
        action="store_true",
        help="Run the browser with a visible window"
    )


@pytest.fixture(scope="module")
def page(request):

    browser_name = request.config.getoption("--browser")
    headless = not request.config.getoption("--headed")

    with sync_playwright() as p:

        if browser_name == "chromium":
            browser = p.chromium.launch(headless=headless)

        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=headless)

        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=headless)

        else:
            raise ValueError(
                f"Unsupported browser: {browser_name}"
            )

        context = browser.new_context()
        page = context.new_page()

        yield page

        page.close()
        context.close()
        browser.close()

@pytest.fixture(autouse=True)
def before_after():
    print("\n========== Test Started ==========")

    yield

    print("\n========== Test Finished ==========")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)
