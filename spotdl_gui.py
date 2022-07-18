#!/usr/bin/python

from tkinter import *
from tkinter import filedialog
import os
import time


## Variables ##
home_path = os.path.expanduser('~')
download_param_album = '{artists}/{album}/ {artists} - {title}.{ext}'
download_param_playlist = '{playlist}/{artists}/{album} - {title} {artist}.{ext}'

# Font Color #
title2_font_color="white"



def file_explorer():
    global filename
    filename = filedialog.askdirectory(initialdir=home_path)
    default_path.set(filename)
    print(filename)
    return filename

def download_progress(status):

    if status == "download":
        download_button["text"]="Téléchargement en cours..."
    elif status == "finish":
        download_button["text"]="Téléchargement terminé"
    elif status == "wait":
        download_button["text"]="Télécharger"
    download_button.update()

    

def download_music():

    url_1 = str(url_entry_1.get())
    url_2 = str(url_entry_2.get())
    url_3 = str(url_entry_3.get())
    url_4 = str(url_entry_4.get())
    url_5 = str(url_entry_5.get())

    #url_playlist = str(url_playlist_entry.get())
    path = str(destination_path_entry.get())

    if "album" in url_1:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print ("album found")
        os.system(f'python3 -m spotdl {url_1} -p "{download_param_album}"')
        os.remove(".spotdl-cache")
        url_entry_1.delete(0, END)
        download_progress("finish")
        time.sleep(3)
        download_progress("wait")
    elif "playlist" in url_1:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print("playlist found")
        os.system(f'python3 -m spotdl {url_1} -p "{download_param_playlist}"')
        os.remove(".spotdl-cache")
        url_entry_1.delete(0, END)
        
    
    if "album" in url_2:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print ("album found")
        os.system(f'python3 -m spotdl {url_2} -p "{download_param_album}"')
        os.remove(".spotdl-cache")
        url_entry_2.delete(0, END)    
    elif "playlist" in url_2:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print("playlist found")
        os.system(f'python3 -m spotdl {url_2} -p "{download_param_playlist}"')
        os.remove(".spotdl-cache")
        url_entry_2.delete(0, END)

    if "album" in url_3:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print ("album found")
        os.system(f'python3 -m spotdl {url_3} -p "{download_param_album}"')
        os.remove(".spotdl-cache")
        url_entry_3.delete(0, END)
    elif "playlist" in url_3:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print("playlist found")
        os.system(f'python3 -m spotdl {url_3} -p "{download_param_playlist}"')
        os.remove(".spotdl-cache")
        url_entry_3.delete(0, END)

    if "album" in url_4:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print ("album found")
        os.system(f'python3 -m spotdl {url_4} -p "{download_param_album}"')
        os.remove(".spotdl-cache")
        url_entry_4.delete(0, END)   
    elif "playlist" in url_4:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print("playlist found")
        os.system(f'python3 -m spotdl {url_4} -p "{download_param_playlist}"')
        os.remove(".spotdl-cache")
        url_entry_4.delete(0, END)

    if "album" in url_5:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print ("album found")
        os.system(f'python3 -m spotdl {url_5} -p "{download_param_album}"')
        os.remove(".spotdl-cache")
        url_entry_5.delete(0, END)
    elif "playlist" in url_5:
        download_progress("download")
        #os.makedirs(f"{path}")
        os.chdir(f"{path}")
        print("playlist found")
        os.system(f'python3 -m spotdl {url_5} -p "{download_param_playlist}"')
        os.remove(".spotdl-cache")
        url_entry_5.delete(0, END) 

    download_progress("finish")
    time.sleep(3)
    download_progress("wait")

## Tkinter ##

# Créer la fenêtre
window = Tk()
window.title("Spotdl")
window.geometry("950x500")
# window.iconbitmap(default="headphones.ico")
window.config(background='#4065A4')
window.minsize(950, 500)
window.maxsize(950, 500)

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
label_title = Label(text="SpotDl", font=("Courier", 40, "bold"), bg='#4065A4', fg=title2_font_color) # Titre sur fenêtre principale
label_title.pack(expand=YES)

# Rentrer dossier destionation
label_destination_path = Label(right_frame, text="Dossier de destination: ", font=("Helvetica", 20), bg='#4065A4', fg=title2_font_color, width=25)
label_destination_path.pack()

default_path = StringVar()
default_path.set(home_path)
destination_path_entry = Entry(right_frame, textvariable=default_path, font=("Helvetica", 20), bg='white', fg='black', justify="center", width=40)
destination_path_entry.pack()
browser_button = Button(right_frame, text="Explorateur de fichiers", font=("Helvetica", 20), bg='white', fg='black', command=file_explorer)
browser_button.pack(fill=X)


# Rentrer URL
label_url = Label(right_frame, text="Url (Album ou Playlist): ", font=("Helvetica", 20), bg='#4065A4', fg=title2_font_color, width=25, pady=5)
label_url.pack()
url_entry_1 = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black', justify="center", width=25)
url_entry_1.pack(fill=X)
url_entry_2 = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black', justify="center", width=25)
url_entry_2.pack(fill=X)
url_entry_3 = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black', justify="center", width=25)
url_entry_3.pack(fill=X)
url_entry_4 = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black', justify="center", width=25)
url_entry_4.pack(fill=X)
url_entry_5 = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black', justify="center", width=25)
url_entry_5.pack(fill=X)

# Créer un bouton
label_blanck = Label(right_frame, font=("Helvetica", 20), bg='#4065A4', fg=title2_font_color, width=25, pady=5)
label_blanck.pack()
download_button = Button(right_frame, text="Télécharger", font=("Helvetica", 20), bg='white', fg='black', command=download_music)
download_button.pack(fill=X)

# On place la sous boite à droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)

# Afficher la frame
frame.pack(expand=YES)

# Afficher la fenêtre
window.mainloop()
