import pyautogui
import time
import subprocess
import pytesseract
from PIL import Image

# Укажите путь к исполняемому файлу tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Функция для открытия приложения Telegram
def open_telegram():
    subprocess.Popen([r"C:\Users\User\AppData\Roaming\Telegram Desktop\Telegram.exe"])

# Функция для ожидания изменения цвета пикселя
def wait_for_pixel_color_change(x, y, inactive_color, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        current_color = pyautogui.pixel(x, y)
        if current_color != inactive_color:
            return True
        time.sleep(0.5)
    return False

# Функция для ожидания окончания таймера на кнопке
def wait_for_timer_to_end(region, timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        screenshot = pyautogui.screenshot(region=region)
        text = pytesseract.image_to_string(screenshot)
        print(f"Detected text: {text.strip()}")
        if not any(char.isdigit() for char in text):  # Предполагаем, что цифры отображают таймер
            return True
        time.sleep(1)
    return False

# Открываем Telegram
open_telegram()

# Ждем, пока приложение загрузится
time.sleep(10)

# Определите координаты элементов
password_field_coords = (851, 399)
submit_button_coords = (947, 480)
tab_coords = (27, 989)
chat_coords = (256, 101)
launch_blum_coords = (804, 920)
submit_button_farm_coords = (849, 723)
submit_button_farm_region = (849, 723, 200, 50)  # Область для скриншота (x, y, width, height)

# Ожидаемый цвет кнопки submit_button_farm
inactive_color_submit_button_farm = (94, 94, 94)  # Замените на реальный цвет пикселя неактивной кнопки

# # Вводим пароль
# password = ""
# pyautogui.click(password_field_coords)
# pyautogui.typewrite(password, interval=0.1)

# # Нажимаем кнопку "Submit"
# pyautogui.click(submit_button_coords)
# time.sleep(3)
# print("Пароль введен и нажата кнопка Submit")

# Нажимаем на вкладку
pyautogui.click(tab_coords)
time.sleep(4)

# Нажимаем на чат
pyautogui.click(chat_coords)
time.sleep(3)

print("Навигация к чату завершена")

# Нажимаем на launch_blum
pyautogui.click(launch_blum_coords)
time.sleep(2)

# Проверка изменения цвета кнопки submit_button_farm и нажатие на нее
if wait_for_pixel_color_change(submit_button_farm_coords[0], submit_button_farm_coords[1], inactive_color_submit_button_farm):
    print("Цвет кнопки 'Farm' изменился")
    # Ждем окончания таймера на кнопке
    if wait_for_timer_to_end(submit_button_farm_region):
        pyautogui.click(submit_button_farm_coords)
        print("Кнопка 'Farm' нажата после окончания таймера")
    else:
        print("Таймер на кнопке 'Farm' не закончился в течение заданного времени")
else:
    print("Цвет кнопки 'Farm' не изменился в течение заданного времени")
    exit(1)

time.sleep(2)
