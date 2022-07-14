#!/usr/bin/python

from tkinter import *
from tkinter import filedialog
from random import randint, choice
import string
import os

home_path = os.path.expanduser('~')

def browse_button():
    global filename
    filename = filedialog.askdirectory(initialdir=home_path)
    print(filename)
    return filename

def download_music():

    artist = str(artist_entry.get())
    album = str(album_entry.get())
    url = str(url_entry.get())
    os.makedirs(f"{filename}/{artist}/{album}")
    print(f"Les dossiers {artist} et {album} ont été créés")
    os.chdir(f"{filename}/{artist}/{album}")
    os.system(f'python3 -m spotdl {url}')
    artist_entry.delete(0, END)
    album_entry.delete(0, END)
    url_entry.delete(0, END)
    
    

# Créer la fenêtre
window = Tk()
window.title("Spotdl")
window.geometry("800x480")
# window.iconbitmap(default="headphones.ico")
window.config(background='#4065A4')
window.minsize(800, 480)

# Créer frame principale
frame = Frame(window, bg='#4065A4')

# Création d'image
width = 300
height = 300
image = PhotoImage(file="headphones.png").zoom(20).subsample(45)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)


# Créer une sous boite à la droite de l'écran
right_frame = Frame(frame, bg='#4065A4')


# Créer un titre
# label_title = Label(right_frame, text="SpotDl", font=("Helvetica", 30), bg='#4065A4', fg='white')
label_title = Label(text="SpotDl", font=("Courier", 40, "bold"), bg='#4065A4', fg='white') # Titre sur fenêtre principale
label_title.pack(expand=YES)

# Rentrer dossier destionation
label_destination_path = Label(right_frame, text="Dossier de destination: ", font=("Helvetica", 20), bg='#4065A4', fg='white', width=25)
label_destination_path.pack()
browser_button = Button(right_frame, text="Explorateur de fichiers", font=("Helvetica", 20), bg='white', fg='#4065A4', command=browse_button)
browser_button.pack(fill=X)

# Rentrer Artiste
label_artist = Label(right_frame, text="Nom de l'artiste: ", font=("Helvetica", 20), bg='#4065A4', fg='white', width=25, pady=5)
label_artist.pack()
artist_entry = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black', justify="center", width=25)
artist_entry.pack(fill=X)

# Rentrer album
label_album = Label(right_frame, text="Nom de l'album: ", font=("Helvetica", 20), bg='#4065A4', fg='white', width=25, pady=5)
label_album.pack()
album_entry = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black', justify="center", width=25)
album_entry.pack(fill=X)

# Rentrer URL
label_url = Label(right_frame, text="Url: ", font=("Helvetica", 20), bg='#4065A4', fg='white', width=25, pady=5)
label_url.pack()
url_entry = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black', justify="center", width=25)
url_entry.pack(fill=X)

# Créer un bouton
label_blanck = Label(right_frame, font=("Helvetica", 20), bg='#4065A4', fg='white', width=25, pady=5)
label_blanck.pack()
generate_password_button = Button(right_frame, text="Télécharger", font=("Helvetica", 20), bg='white', fg='#4065A4', command=download_music)
generate_password_button.pack(fill=X)

# On place la sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# Afficher la frame
frame.pack(expand=YES)

# Afficher la fenêtre
window.mainloop()
