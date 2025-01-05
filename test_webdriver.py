from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path ke Microsoft Edge WebDriver
driver_path = "C:/Users/tyradi/Documents/Odoo16/server/custom/cendana/simrs/v16_simrs_mujirahayu/test/msedgedriver.exe"

# Setup Service untuk Microsoft Edge WebDriver
service = Service(driver_path)

# Setup WebDriver untuk Microsoft Edge
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")  # Membuka browser dalam mode full screen
driver = webdriver.Edge(service=service, options=options)

# Baca pencarian dari file
with open("C:/Users/tyradi/Documents/Odoo16/server/custom/cendana/simrs/v16_simrs_mujirahayu/test/random_searches.txt", "r") as file:
    searches = file.readlines()

# Lakukan pencarian di Microsoft Edge
for search in searches:
    query = search.strip()
    if query:
        driver.get("https://www.bing.com")  # Buka Bing
        search_box = driver.find_element("name", "q")  # Temukan kotak pencarian
        search_box.send_keys(query)  # Masukkan pencarian
        search_box.send_keys(Keys.RETURN)  # Tekan Enter
        time.sleep(2)  # Tunggu beberapa detik sebelum pencarian berikutnya

# Tutup browser setelah selesai
driver.quit()
