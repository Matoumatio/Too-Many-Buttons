from customtkinter import *
from PIL import Image

def ouvrir_page2():
    page2 = CTkToplevel()
    page2.geometry("400x300")
    page2.title("deuxième page")
    button2 = CTkButton(page2, text="Ouvrir la troisième page", command=ouvrir_page3)
    button2.pack(pady=20)
    page2_image_label = CTkLabel(page2, image=page2_image)
    page2_image_label.pack(pady=20)

def ouvrir_page3():
    page3 = CTkToplevel()
    page3.geometry("400x300")
    page3.title("troisième page")

app = CTk()
app.geometry("700x500")
app.title("première page")
app.after(2000, ouvrir_page2)  # Ouvre la deuxième page après 2 secondes

button = CTkButton(app, text="Ouvrir la deuxième page", command=ouvrir_page2)
button.pack(pady=20)

page2_image = CTkImage(dark_image=Image.open("assets/cassoulet.png"), size=(200, 200))

app.mainloop()