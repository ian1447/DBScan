from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
from tkinter import messagebox
from datetime import datetime

root = Tk()
root.title("Contact Tracing")
root.resizable(False, False)
root.geometry("1000x550")

global is_header
is_header = False

# creating widgets
# myLabel = Label(root, text='Hello World!') #for text
# for bisu image
image = Image.open("background.png")
resize_image = image.resize((570, 550))
my_img = ImageTk.PhotoImage(resize_image)  # for images
my_img_label = Label(image=my_img)

# for bisu logo
logo = Image.open("logonobg.png")
logo_label = ImageTk.PhotoImage(logo)  # for images
logo_image = Label(image=logo_label)

# text labels
myLabel = Label(root, text='BISU\nContact Tracing', font=('Times', 24))  # for text


# grouplabel = Label(root, text='Group 8', font = ('Times',16)) #for text

def header():
    global header_logo
    header_logo = ImageTk.PhotoImage(Image.open("logonobg.png"))  # for images
    header_logo_label = Label(image=header_logo)
    header_logo_label.pack(side="left", anchor="nw", padx=(300, 0))

    header_logo_label = Label(root, text='Bohol Island State University', font=('Times', 17))  # for text
    header_logo_label.pack(anchor="n", pady=30, side="left")
    header_logo_address_label = Label(root, text='Tagbilaran City Bohol', font=('Times', 14))  # for text
    header_logo_address_label.place(x=470, y=60)

    separator = ttk.Separator(root, orient='horizontal')
    separator.place(relx=0, rely=0.22, relwidth=1, relheight=1)

def start_program():
    global rfid_pic
    global start_label
    global rfid_image_label
    global contact_tracing_Button
    global from_trace
    global is_header
    if not is_header:
        header()
        is_header = True

    start_label = Label(root, text="Please Scan RFID...", font=('Times', 20))
    start_label.place(x=420, y=140)

    rfid = Image.open("RFIDnobg.png")
    rfid_resized = rfid.resize((300, 300))
    rfid_pic = ImageTk.PhotoImage(rfid_resized)
    rfid_image_label = Label(image=rfid_pic)
    rfid_image_label.place(x=400, y=180)

    contact_tracing_Button = Button(root, text="Contact Tracing", padx=10, pady=10, font=('Times', 24),
                                    command=clear_start_show_details)
    contact_tracing_Button.place(x=750, y=465)

def clear_front_page():
    startButton.destroy()
    myLabel.destroy()
    logo_image.destroy()
    my_img_label.destroy()
    start_program()

def clear_start_contact_tracing():
    start_label.destroy()
    rfid_image_label.destroy()
    contact_tracing_Button.destroy()
    contact_tracing()

def clear_start_register():
    start_label.destroy()
    rfid_image_label.destroy()
    contact_tracing_Button.destroy()
    register()
    #show_details()

def clear_start_show_details():
    start_label.destroy()
    rfid_image_label.destroy()
    contact_tracing_Button.destroy()
    show_details()

def clear_contact_tracing():
    name_label.destroy()
    name_entry.destroy()
    trace_button.destroy()
    back_button.destroy()
    traced_frame1.destroy()
    start_program()

def contact_tracing():
    global name_label
    global name_entry
    global trace_button
    global back_button
    global traced_frame1

    from_trace = True

    name_label = Label(root, text="Enter Name: ", font=('Times', 20))
    name_label.place(x=250, y=130)

    name_entry = ttk.Entry(root, width=20, font=('Times', 20))
    name_entry.place(x=400, y=130)

    trace_button = Button(root, text="Trace", font=('Times', 14), command=trace)
    trace_button.place(x=700, y=130)

    traced_frame1 = LabelFrame(root, text="People Subject to Contact Tracing", font=('Times', 14))
    traced_frame_canvas = Canvas(traced_frame1)
    traced_frame_canvas.pack(side=LEFT, fill="both", expand="yes")

    myscrollbar = ttk.Scrollbar(traced_frame1, orient="vertical", command=traced_frame_canvas.yview)
    myscrollbar.pack(side=RIGHT, fill="y")

    traced_frame_canvas.configure(yscrollcommand=myscrollbar.set)

    traced_frame_canvas.bind('<Configure>',
                             lambda e: traced_frame_canvas.configure(scrollregion=traced_frame_canvas.bbox('all')))

    myframe = Frame(traced_frame_canvas)
    traced_frame_canvas.create_window((0, 0), window=myframe, anchor="nw")

    traced_frame1.place(x=100, y=180, width=800, height=300)
    back_button = Button(root, text="Back", padx=2, pady=2, font=('Times', 24), command=clear_contact_tracing)
    back_button.place(x=895, y=480)

    Label(myframe, text="No One").pack()

