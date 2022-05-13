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
<img width="522" alt="GG1" src="https://user-images.githubusercontent.com/97599612/168244955-b6cc58ed-df8c-4999-9f31-1e26f4e9dd75.png">

* При нажатии кнопки 'Сгенерировать число' появлятся всплывающее окно
<img width="701" alt="GG2" src="https://user-images.githubusercontent.com/97599612/168244979-1cd0bde4-a884-4766-bd97-74a7ff40d276.png">

* Программа дает подсказки (больше, меньше) если введеное число не равно загаданному
<img width="520" alt="GG3" src="https://user-images.githubusercontent.com/97599612/168244995-5215f805-65b6-43c9-81fe-f67f86b2ed2d.png">

* Программа дает подсказки (больше, меньше) если введеное число не равно загаданному
<img width="523" alt="GG4" src="https://user-images.githubusercontent.com/97599612/168245005-99bae883-4376-45d8-938e-1601358372e5.png">

* Вы отгадали! Загаднное число __
<img width="530" alt="GG5" src="https://user-images.githubusercontent.com/97599612/168245010-31fa2799-4137-447a-b892-135ab92bba72.png">

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
<img width="453" alt="GGR1" src="https://user-images.githubusercontent.com/97599612/168245014-cb20ccb7-fbba-41c6-b042-47e77b88feac.png">

* При возникновении ValueError появится всплывающее окно
<img width="757" alt="GGR2" src="https://user-images.githubusercontent.com/97599612/168245015-c838de3a-cf7e-48c4-b0d0-f764be484d97.png">

* Компьютер угадал число
<img width="453" alt="GGR3" src="https://user-images.githubusercontent.com/97599612/168245016-ed4d4694-6adb-4460-b17a-4f9d4cc07174.png">


[Вверх](#anchor)