from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PROXY = ["213.157.243.196:5678", "122.136.212.132:53281",
         "185.162.231.178:80", "70.185.95.177:39593"]
i = random.randint(0, 3)

chrome_options = Options()
chrome_options.add_experimental_option(
    "detach", True)
chrome_options.add_argument('--disk-cache-dir=/path/to/cache')
# chrome_options.add_argument('--proxy-server=%s' % PROXY[i])


# Get IP

def get_ip():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://api.ipify.org/')
    ip = driver.find_element(By.TAG_NAME, "body").text
    driver.close()
    return ip


start_time_wait = 30


# Login Twitter

def login_twitter():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://x.com/i/flow/login")
    wait = WebDriverWait(driver, start_time_wait)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@name='text']")))
    input_email = driver.find_element(By.XPATH, "//input[@name='text']")
    input_email.send_keys("vinningrazors329@gmail.com")
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@role='button']")))
    next_btn = driver.find_elements(By.XPATH, "//button[@role='button']")
    for i in next_btn:
        try:
            print(i.text)
            if i.text == "Next":
                i.click()
                break
        except Exception:
            continue

    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")))
    input_username = driver.find_element(
        By.XPATH, "//input[@data-testid='ocfEnterTextTextInput']")
    input_username.send_keys("@Winner949124"+Keys.RETURN)

    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='password']")))
    password = driver.find_element(By.XPATH, "//input[@type='password']")
    password.send_keys("@VinningRazors" + Keys.RETURN)
    return driver


# Get Trends

def get_trends(driver):
    wait = WebDriverWait(driver, start_time_wait)
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@aria-label='Timeline: Trending now']")))
    trending = driver.find_element(
        By.XPATH, "//div[@aria-label='Timeline: Trending now']")
    trend = trending.find_elements(By.TAG_NAME, "span")

    new_trend = set()
    for i in trend:
        new_trend.add(i.text)

    # Clearing Data

    final_data = [i for i in new_trend if not any(x in i for x in [
        "posts", "Trending in India", "What’s happening", '· Trending', "Show more"])]
    
    driver.close()
    return final_data
