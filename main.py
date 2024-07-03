from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import urllib.parse

class Request:
    def __init__(self, method, args):
        self.args = args
        self.method = method

inc = 0
def fetch_information(title, poster, date, ratings):
    global inc
    inc = inc + 1

    text[f'a{inc}'].config(text=title)

    if check_var.get():
        text2[f'a{inc}{inc}'].config(text=date)
    else:
        text2[f'a{inc}{inc}'].config(text="")

    if check_var2.get():
        text3[f'a{inc}{inc}{inc}'].config(text=ratings)
    else:
        text3[f'a{inc}{inc}{inc}'].config(text="")

    response = requests.get(poster)
    img_data = response.content
    img = (Image.open(BytesIO(img_data)))
    resized_image = img.resize((155, 200))
    photo2 = ImageTk.PhotoImage(resized_image)
    image[f'b{inc}'].config(image=photo2)
    image[f'b{inc}'].image = photo2

def search():
    global inc
    inc = 0
    request = Request ('GET', {'search': Search.get()})

    if request.method == 'GET':
        search = urllib.parse.quote(request.args.get('search', ''))
        url = f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
        response = requests.get(url)
        #print(response.json())

        if response.status_code == 200:
            data = response.json()
            for item in data.get('items', []):
                volume_info = item.get('volumeInfo', {})
                title = volume_info.get('title', 'N/A')
                publisher = volume_info.get('publisher', 'N/A')
                published_date = volume_info.get('publishedDate', 'N/A')
                author = volume_info.get('authors', ['N/A'])
                ratings = volume_info.get('averageRating', ['N/A'])
                image_links = volume_info.get('imageLinks', {})
                image = image_links.get('thumbnail') if 'thumbnail' in image_links else 'N/A'

                print(title)
                print(publisher)
                print(published_date)
                print(author)
                print(ratings)
                print(image)

                fetch_information (title, image, published_date, ratings)

                if check_var.get() or check_var2.get():
                    frame11.place(x=160, y=600)
                    frame22.place(x=360, y=600)
                    frame33.place(x=560, y=600)
                    frame44.place(x=760, y=600)
                    frame55.place(x=960, y=600)
                else:
                    frame11.place_forget()
                    frame22.place_forget()
                    frame33.place_forget()
                    frame44.place_forget()
                    frame55.place_forget()

        else:
            print("Failed to Fetch Data From The Google Books API.")
            messagebox.showinfo("Error!", "Failed to Fetch Data From The Google Books API.")

#display the menu at the mouse position
def show_menu(event):
    menu.post(event.x_root, event.y_root)

root = Tk()
root.title("Book Recommend System")
root.geometry("1250x700+200+100")
root.config(bg="#111119")
root.resizable(False, False)

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
heading = Label (root, text="Book Recommendation", font=("Lato", 38, "bold"), fg="white", bg="#2f2f2a")
heading.place(x=410, y=81)

#search background image
searchBar_image_original = Image.open("Images/search_bar.png")
searchBar_image_resized = searchBar_image_original.resize((600, 100), Image.Resampling.LANCZOS)
searchBar_image = ImageTk.PhotoImage(searchBar_image_resized)
Label(root, image=searchBar_image, bg="#2f2f2a").place(x=250, y=155)

#entry box / search selection
Search = StringVar()
search_entry = Entry(root, textvariable=Search, width=17, font=("Lato", 30, "italic"), bg="white", fg="black", bd=0)
search_entry.place(x=350, y=180)

#search button
search_button_image = Image.open("Images/search_button.png")
search_button_image_resized = search_button_image.resize((240, 75), Image.Resampling.LANCZOS)
search_button_image = ImageTk.PhotoImage(search_button_image_resized)
search_button = Button(root, image=search_button_image, bg="#2f2f2a", bd=0, activebackground="#2f2f2a", cursor="hand2", command=search)
search_button.place(x=748, y=165)

#settings button
settings_image = Image.open("Images/settings.png")
settings_image_resized = settings_image.resize((50, 50), Image.Resampling.LANCZOS)
settings_image = ImageTk.PhotoImage(settings_image_resized)
settings = Button(root, image=settings_image, bd=0, cursor="hand2", activebackground="#2f2f2a", bg="#2f2f2a")
settings.place(x=1050, y=175)
settings.bind('<Button-1>', show_menu)

#menu for search button
menu = Menu(root, tearoff=0)

