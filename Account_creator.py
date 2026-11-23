from tkinter import *
Window = Tk()
Window.title("Account creator.")
Window.geometry("500x500")
Frame1 = Frame(master = Window, relief = "groove", bg = "green", width = 400, height = 200)
Frame1.pack()
Full_name = Label(text = "Full name", fg = "white", bg = "blue", width = 20)
Email_id = Label(text = "Email id", fg = "white", bg = "blue", width = 20)
Enter_password = Label(text = "Enter_password", fg = "white", bg = "blue", width = 20)
Entry1 = Entry()
Entry2 = Entry()
Entry3 = Entry(show = "*")
Full_name.place(x = 60, y = 20)
Entry1.place(x = 300, y = 20)
Email_id.place(y = 60, x = 60)
Entry2.place(x = 300, y = 60)
Enter_password.place(y = 100, x = 60)
Entry3.place(x = 300, y = 100)
text = Text(height = 100, width = 500)
def button_pressed():
    Name = Entry1.get()
    Msg = f"Hi, {Name}, Congrats for making a new account!"
    text.insert(END, Msg)
    text.pack()

Button1 = Button(text = "Create Account", fg = "blue", bg = "White", command = button_pressed)
Button1.place(x = 210, y = 150)
Window.mainloop()

    
