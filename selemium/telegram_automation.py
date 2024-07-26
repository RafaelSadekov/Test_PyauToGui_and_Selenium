from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Укажите путь к вашему WebDriver
driver_path = 'C:\\chromedriver\\chromedriver.exe'  # Убедитесь, что указали правильный путь к chromedriver.exe

# Создайте объект Service
service = Service(executable_path=driver_path)

# Инициализация драйвера с использованием объекта Service
driver = webdriver.Chrome(service=service)

# Откройте веб-версию Telegram
driver.get("https://web.telegram.org/")

# Явное ожидание, пока страница загрузится и появится кнопка логина по номеру телефона
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Log in by phone Number")]'))
)

# Нажмите кнопку "Log in by phone Number"
login_by_phone_button = driver.find_element(By.XPATH, '//button[contains(text(), "Log in by phone Number")]')
login_by_phone_button.click()

# Ожидание поля ввода телефона
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, 'sign-in-phone-number'))
)

# Введите номер телефона
phone_number = '+79266565746'  # Ваш номер телефона
phone_input = driver.find_element(By.ID, 'sign-in-phone-number')
phone_input.clear()  # Очистите поле перед вводом номера
phone_input.send_keys(phone_number)
phone_input.send_keys(Keys.ENTER)

# Ожидание ввода кода
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.NAME, 'phone_code'))
)

# Введите код, полученный на телефон
phone_code = input("Введите код, полученный на телефон: ")
code_input = driver.find_element(By.NAME, 'phone_code')
code_input.send_keys(phone_code)
code_input.send_keys(Keys.ENTER)

# Ожидание ввода пароля, если он требуется
try:
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'sign-in-password'))
    )
    password = ''  # Замените на ваш пароль, если он требуется
    password_input = driver.find_element(By.ID, 'sign-in-password')
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
except:
    print("Пароль не требуется")

# Ожидание загрузки главной страницы и поля поиска
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search"]'))
)

# Найдите поле поиска и введите текст "Blum"
search_field = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
search_field.send_keys('Blum')
search_field.send_keys(Keys.ENTER)

# Ожидание загрузки результатов поиска
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//span[@title="Blum"]'))
)

# Найдите и кликните на канал "Blum" из результатов поиска
channel = driver.find_element(By.XPATH, '//span[@title="Blum"]')
channel.click()

# Ожидание открытия канала и появления кнопки "launch blum"
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "launch blum")]'))
)

# Найдите и кликните на кнопку "launch blum"
launch_button = driver.find_element(By.XPATH, '//button[contains(text(), "launch blum")]')
launch_button.click()

# Закройте браузер после выполнения действий
time.sleep(5)
driver.quit()
