from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import urllib.parse

root = Tk()
root.title("Book Recommend System")
root.geometry("1250x700+200+100")
root.config(bg="#111119")

##################################################################################################################

# icon
icon_image = PhotoImage(file="Images/app_icon.png")
root.iconphoto(False, icon_image)

# background image
bg_image_original = Image.open("Images/bg.png")
bg_image_resized = bg_image_original.resize((1250, 300), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(bg_image_resized)
Label(root, image=bg_image, bg="#111119").place(x=-2, y=-2)

#logo
logo_image_original = Image.open("Images/logo.png")
logo_image_resized = logo_image_original.resize((60, 60), Image.Resampling.LANCZOS)
logo_image = ImageTk.PhotoImage(logo_image_resized)
Label(root, image=logo_image, bg="#2f2f2a").place(x=300, y=80)

#heading
heading = Label (root, text="Book Recommendation", font=("Lato", 35, "bold"), fg="white", bg="#2f2f2a")
heading.place(x=410, y=81)

#search background image
searchBar_image_original = Image.open("Images/search_bar.png")
searchBar_image_resized = searchBar_image_original.resize((600, 100), Image.Resampling.LANCZOS)
searchBar_image = ImageTk.PhotoImage(searchBar_image_resized)
Label(root, image=searchBar_image, bg="#2f2f2a").place(x=250, y=155)

#entry box / search selection
Search = StringVar()
search_entry = Entry(root, textvariable=Search, width=18, font=("Lato", 30, "italic"), bg="white", fg="black", bd=0)
search_entry.place(x=417, y=180)

#search button
search_button_image = Image.open("Images/search_button.png")
search_button_image_resized = search_button_image.resize((240, 75), Image.Resampling.LANCZOS)
search_button_image = ImageTk.PhotoImage(search_button_image_resized)
search_button = Button(root, image=search_button_image, bg="#2f2f2a", bd=0, activebackground="#2f2f2a", cursor="hand2").place(x=748, y=165)
Label(root, image=search_button_image, bg="#2f2f2a")

##################################################################################################################

root.mainloop()
