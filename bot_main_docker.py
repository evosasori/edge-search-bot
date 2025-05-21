from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
import time
import sys

def create_driver():
    """Create and return a WebDriver instance"""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    try:
        # Use Remote WebDriver from Docker container
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )
        
        # Wait for the driver to be ready
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        
        return driver
    except Exception as e:
        print(f"Failed to create driver: {e}")
        return None

def perform_search(driver, query):
    """Perform a single search on Bing"""
    try:
        print(f"Searching for: {query}")
        
        # Navigate to Bing
        driver.get("https://www.bing.com")
        
        # Wait for the search box to be present and clickable
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
        
        # Clear any existing text and enter the search query
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for search results to load
        wait.until(EC.presence_of_element_located((By.ID, "b_results")))
        
        print(f"Search completed for: {query}")
        time.sleep(5)  # Wait between searches
        
        return True
        
    except TimeoutException:
        print(f"Timeout occurred while searching for: {query}")
        return False
    except Exception as e:
        print(f"Error during search for '{query}': {e}")
        return False

def main():
    """Main function to run the search bot"""
    # Create driver
    driver = create_driver()
    if not driver:
        print("Failed to create WebDriver. Make sure Docker Selenium is running.")
        sys.exit(1)
    
    try:
        # Check if driver is working
        driver.get("https://www.bing.com")
        print("Successfully connected to Bing")
        
        # Read searches from file
        try:
            with open("./random_searches.txt", "r", encoding="utf-8") as file:
                searches = file.readlines()
        except FileNotFoundError:
            print("random_searches.txt file not found!")
            return
        except Exception as e:
            print(f"Error reading file: {e}")
            return
        
        # Filter out empty lines
        searches = [search.strip() for search in searches if search.strip()]
        
        if not searches:
            print("No search queries found in the file!")
            return
        
        print(f"Found {len(searches)} search queries")
        
        # Initial delay
        print("Waiting 15 seconds before starting searches...")
        time.sleep(15)
        
        # Perform searches
        successful_searches = 0
        for index, query in enumerate(searches, 1):
            print(f"Processing search {index}/{len(searches)}")
            
            try:
                # Check if window is still available
                driver.current_url
                
                if perform_search(driver, query):
                    successful_searches += 1
                else:
                    print(f"Failed to search for: {query}")
                    
            except NoSuchWindowException:
                print("Browser window was closed. Recreating driver...")
                driver.quit()
                driver = create_driver()
                if not driver:
                    print("Failed to recreate driver. Stopping.")
                    break
                
                # Retry the search with new driver
                if perform_search(driver, query):
                    successful_searches += 1
                    
            except Exception as e:
                print(f"Unexpected error: {e}")
                break
        
        print(f"Completed {successful_searches}/{len(searches)} searches successfully")
        
    except KeyboardInterrupt:
        print("\nSearch bot interrupted by user")
    except Exception as e:
        print(f"Unexpected error in main: {e}")
    finally:
        # Always clean up
        try:
            driver.quit()
            print("Driver closed successfully")
        except:
            pass

if __name__ == "__main__":
    main()