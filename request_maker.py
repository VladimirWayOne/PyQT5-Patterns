import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from gui import mainframe

from tkinter import messagebox, Text, Tk, WORD, DISABLED, Label, Entry, Checkbutton, Button, Frame, StringVar


class Auth_Window(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.ready_to_close = False

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky='E')
        self.label_password.grid(row=1, sticky='E')
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)
        self.creditianals = ('', '')


        self.pack()

    def __del__(self):
        print(self.creditianals)
        self.destroy()


    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.creditianals = (username, password)

        # print(username, password)

        if username == "admin" and password == "admin":
            messagebox.showinfo("Login info", "Welcome John")
            print('Ready to close')
            self.ready_to_close = True
            self.destroy()

        else:
            messagebox.showerror("Login error", "Incorrect username")



class App(QtWidgets.QMainWindow, mainframe.Ui_MassRequests):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.btn_find_fit.clicked.connect(self.browse_fit)
        #self.btn_save.clicked.connect(self.browse_path)
        #self.btn_go.clicked.connect(self.go)


root = None
login = None


def main():
    root = Tk()
    login = Auth_Window(root)



    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()





def quit():
    global login_screen
    login_screen.destroy()


def login():
    # getting form data
    uname = username.get()
    pwd = password.get()
    # applying empty validation
    if uname == '' or pwd == '':
        message.set("fill the empty field!!!")
    else:
        if uname == "test" and pwd == "test":
            message.set("Login success")
            close_frame = True
            quit()
        else:
            message.set("Wrong username or password!!!")


def Loginform():
    global login_screen
    # Setting title of screen
    login_screen.title("Login Form")
    # setting height and width of screen
    login_screen.geometry("300x250")
    # declaring variable
    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()
    # Creating layout of login form
    Label(login_screen, width="300", text="Please enter details below", bg="orange", fg="white").pack()
    # Username Label
    Label(login_screen, text="Username * ").place(x=20, y=40)
    # Username textbox
    Entry(login_screen, textvariable=username).place(x=90, y=42)
    # Password Label
    Label(login_screen, text="Password * ").place(x=20, y=80)
    # Password textbox
    Entry(login_screen, textvariable=password, show="*").place(x=90, y=82)
    # Label for displaying login status[success/failed]
    Label(login_screen, text="", textvariable=message).place(x=95, y=100)
    # Login button
    Button(login_screen, text="Login", width=10, height=1, bg="orange", command=login).place(x=105, y=130)
    login_screen.mainloop()

if __name__ == '__main__':
    login_screen = Tk()
    Loginform()
    main()
