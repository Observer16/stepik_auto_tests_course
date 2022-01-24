link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_button_submit(self, browser, language):
    browser.get(link)
    browser.find_element_by_css_selector("#add_to_basket_form > button")