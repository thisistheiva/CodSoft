from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("570x600")
window.resizable(False, False)
window.configure(bg = "#17161b")

expression = ""

def show(value):
    global expression
    expression += value
    result.config(text = expression)
    
def clear():
    global expression
    expression = ""
    result.config(text = expression)
    
def calc():
    global expression
    output = "" 
    if expression != "":
        try:
            output = eval(expression)  
        except:
            output = "error"
            expression = ""   
    result.config(text = output)              

result = Label(window, width = 25, height = 2, text ="", font = ("arial", 30), bg = "grey")
result.pack()

Button(window, text = "7", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("7")).place(x = 10, y = 100)
Button(window, text = "8", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("8")).place(x = 150, y = 100)
Button(window, text = "9", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("9")).place(x = 290, y = 100)
Button(window, text = "+", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#ff6ec7", command = lambda: show("+")).place(x = 430, y = 100)

Button(window, text = "4", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("4")).place(x = 10, y = 200)
Button(window, text = "5", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("5")).place(x = 150, y = 200)
Button(window, text = "6", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("6")).place(x = 290, y = 200)
Button(window, text = "-", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#ff6ec7", command = lambda: show("-")).place(x = 430, y = 200)

Button(window, text = "1", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("1")).place(x = 10, y = 300)
Button(window, text = "2", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("2")).place(x = 150, y = 300)
Button(window, text = "3", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("3")).place(x = 290, y = 300)
Button(window, text = "*", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#ff6ec7", command = lambda: show("*")).place(x = 430, y = 300)

Button(window, text = "0", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show("0")).place(x = 10, y = 400)
Button(window, text = ".", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: show(".")).place(x = 150, y = 400)
Button(window, text = "C", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#4c454c", command = lambda: clear()).place(x = 290, y = 400)
Button(window, text = "/", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#ff6ec7", command = lambda: show("/")).place(x = 430, y = 400)

Button(window, text = "=", width = 16, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#ff6ec7", command = lambda: calc()).place(x =10, y = 500)
Button(window, text = "%", width = 5, height = 1 , font = ("arial", 30 , "bold"), bd = 1, fg = "#fff", bg = "#ff6ec7", command = lambda: show("%")).place(x = 430, y = 500)

window.mainloop()