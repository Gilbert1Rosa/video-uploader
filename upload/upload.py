from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    element = driver.find_element(By.NAME, "q")
    element.clear()
    element.send_keys("pycon")
    element.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


def login_to_tiktok():
    """
        Scrapping to login to tiktok.
    """
    driver = webdriver.Firefox()
    driver.get("https://www.tiktok.com/")
    login_button = driver.find_element(By.ID, "header-login-button")
    login_button.click()
    sleep(2)
    login_google_button = None
    elements = driver.find_elements(By.CLASS_NAME, "tiktok-1j4ihbo-DivBoxContainer")
    for element in elements:
        if element.text == "Continuar con Google":
            login_google_button = element
            break
    login_google_button.click()
    sleep(200)
    driver.close()
    """
        When emergent window, asking for google login opens up,
        put login credentials.
    """


def upload_video():
    """
        Scrapping to load video data to tiktok.
    """


def comment():
    """
        Make default comment.
    """


login_to_tiktok()

