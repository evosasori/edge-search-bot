from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path ke Microsoft Edge WebDriver
# driver_path = "C:/Users/tyradi/Documents/Odoo16/server/custom/cendana/simrs/v16_simrs_mujirahayu/test/msedgedriver.exe" # Untuk Windows
driver_path = "./edgedriver_linux64/msedgedriver" # Untuk Linux


# Setup Service untuk Microsoft Edge WebDriver
service = Service(driver_path)

# Setup WebDriver untuk Microsoft Edge
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")  # Membuka browser dalam mode full screen
driver = webdriver.Edge(service=service, options=options)

# Baca pencarian dari file
with open("./random_searches.txt", "r") as file:
    searches = file.readlines()
index = 0
# Lakukan pencarian di Microsoft Edge
for search in searches:
    index += 1
    query = search.strip()
    if index == 1:
        time.sleep(15)
    if query:
        driver.get("https://www.bing.com")  # Buka Bing
        search_box = driver.find_element("name", "q")  # Temukan kotak pencarian
        search_box.send_keys(query)  # Masukkan pencarian
        search_box.send_keys(Keys.RETURN)  # Tekan Enter
        time.sleep(5)  # Tunggu beberapa detik sebelum pencarian berikutnya

# Tutup browser setelah selesai
driver.quit()
