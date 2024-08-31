import tkinter as tk
def click(event):
    global expression
    expression += event.widget.cget("text")
    equation.set(expression)
def clear():
    global expression
    expression = ""
    equation.set("")
def calculate():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""
expression = ""
root = tk.Tk()
root.title("Simple Calculator")
equation = tk.StringVar()
display = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
row_value = 1
column_value = 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=calculate)
    elif button == "C":
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=clear)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18))
        btn.bind("<Button-1>", click)
    btn.grid(row=row_value, column=column_value)

    column_value += 1
    if column_value > 3:
        column_value = 0
        row_value += 1
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=2)
root.mainloop()