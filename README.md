<a id="anchor"></a>

Содержание:
* [Guessing number Game](#game1)
* [Screenshots](#screens1)
* [Guessing number Reverse Game](#game2)
* [Screenshots](#screens2)


<a id="game1"></a>

# Игра в которой Вы отгадываете число, загаданное компьютером


### Полный код программы
** см. файл app2.py
```
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
```

<a id="screens1"></a>
### Скриншоты
* Главный экран
![IMG_1912](https://user-images.githubusercontent.com/97599612/167812257-7bceca54-7ed3-4200-94ab-47dec1f520c9.JPG)

* При нажатии кнопки 'Сгенерировать число' появлятся всплывающее окно
![IMG_1913](https://user-images.githubusercontent.com/97599612/167812265-d392f42d-6bcb-47a3-ab05-8a6e462f22c3.JPG)

* Программа дает подсказки (больше, меньше) при если введеное число не равно загаданному
![IMG_1915](https://user-images.githubusercontent.com/97599612/167812273-f9e0c50a-2c8f-41b0-900e-d8e87f183dcb.JPG)

![IMG_1914](https://user-images.githubusercontent.com/97599612/167812268-e21d7e47-2ae9-4dbe-bd37-86a237da5c1c.JPG)

* Вы отгадали! Загаднное число __
![IMG_1916](https://user-images.githubusercontent.com/97599612/167812033-63d54bcf-1c7f-4bab-9186-33fa936ef0a9.JPG)

___
___

[Вверх](#anchor)

<a id="game2"></a>
# Игра в которой компьютер отгадывает число, загаданное Вами

### Полный код программы
** см. файл app1.py
```
from operator import ge
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint 

window = Tk()
window.geometry("410x125")
window.title("Компьютер угадывает число")


min_number = 1
max_number = 15


def generate_number():
    global number
    list1.delete(0, END)
    number = randint(min_number, max_number)
    list1.insert(END, number)


def give_more():
    try:
        global number, min_number
        min_number = number + 1
        generate_number()
    except ValueError:
        messagebox.showinfo("Лимит попыток исчерпан", "Пожалуйста, начните заново")


def give_less():
    try:
        global number, max_number
        max_number = number - 1
        generate_number()
    except ValueError:
        messagebox.showinfo("Лимит попыток исчерпан", "Пожалуйста, начните заново")


def win():
    global min_number, max_number
    list1.delete(0, END)
    list1.insert(END, "Победа!")
    min_number = 1
    max_number = 15


b1 = Button(window, text='>', command=give_more)
b1.grid(row=0,column=1)

b2 = Button(window, text='<', command=give_less)
b2.grid(row=1,column=1)

b3 = Button(window, text='=', command=win)
b3.grid(row=2,column=1)

b4 = Button(window, text='Старт', command=generate_number)
b4.grid(row=3,column=1)


list1 = Listbox(window, height=6, width=35)
list1.grid(row=0, column=2, rowspan=6, columnspan=2,sticky=(N,W,E,S))
 
sb1 = ttk.Scrollbar(window, orient=VERTICAL, command=list1.yview)
sb1.grid(row=0, column=4, rowspan=6, sticky=(N,S))

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


window.mainloop()
```


<a id="screens2"></a>

### Скриншоты

* Главное окно с кнопками '>', '<', '=' и 'Старт'.
При нажатии на 'Старт' на экран будет выведено число. Если число не равно Вашему, Вы можете воспользоваться кнопками '>' или '<'. Когда компьютер угадает Ваше число, нажмите '='.
можете 
![IMG_1909](https://user-images.githubusercontent.com/97599612/167812206-713409bc-d5ae-4938-91e6-30f51e2dcdec.JPG)

* При возникновении ValueError появится всплывающее окно
![IMG_1911](https://user-images.githubusercontent.com/97599612/167812250-f4365674-3053-4f9e-84b6-0b2b2a917709.JPG)

* Компьютер угадал число
![IMG_1910](https://user-images.githubusercontent.com/97599612/167812242-4a8d273c-51aa-415c-b27d-5be88b3c3cde.JPG)


[Вверх](#anchor)