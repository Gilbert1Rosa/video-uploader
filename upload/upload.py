import copy
from time import sleep

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.options import FirefoxProfile

import pyautogui

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


def upload_video(profile_path, caption, video_path):
    """
        Scrapping to load video data to tiktok.
    """
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
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.typewrite(video_path)
        pyautogui.press('enter')
    finally:
        sleep(5)
        driver.close()


def comment():
    """
        Make default comment.
    """