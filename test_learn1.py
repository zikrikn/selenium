from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

@pytest.fixture()
def driver():
    # Inisialisasi WebDriver Chrome
    driver = webdriver.Chrome()
    # Buka Google Search
    driver.get("http://www.google.com")
    yield driver
    driver.quit()

def test_google(driver):
    # Cari 'Zikri Kholifah Nur'
    driver.find_element(By.NAME, "q").send_keys("Zikri Kholifah Nur" + Keys.ENTER)
    
    # Menggunakan XPath untuk mencari elemen dengan teks tertentu
    result = driver.find_element(By.XPATH, "//h3[contains(text(),'Zikri Kholifah Nur - Subang, Jawa Barat, Indonesia')]")
    
    assert result is not None, "Hasil pencarian 'Zikri Kholifah Nur - Subang' tidak ditemukan."
    
    assert "Zikri Kholifah Nur" in driver.title, "Judul halaman tidak sesuai."
    
    time.sleep(5)  # Waktu tunggu sebelum menutup browser