import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    #Fixture untuk menginisialisasi dan menutup WebDriver Chrome
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    yield driver
    driver.quit()

def login(driver, username, password):
    #Fungsi untuk melakukan login
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "btn-login").click()

def test_login_success(driver):
    #Tes login berhasil
    login(driver, "John Doe", "ThisIsNotAPassword")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Login gagal: URL tidak sesuai setelah login berhasil"

def test_login_invalid_email(driver):
    #Tes login dengan email yang salah
    login(driver, "invalid_email", "ThisIsNotAPassword")
    error_message = driver.find_element(By.CLASS_NAME, "lead.text-danger").text
    assert error_message == "Login failed! Please ensure the username and password are valid.", "Error message tidak sesuai untuk email yang salah"

def test_login_invalid_password(driver):
    #Tes login dengan password yang salah
    login(driver, "John Doe", "invalid_password")
    error_message = driver.find_element(By.CLASS_NAME, "lead.text-danger").text
    assert error_message == "Login failed! Please ensure the username and password are valid.", "Error message tidak sesuai untuk password yang salah"
