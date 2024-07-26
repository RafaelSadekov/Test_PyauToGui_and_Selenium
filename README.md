# Telegram Automation with Selenium and PyAutoGUI

## Описание

Этот проект использует Selenium и PyAutoGUI для автоматизации взаимодействия с веб-версией Telegram и настольной версией Telegram. Скрипты автоматически выполняют следующие действия:

1. Открытие веб-версии Telegram с помощью Selenium.
2. Выполнение входа по номеру телефона, ввод кода и пароля.
3. Поиск и открытие канала "Blum".
4. Нажатие на кнопку "launch blum".
5. Открытие настольной версии Telegram с помощью PyAutoGUI и автоматизация ввода пароля и других действий.

## Требования

- Python 3.x
- Selenium
- PyAutoGUI
- ChromeDriver (совместимый с вашей версией Chrome)

## Установка

1. Установите Python и pip (если еще не установлены).
2. Установите необходимые библиотеки:
   ```bash
   pip install selenium pyautogui
