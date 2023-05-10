from tkinter import *
import random
from rules import rules_window


def draw():
    canvas.delete("all")
    w = 300 // m
    h = 300 // n
    for i in range(n):
        for j in range(m):
            canvas.create_rectangle(j * w, i * h, j * w + w, i * h + h, fill=colors[a[i][j]])


def click(event):
    global count
    column = event.x // 60
    row = event.y // 60
    print(column, row)
    if a[row][column] != 0:
        count += 1
        label.config(text=f'Количество ходов: {count}')
        flood(a, row, column)
        draw()
        canvas.after(500, fall)
        canvas.after(600, draw)
        canvas.after(1050, move)
        canvas.after(1100, draw)



def flood(a, row, column):
    old_color = a[row][column]
    a[row][column]=0
    if a[row][column - 1] == old_color:
        flood(a,row, column - 1)
    if a[row - 1][column] == old_color:
        flood(a, row - 1, column)
    if a[row][column + 1] == old_color:
        flood(a, row, column +1)
    if a[row + 1][column] == old_color:
        flood(a, row + 1, column)


def new_game():
    for i in range(5):
        for j in range(5):
            a[i][j] = random.randint(1, 3)
            draw()


def save():
    b = []
    for i in a:
        b.append(" ".join([str(j) for j in i]) + "\n")
    f = open("save.txt", "w")
    f.writelines(b)
    f.close()








def restore():
    f = open("save.txt", "r")
    b = f.readlines()
    f.close()
    for i in range(n):
        for j in range(m):
            a[i][j] = int(b[i].split()[j])
    draw()


def fall():
    for k in range(10):
        for i in range(5):
            for j in range(5):
                if a[i + 1][j] == 0:
                    a[i + 1][j] = a[i][j]
                    a[i][j] = 0


def move():
    for k in range(10):
        for j in range(4):
            flag = True
            for i in range(5):
                if a[i][j] != 0:
                    flag = False
            if flag:
                for i in range(5):
                    a[i][j] = a[i][j + 1]
                    a[i][j + 1] = 0





a = [[1, 1, 2, 2, 3, 9],
     [2, 2, 1, 3, 1, 9],
     [1, 3, 3, 2, 1, 9],
     [2, 1, 1, 3, 3, 9],
     [3, 1, 3, 2, 3, 9],
     [9, 9, 9, 9, 9, 9]]

for i in range(5):
    for j in range(5):
        a[i][j] = random.randint(1, 3)

count = 0
colors = ["white", "red", "blue", "green"]
m = n = 5
window = Tk()
window.title("same game")
label = Label(text = "Количество очков: 0  ")
label.pack()
canvas = Canvas(window, height=300, width=300, bg="white")
canvas.pack()
draw()
canvas.bind('<Button-1>', click)
mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новая игра",
                     command=new_game)
filemenu.add_command(label="Сохранить",
                     command=save)
filemenu.add_command(label="Восстановить",
                     command=restore)
mainmenu.add_cascade(label="Игра",
                     menu=filemenu)
progmenu = Menu(mainmenu, tearoff=0)
progmenu.add_command(label="Правила игры", command=rules_window)
mainmenu.add_cascade(label="О программе",
                     menu=progmenu)
window.mainloop()



