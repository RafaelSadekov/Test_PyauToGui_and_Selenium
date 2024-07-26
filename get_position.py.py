import pyautogui

# Определение координат позиции курсора
print("Наведите курсор на нужный элемент и подождите 5 секунд...")
pyautogui.sleep(5)
print(pyautogui.position())

# Получение цвета пикселя под курсором
x, y = pyautogui.position()
color = pyautogui.pixel(x, y)
print(f'Цвет пикселя на ({x}, {y}): {color}')