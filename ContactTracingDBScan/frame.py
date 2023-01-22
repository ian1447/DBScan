from tkinter import *
from tkinter import ttk

win =Tk()

def start():
    traced_frame = LabelFrame(win)
    wrapper2 = LabelFrame(win)

    traced_frame_canvas = Canvas(traced_frame)
    traced_frame_canvas.pack(side=LEFT, fill="both", expand="yes")

    myscrollbar = ttk.Scrollbar(traced_frame, orient="vertical", command=traced_frame_canvas.yview)
    myscrollbar.pack(side=RIGHT, fill="y")

    traced_frame_canvas.configure(yscrollcommand=myscrollbar.set)

    traced_frame_canvas.bind('<Configure>', lambda e: traced_frame_canvas.configure(scrollregion=traced_frame_canvas.bbox('all')))

    myFrame = Frame(traced_frame_canvas)
    traced_frame_canvas.create_window((0,0), window=myFrame, anchor="nw")

    traced_frame.pack(fill="both", expand="yes", padx=10, pady=10)
    wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

    for i in range(50):
        Button(myFrame, text = "asd" + str(i)).pack()
start()


win.geometry("500x500")
win.resizable(False,False)
win.title("MyScroller")
win.mainloop()