def trace():
    global myframe
    for widgets in traced_frame1.winfo_children():
        widgets.destroy()

    traced_frame = LabelFrame(root, text="People Subject to Contact Tracing", font=('Times', 14))
    traced_frame_canvas = Canvas(traced_frame)
    traced_frame_canvas.pack(side=LEFT, fill="both", expand="yes")

    myscrollbar = ttk.Scrollbar(traced_frame, orient="vertical", command=traced_frame_canvas.yview)
    myscrollbar.pack(side=RIGHT, fill="y")

    traced_frame_canvas.configure(yscrollcommand=myscrollbar.set)

    traced_frame_canvas.bind('<Configure>',
                             lambda e: traced_frame_canvas.configure(scrollregion=traced_frame_canvas.bbox('all')))

    myframe = Frame(traced_frame_canvas)
    traced_frame_canvas.create_window((0, 0), window=myframe, anchor="nw")

    traced_frame.place(x=100, y=180, width=800, height=300)
    back_button = Button(root, text="Back", padx=2, pady=2, font=('Times', 24), command=clear_contact_tracing)
    back_button.place(x=895, y=480)

    for i in range(50):
        Label(myframe, text=name_entry.get()).pack()

def register():
    global enter_course_entry
    global enter_name_entry
    global enter_address_entry
    global filename
    filename = ""
    traced_label = Label(root, text="Register", font=('Times', 24))
    traced_label.place(x=480, y=130)
    upload_button = Button(root, text="Upload Photo", font=('Times', 14), command=upload_photo)
    upload_button.place(x=170, y=190)
    enter_name_label = Label(root, text="Name: ", font=('Times', 15))
    enter_name_label.place(x=430, y=220)
    enter_name_entry = ttk.Entry(root, width=45, font=('Times', 13))
    enter_name_entry.place(x=530, y=220)
    enter_course_label = Label(root, text="Course: ", font=('Times', 15))
    enter_course_label.place(x=430, y=260)
    enter_course_entry = ttk.Entry(root, width=45, font=('Times', 13))
    enter_course_entry.place(x=530, y=260)
    enter_address_label = Label(root, text="Address: ", font=('Times', 15))
    enter_address_label.place(x=430, y=300)
    enter_address_entry = ttk.Entry(root, width=45, font=('Times', 13))
    enter_address_entry.place(x=530, y=300)
    register_button = Button(root, text="Register", font=('Times', 24), command=register_details)
    register_button.place(x=620, y=340)

def upload_photo():
    global img
    global filename
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if filename:
        upload_image = Image.open(filename)
        resize_img = upload_image.resize((250, 250))
        img = ImageTk.PhotoImage(resize_img)
        b2 = Label(root, image=img)  # using Button
        b2.place(x=100, y=230)

def register_details():
    if enter_name_entry.get() == "" or enter_course_entry.get() == "" or enter_address_entry.get() == "":
        messagebox.showwarning('Error', 'Error: Please Fill up Data!')
    else:
        if filename == "":
            messagebox.showwarning('Error', 'Error: Please Add Photo!')
        else:
            print(enter_name_entry.get())
            print(enter_course_entry.get())
            print(enter_address_entry.get())
            print(filename)

def show_details():
    global sample_pic
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    rfid = Image.open("RFID.jpg")
    rfid_resized = rfid.resize((300, 300))
    sample_pic = ImageTk.PhotoImage(rfid_resized)
    rfid_image_label = Label(image=sample_pic)
    rfid_image_label.place(x=100, y=170)

    detail_name_label = Label(root, text="Name: ", font=('Times', 18))
    detail_name_label.place(x=500, y=180)
    detail_name = Label(root, text="Ric Ian Jamora", font=('Times', 18))
    detail_name.place(x=600, y=180)
    detail_course_label = Label(root, text="Course: ", font=('Times', 18))
    detail_course_label.place(x=500, y=220)
    detail_course = Label(root,text="BSCpE", font=('Times', 18))
    detail_course.place(x=600, y=220)
    detail_address_label = Label(root, text="Address: ", font=('Times', 18))
    detail_address_label.place(x=500, y=260)
    detail_address = Label(root, text="Tagbilaran ", font=('Times', 18))
    detail_address.place(x=600, y=260)
    detail_time_label = Label(root, text="Time: ", font=('Times', 18))
    detail_time_label.place(x=500, y=300)
    detail_time = Label(root, text=currentTime, font=('Times', 18))
    detail_time.place(x=600, y=300)
    detail_temp_label = Label(root, text="Temperature: ", font=('Times', 18))
    detail_temp_label.place(x=500, y=340)
    detail_temp = Label(root, text="36.1\N{DEGREE SIGN}C", font=('Times', 18))
    detail_temp.place(x=640, y=340)
    detail_room_label = Label(root, text="Room: ", font=('Times', 18))
    detail_room_label.place(x=500, y=380)
    detail_room_entry = ttk.Entry(root, width=20, font=('Times', 13))
    detail_room_entry.place(x=600, y=385)

    save_button = Button(root, text="Save", font=('Times', 24))
    save_button.place(x=895, y=480)

    #for image showing
    # upload_image = Image.open(filename)
    # resize_img = upload_image.resize((250, 250))
    # img = ImageTk.PhotoImage(resize_img)
    # b2 = Label(root, image=img)  # using Button
    # b2.place(x=100, y=230)

# button labels
startButton = Button(root, text="Start", padx=10, pady=10, font=('Times', 24), command=clear_front_page)

# puting label into the root
my_img_label.pack(side=LEFT, anchor="w", fill=BOTH)
logo_image.pack(anchor="center", pady=40)
myLabel.pack(anchor="n")
# grouplabel.pack()
startButton.pack(anchor="center", pady=50)

root.mainloop()
