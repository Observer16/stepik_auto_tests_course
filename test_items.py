link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_button_submit(browser):
    browser.get(link)
    