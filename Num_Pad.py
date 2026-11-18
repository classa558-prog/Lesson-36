from tkinter import *
Window = Tk()
Window.title = ("Num Pad")
Num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):

    for j in range(3):
        frame1 = Frame(master = Window, relief = "groove", borderwidth = 5)
        frame1.grid(row = i, column = j)
        label1 = Label(master = frame1, text = Num_list[i][j], width = 5, height = 3)
        label1.pack(padx = 5, pady = 5)
Window.mainloop()


