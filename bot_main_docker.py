from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

# Setup opsi Edge
options = Options()
options.add_argument("--start-maximized")

# Gunakan Remote WebDriver dari Docker container
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

# Baca pencarian dari file
with open("./random_searches.txt", "r") as file:
    searches = file.readlines()

index = 0
for search in searches:
    index += 1
    query = search.strip()
    if index == 1:
        time.sleep(15)  # Delay awal
    if query:
        driver.get("https://www.bing.com")  # Buka Bing
        search_box = driver.find_element(By.NAME, "q")  # Gunakan By.NAME, bukan string literal
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

driver.quit()
