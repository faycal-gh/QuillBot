from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def getResult(text, filePATH):
    driver.get('https://quillbot.com/')
    div_elem = driver.find_element(By.ID, "inputText")
    div_elem.send_keys(text)
    driver.find_element(By.XPATH, '//*[@class="MuiGrid-root MuiGrid-item original-text-btns css-1wxaqej"]/div/div/button[1]').click()
    time.sleep(15)
    element = driver.find_element(By.ID, "editable-content-within-article")
    text = element.text
    print(f"==================================================\n{text}")
    with open(filePATH, 'a') as file:
        file.write(text)

chatGPT_PATH = 'C:/Users/terra/Desktop/chatGPT.txt'
quillbot_PATH = 'C:/Users/terra/Desktop/quillbot.txt'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("detach", True)

options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')

PATH = "C:/Users/terra/Desktop/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)

with open(chatGPT_PATH, 'r') as file:
    data = file.read().replace('\n', ' ')
    words = data.split()
    for i in range(0, len(words), 125):
        group = words[i:i+125]
        getResult(' '.join(group), quillbot_PATH)

input("")