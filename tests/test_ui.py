from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


def test_title_is_correct():
    driver = webdriver.Chrome()
    driver.get(url='https://pwdg.herokuapp.com/')
    assert "Password Generator" in driver.title
    driver.quit()


def test_navbar():
    driver = webdriver.Chrome()
    driver.get(url='https://pwdg.herokuapp.com/')
    time.sleep(3)
    driver.find_element(By.ID, "navbarNav")
    assert 'Password Generator'
    assert 'Author'
    driver.quit()

def test_link_to_github():
    driver = webdriver.Chrome()
    driver.get(url='https://pwdg.herokuapp.com/')
    github_url = 'https://github.com/gmachadosimoes'
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li/a").click()
    time.sleep(3)
    driver.current_url
    assert driver.current_url == github_url
    driver.quit()

    