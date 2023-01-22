import tkinter as tk

root = tk.Tk()


####### Create Button ###############

def get_text(text):
    print(text)


for i in range(10):
    text = f'Hello I am BeginnerSQL74651 {i}'
    button = tk.Button(root, text=text, command=lambda button_text=text: get_text(button_text))
    button.grid()

root.mainloop()
