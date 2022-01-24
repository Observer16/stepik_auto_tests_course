from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_submit(browser):
    browser.get(link)
    