# pip install mouse
# pip install keyboard

import tkinter as tk
from tkinter import messagebox
# Модулі для імітації миші та відстеження клавіатури
import mouse
import keyboard
# Модуль для затримки (хоча в Tkinter краще використовувати root.after)
import time 

# =================================================================
# Змінні стану програми (глобальні, щоб їх можна було змінити у функціях)
# =================================================================
running = False  # Зберігає стан: True, якщо клікер активний
delay = 0        # Зберігає затримку між кліками у мілісекундах (мс)

# =================================================================
# Функції-обробники подій
# =================================================================

def start_clicker():
    """Запускає процес автоклікання, отримує швидкість з поля вводу."""
    global running, delay

    try:
        # Отримуємо введене значення та перетворюємо його на ціле число
        clicks_per_second = int(entry.get())

        if clicks_per_second <= 0:
            messagebox.showerror("Помилка", "Швидкість має бути більше 0!")
            return

        # Розрахунок затримки: 1 секунда (1000 мс) ділимо на кількість кліків
        delay = int(1000 / clicks_per_second)

        messagebox.showinfo("Auto Clicker", "Auto Clicker розпочато! Натисніть 'ESC', щоб зупинити.")
        running = True

        # Запуск циклічного клікання через root.after
        schedule_click()

    except ValueError:
        # Обробка випадку, коли користувач ввів не число або залишив поле порожнім
        messagebox.showerror("Помилка вводу", "Будь ласка, введіть коректне число кліків на секунду.")


def schedule_click():
    """Виконує один клік і планує наступний, якщо клікер активний."""
    if running:
        mouse.click()  # Симуляція лівого клацання миші

        # Плануємо повторний виклик цієї функції через 'delay' мілісекунд
        root.after(delay, schedule_click)


def exit_app():
    """Зупиняє клікер та закриває вікно програми."""
    global running

    if running:
        # Змінюємо стан на False, щоб зупинити цикл schedule_click
        running = False 

    messagebox.showinfo("Auto Clicker", "Auto Clicker зупинено.")
    root.destroy() # Закриття вікна Tkinter


def show_info(event):
    """Відображає інформаційне повідомлення (прив'язано до клавіші 'i')."""
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

# =================================================================
# Створення графічного інтерфейсу (GUI)
# =================================================================

# Ініціалізація головного вікна
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x220")
root.resizable(False, False) # Заборонити змінювати розмір вікна
root.configure(bg="#e0f7fa") # Світло-блакитний фон (колір Light Cyan)

# Прив'язка події: натискання клавіші 'i' викликає функцію show_info
root.bind('i', show_info) 

# Дизайн вікна
# Заголовок
title_label = tk.Label(
    root, 
    text="Auto Clicker", 
    font=("Trebuchet MS", 16, "bold"), 
    bg="#e0f7fa", 
    fg="#00796b" # Темно-бірюзовий
)
title_label.pack(pady=10) 

# Мітка для кількості кліків
label = tk.Label(
    root, 
    text="Кліків на секунду:", 
    font=("Trebuchet MS", 12), 
    bg="#e0f7fa", 
    fg="#00796b"
)
label.pack(pady=5)

# Поле введення для кількості кліків на секунду
entry = tk.Entry(
    root, 
    font=("Arial", 12),
    width=10,
    justify='center' # Вирівнювання тексту по центру
)
entry.pack(pady=5)
entry.insert(0, "10") # Встановлюємо значення за замовчуванням

# Кнопки
# Рамка для групування кнопок
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30)) 

# Кнопка "Почати" (зелена)
start_button = tk.Button(
    button_frame, 
    text="Почати", 
    command=start_clicker, 
    bg="#4caf50", # Зелений
    activebackground="#66bb6a", # Колір при натисканні
    fg="white", 
    font=("Trebuchet MS", 12),
    width=8
)
start_button.grid(row=0, column=0, padx=10) 

# Кнопка "Вийти" (червона)
exit_button = tk.Button(
    button_frame, 
    text="Вийти", 
    command=exit_app, 
    bg="#f44336", # Червоний
    activebackground="#ef5350", # Колір при натисканні
    fg="white", 
    font=("Trebuchet MS", 12),
    width=8
)
exit_button.grid(row=0, column=1, padx=10) 

# =================================================================
# Налаштування гарячих клавіш та виходу
# =================================================================

# Додати гарячу клавішу 'ESC' для негайного виходу/зупинки клікера
keyboard.add_hotkey('esc', exit_app)

# Обробка закриття вікна (кнопка 'X') також викликає exit_app
root.protocol("WM_DELETE_WINDOW", exit_app) 

# Запуск головного циклу Tkinter
root.mainloop()


















































































