check_var = BooleanVar()
menu.add_checkbutton(
    label="Published Date", 
    variable=check_var, 
    command=lambda: print(f"Published Date Option is {'Checked' if check_var.get() else 'Unchecked'}")
)

check_var2 = BooleanVar()
menu.add_checkbutton(
    label="Ratings", 
    variable=check_var2, 
    command=lambda: print(f"Ratings Option is {'Checked' if check_var2.get() else 'Unchecked'}")
)

#logout button
logout_image = Image.open("Images/logout.png")
logout_image_resized = logout_image.resize((60, 60), Image.Resampling.LANCZOS)
logout_image = ImageTk.PhotoImage(logout_image_resized)
Button(root, image=logout_image, bg="#5c4b35", cursor="hand2", command=lambda: root.destroy()).place(x=1150, y=20)

##################################################################################################################

#first frame
frame1 = Frame (root, width=170, height=240, bg="#b7b7b7")
frame2 = Frame (root, width=170, height=240, bg="#b7b7b7")
frame3 = Frame (root, width=170, height=240, bg="#b7b7b7")
frame4 = Frame (root, width=170, height=240, bg="#b7b7b7")
frame5 = Frame (root, width=170, height=240, bg="#b7b7b7")
frame1.place(x=160, y=350)
frame2.place(x=360, y=350)
frame3.place(x=560, y=350)
frame4.place(x=760, y=350)
frame5.place(x=960, y=350)

#book title
text={
    'a1':Label(frame1, text="Book Title", font=("calibri", 16, "bold"), fg="black", bg="#b7b7b7"),
    'a2':Label(frame2, text="Book Title", font=("calibri", 16, "bold"), fg="black", bg="#b7b7b7"),
    'a3':Label(frame3, text="Book Title", font=("calibri", 16, "bold"), fg="black", bg="#b7b7b7"),
    'a4':Label(frame4, text="Book Title", font=("calibri", 16, "bold"), fg="black", bg="#b7b7b7"),
    'a5':Label(frame5, text="Book Title", font=("calibri", 16, "bold"), fg="black", bg="#b7b7b7")
}
text['a1'].place(x=10, y=4)
text['a2'].place(x=10, y=4)
text['a3'].place(x=10, y=4)
text['a4'].place(x=10, y=4)
text['a5'].place(x=10, y=4)

#poster / image of books
image={
    'b1':Label(frame1, bg="#b7b7b7"),
    'b2':Label(frame2, bg="#b7b7b7"),
    'b3':Label(frame3, bg="#b7b7b7"),
    'b4':Label(frame4, bg="#b7b7b7"),
    'b5':Label(frame5, bg="#b7b7b7")
}
image['b1'].place(x=3, y=30)
image['b2'].place(x=3, y=30)
image['b3'].place(x=3, y=30)
image['b4'].place(x=3, y=30)
image['b5'].place(x=3, y=30)

##################################################################################################################

#second frame
frame11 = Frame (root, width=170, height=70, bg="#e6e6e6")
frame22 = Frame (root, width=170, height=70, bg="#e6e6e6")
frame33 = Frame (root, width=170, height=70, bg="#e6e6e6")
frame44 = Frame (root, width=170, height=70, bg="#e6e6e6")
frame55 = Frame (root, width=170, height=70, bg="#e6e6e6")

#published date
text2={
    'a11':Label(frame11, text="Published Date", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6"),
    'a22':Label(frame22, text="Published Date", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6"),
    'a33':Label(frame33, text="Published Date", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6"),
    'a44':Label(frame44, text="Published Date", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6"),
    'a55':Label(frame55, text="Published Date", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6")
}
text2['a11'].place(x=10, y=4)
text2['a22'].place(x=10, y=4)
text2['a33'].place(x=10, y=4)
text2['a44'].place(x=10, y=4)
text2['a55'].place(x=10, y=4)

#ratings
text3={
    'a111':Label(frame11, text="Ratings", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6"),
    'a222':Label(frame22, text="Ratings", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6"),
    'a333':Label(frame33, text="Ratings", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6"),
    'a444':Label(frame44, text="Ratings", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6"),
    'a555':Label(frame55, text="Ratings", font=("calibri", 13, "bold", "italic"), fg="#0034ff", bg="#e6e6e6")
}
text3['a111'].place(x=20, y=35)
text3['a222'].place(x=20, y=35)
text3['a333'].place(x=20, y=35)
text3['a444'].place(x=20, y=35)
text3['a555'].place(x=20, y=35)

##################################################################################################################

root.mainloop()
