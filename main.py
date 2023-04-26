from tkinter import *
import random





def draw():
    canvas.delete("all")
    w = 300 // m
    h = 300 // n
    for i in range(n):
        for j in range(m):
            canvas.create_rectangle(j * w, i * h, j * w + w, i * h + h, fill=colors[a[i][j]])


def click(event):
    column = event.x // 60
    row = event.y // 60
    print(column, row)
    if a[row][column] != 0:
        flood(a, row, column)
        draw()


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


a = [[1, 1, 2, 2, 3, 9],
     [2, 2, 1, 3, 1, 9],
     [1, 3, 3, 2, 1, 9],
     [2, 1, 1, 3, 3, 9],
     [3, 1, 3, 2, 3, 9],
     [9, 9, 9, 9, 9, 9]]


for i in range(5):
    for j in range(5):
      a[i][j] = random.randint(1, 3)

def fall(a):
    pass

colors = ["white", "red", "blue", "green"]
m = n = 5
window = Tk()
window.title("same game")
canvas = Canvas(window, height=300, width=300, bg="white")
canvas.pack()
draw()
canvas.bind('<Button-1>', click)
window.mainloop()
