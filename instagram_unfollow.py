from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup

# Set up initial configurations and ChromeDriver path
username = "your_username"
password = "your_password"
driver_path = 'path/to/chromedriver'  # Update this path to where you have ChromeDriver installed

# Initialize the WebDriver
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.instagram.com/")

# Wait for the login page to load
time.sleep(5)

# Enter login credentials
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for login to complete
time.sleep(5)

# Navigate to the user's profile page
driver.get(f"https://www.instagram.com/{username}/")
time.sleep(5)

# Click on the 'Following' link to open the list
driver.find_element(By.XPATH, "//a[contains(@href, '/following')]").click()
time.sleep(3)

# Function to scroll down the following list
def scroll_down():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(2, 4))
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Scroll down to load all followings
scroll_down()

# Use BeautifulSoup to extract following list
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
followings = [element.text for element in soup.find_all("a", {"class": "FPmhX"})]

# Function to unfollow a user
def unfollow_user(username):
    driver.get(f"https://www.instagram.com/{username}/")
    time.sleep(2)
    unfollow_button = driver.find_element(By.XPATH, "//button[text()='Following']")
    unfollow_button.click()
    time.sleep(2)
    confirm_button = driver.find_element(By.XPATH, "//button[text()='Unfollow']")
    confirm_button.click()
    time.sleep(random.uniform(2, 5))

# Unfollow a specified number of followings (e.g., first 10 for testing)
for following in followings[:10]:  # Limit to 10 for testing purposes
    unfollow_user(following)

# Close the browser after completing the task
driver.quit()
