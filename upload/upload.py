import copy
from time import sleep

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.options import FirefoxProfile

await_time_in_seconds = 2


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


# Not necesary can start session on tiktok in firefox profile
def login_to_tiktok():
    """
        Scrapping to login to tiktok.
    """
    # Create custom firefox profile for selenium
    profile_path = "C:\\Users\\Gilbert\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\qp71cu4y.Selenium"
    options = FirefoxOptions()
    options.profile = FirefoxProfile(profile_path)
    driver = Firefox(options)
    driver.get("https://www.tiktok.com/")
    login_button = driver.find_element(By.ID, "header-login-button")
    login_button.click()
    sleep(await_time_in_seconds)
    login_google_button = None
    elements = driver.find_elements(By.CLASS_NAME, "tiktok-1j4ihbo-DivBoxContainer")
    for element in elements:
        if element.text == "Continue with Google":
            login_google_button = element
            break
    login_google_button.click()
    sleep(await_time_in_seconds)
    handles = copy.copy(driver.window_handles)
    main_window = driver.current_window_handle
    handles.remove(main_window)
    driver.switch_to.window(handles[0])
    account_button = driver.find_element(By.CLASS_NAME, 'd2laFc')
    account_button.click()
    driver.close()


def upload_video(caption, video_path):
    """
        Scrapping to load video data to tiktok.
    """
    profile_path = "C:\\Users\\Gilbert\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\qp71cu4y.Selenium"
    options = FirefoxOptions()
    options.profile = FirefoxProfile(profile_path)
    driver = Firefox(options)
    try:
        driver.get("https://www.tiktok.com/")
        upload_button = driver.find_element(By.CLASS_NAME, "tiktok-1qup28j-DivUpload")
        upload_button.click()
        sleep(5)
        form_frame = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(form_frame)
        caption_textbox = driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")
        caption_textbox.click()
        caption_textbox.send_keys(caption)
        select_file_button = driver.find_element(By.CLASS_NAME, "css-1z070dx")
        select_file_button.click()
        upload_file_browser = driver.find_element(By.ID, "uploadFile")
        upload_file_browser.send_keys(video_path)
    finally:
        sleep(2)
        driver.close()


def comment():
    """
        Make default comment.
    """


upload_video("Some title", "")
