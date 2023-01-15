from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log((12*math.sin(int(x)))))  

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    num = browser.find_element(By.ID, "input_value")
    value = num.text
    y = calc(value)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
     # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()






