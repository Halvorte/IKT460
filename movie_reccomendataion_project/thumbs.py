from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Thumbs Up or Thumbs Down")

my_img = ImageTk.PhotoImage(Image.open("images/john_wick_2.jpg"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

button_thumbs_up = Button(root, text="Thumbs Up")
button_thumbs_up.pack()

button_thumbs_down = Button(root, text="Thumbs Down")
button_thumbs_down.pack()

root.mainloop()