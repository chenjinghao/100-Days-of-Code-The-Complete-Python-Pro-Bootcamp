from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
from random import randint

watermarked_photo = None

def open_file():
    filename = filedialog.askopenfilename()
    return filename

def save_file():
    filename = filedialog.asksaveasfilename(defaultextension=".jpg")
    if not filename:
        return
    open_image.save(filename)

def add_watermark():
    file = open_file()
    img = Image.open(fp=file)
    watermark_text = text.get()

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 40)

    width, height = img.size 
    x=width/100
    y=height/100

    draw.text((x,y), text=watermark_text, font=font)


    img.save(rf'C:/Users/JingH/Desktop/watermarked_{randint(0,1000)}.jpg')

    photo = ImageTk.PhotoImage(img)
    watermarked_photo = ttk.Label(window,image=photo)
    watermarked_photo.image = photo
    watermarked_photo.grid(column=1,row=8)  


window = Tk()
window.title('Watermark 4 Photo')
window.config(width=1200, height=600, padx=40, pady=40)

mainframe = ttk.Frame(window)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Watermak 4 Photo', font=('bold', 24)).grid(column=1, row=0, columnspan=2)
ttk.Label(mainframe,text='-Adam CHEN JINGHAO').grid(column=1, row=1, columnspan=2, sticky=(E))

ttk.Label(mainframe,text='Text into Photo: ').grid(column=1,row=3)
text = StringVar()
ttk.Entry(mainframe, textvariable=text).grid(column=2,row=3)

open_image = ttk.Button(mainframe, 
           text='Choose a photo to add Watermark',command=add_watermark
           ).grid(column=1,row=8, columnspan=2)


window.mainloop()
