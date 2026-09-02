import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        slow_mo=1000
        context = browser.new_context()
        page=context.new_page()
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

