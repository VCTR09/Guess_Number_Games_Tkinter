from tkinter import *
from tkinter import messagebox
from random import randint


# Окно приложения
root = Tk()
root.geometry("500x300")
root.title("Игра Угадай Число")
root.configure(bg="ivory")


# Функция Генератор Чисел
def GenerateNumberFunc():
    global Number
    # Создать число
    Number = randint(1, 15)

    # MessageBox показывает, что случайное число было сгенерировано
    messagebox.showinfo("A number was generated", "Число было сгенерировано! Пожалуйста, угадайте Число")


# Функция Отгадки Числа
def GuessNumberFunc():
    global Number
    # Получает Значение из поля Answer Entry
    UserResponse = AnswerEntry.get()

    # Конвертирует Значение из поля Answer Entry в Number
    UserResponse = int(UserResponse)

    # Проверяет если User Response был больше, меньше, или равен правильному числу
    if UserResponse > Number:
        ResultLabel.config(text="Неправильно! Загаданное число меньше", fg='Red')
    elif UserResponse < Number:
        ResultLabel.config(text="Неправильно! Загаданное число больше", fg='Red')
    else:
        ResultLabel.config(text="Вы отгадали! Загаданное число {}".format(Number), fg="Green")
        AnswerEntry.delete(0, "end")


# Заголовок
Title = Label(root, text="Игра Угадай Число", font=("Arial",30))
Title.pack()


# Main Frame
MainFrame = Frame(root)
MainFrame.pack(pady=40)
MainFrame.configure(bg="ivory")


# Метка Угадайте Число
GuessNumLabel = Label(MainFrame, text="Угадайте число от 1 до 15:", font=("Arial",20))
GuessNumLabel.pack()


# Текстовое поле Ответ
AnswerEntry = Entry(MainFrame, font=("Arial",16))
AnswerEntry.pack(pady=10)


# Кнопка Генератор Чисел
GenerateNumberBtn = Button(MainFrame, text="Сгенерировать число", width=16, font=("Arial",16), bg='orange', fg='Dodgerblue', command=GenerateNumberFunc)
GenerateNumberBtn.pack()


# Кнопка Угадать
GuessBtn = Button(MainFrame, text="Угадать", width=16, font=("Arial",16), bg='orange', fg='#15e650', command=GuessNumberFunc)
GuessBtn.pack(pady=5)


# Метка Результат
ResultLabel = Label(MainFrame, text="", font=("Arial", 16))
ResultLabel.pack()


# Mainloop
root.mainloop()