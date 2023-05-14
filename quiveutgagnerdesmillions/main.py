from guizero import App, Text, PushButton, Box, Picture
import csv
import random
import pygame
import tkinter as tk
import os
import shutil
import tkinter as tk
from tkinter import filedialog
#Initialisation des variables#
question_actuelle = 0

somme = 0 
tabb=[]
index = 0
logreponse = []
chemin = "musique/"
#Chargement des questions et des réponses depuis le fichier CSV#
def lecture_csv(c):
    with open(c, newline='',encoding='utf-8-sig') as csvfile:
        fichier = csv.DictReader(csvfile, delimiter=',')
        for ligne in fichier :
            tabb.append(dict(ligne))
        print('////')
        print('////')
        print(tabb)
        return tabb

def retouraumenu():
    global index, somme, gamegrid, tabb
    gamegrid.destroy()
    index = 0
    somme = 0
    tabb = []
    menu()
def findejeu():
    global index, somme, tabb
    index = 0
    somme = 0
    tabb = []
    menu()


def check(reponse):
    global somme, gamegrid, index, logreponse, solde, index
    if reponse == tabb[index]["reponse1"]:
       
        somme = somme + 100
        logreponse.append(tabb[index]["reponse1"] + " : Bonne réponse")
        print(logreponse)
    else: 
        print("Mauvaise réponse")
        logreponse.append(tabb[index]["reponse1"] + " : Mauvaise réponse")
       
    gamegrid.destroy() 
    if index < len(tabb) - 1:

        index = index + 1
    
        generate()
    else:
        app.info("Votre score", "Vous avez gagné " + str(somme) + "€")
        findejeu()
        

        
    

  
#genener les boutons pour les réponses
def generate():
    tab = [1, 2, 3, 4]
    random.shuffle(tab)
    global gamegrid, logreponse
    gamegrid = Box(app, layout="grid")
    title = Text(gamegrid, text="Qui veux gagner des millions ?", size=40, font="Arial", color="blue", grid=[0, 0])
    spacers = Box(gamegrid, height=100, width=10, grid=[0, 1])
    question = Text(gamegrid, text=tabb[index]["question"], size=20, font="Arial", color="white", grid=[0, 2])
    spacers = Box(gamegrid, height=100, width=10, grid=[1, 0])


    for i in range(4):
      
        button = PushButton(gamegrid, width=30, text=tabb[index]["reponse" + str(tab[i])], grid=[0, i + 4], command=check, args=[tabb[index]["reponse" + str(tab[i])]])
    spacers = Box(gamegrid, height=100, width=10, grid=[0, 8])
    displaysolde = Text(gamegrid, text="Votre solde est de " + str(somme) + "€", size=20, font="Arial", color="white", grid=[0, 9])
    logbox = Box(gamegrid, height=100, width=10, grid=[1, 10], layout="grid", border=False)
    #
    #
    #log des reponses
    
        
    #
    #
    #
    
    button = PushButton(gamegrid, text="Quitter", grid=[0, 11], command=retouraumenu, width=10)
#page suivante et lancer les questions 
def launch(chemin):
    c = chemin
    lecture_csv(c)
    gridniveaux.destroy()
    generate()

#quitter la page musique pour retourner au menu
def quittermusique():
    griddemusique.destroy()
    menu()
def refresh():
    griddemusique.destroy()
    musiquepage()
#lorseque l'utilisateur choisis une musique il est copié dans le dossier musique
def selectmusique(reponse):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("musique/" + reponse + ".mp3") 
    pygame.mixer.music.play(loops=0)
#jouer la musique selectionne
def selectmusiquefromfile():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    if file_path:
        print("Le chemin du fichier sélectionné est :", file_path)
        destination_folder = "musique/"
        shutil.copy(file_path, destination_folder)
        app.info("Operation en cour", "Cette opération va prendre un moment")
        refresh()


    else:
        print("Aucun fichier sélectionné.")


#page musique
def musiquepage():
    global chemin, griddemusique
    r = 0
    griddemusique = Box(app, layout="grid")
    title = Text(griddemusique, text="Choisiser votre musique", size=40, font="Arial", color="white", grid=[0,0])
    noms_fichiers = os.listdir(chemin)
    for nom_fichier in noms_fichiers:
        nom_bouton = os.path.splitext(nom_fichier)[0]
        bouton = PushButton(griddemusique, text=nom_bouton, grid=[0, r +1], args=[nom_bouton], width=0, command=selectmusique)
        r = r+1
    spacer = Box(griddemusique, height=100, width=10, grid=[0, r +2])
    buttonquitter = PushButton(griddemusique, text="Quitter", grid=[0, r + 3], command=quittermusique, width=10)
    import_button = PushButton(griddemusique, text="Importer", command=selectmusiquefromfile, grid=[1, 0])



def menuniveaux():
    gridmenu.destroy()
    global gridniveaux
    gridniveaux = Box(app, layout="grid", border=False)
    title = Text(gridniveaux, text="Choisiser votre niveaux", size=40, font="Arial", color="white", grid=[0,0])
    spacer = Box(gridniveaux, grid=[0, 1], height=100, width=10)
    bouttonenfant = PushButton(gridniveaux, text="Niveaux Enfants", grid=[0, 2], width=10,  command=launch, args=["questionenfant.csv"])
    spacer = Box(gridniveaux, grid=[0, 3], height=100, width=10)
    bouttonadulte = PushButton(gridniveaux, text="Niveaux Adulte", grid=[0, 4], width=10, command= launch, args=["questions.csv"])


def quitterlog():
    griddelog.destroy()
    menu()

def logpage():
    global logreponse, griddelog
    griddelog = Box(app, layout="grid")
    title = Text(griddelog, text="Log systeme", size=40, font="Arial", color="white", grid=[0,0])
    for j in logreponse:
       log = Text(griddelog, text=j, size=10, font="Arial", color="white", grid=[0, logreponse.index(j) +1 ])

    buttonquitter = PushButton(griddelog, text="Quitter", grid=[0, 12], command=quitterlog, width=10)



def musiquesection():
    gridmenu.destroy()
    musiquepage()
    
def logsection():
    gridmenu.destroy()
    logpage()

backdroundcolor = "purple"
listcouleur = ["red", "blue", "green", "yellow", "orange", "pink", "brown", "black", "white", "grey", "purple"]
def petiteanimationstyler():
    global backdroundcolor, listcouleur
    backdroundcolor = random.choice(listcouleur)
    app.bg = backdroundcolor
    app.after(5, petiteanimationstyler)

def quittertout():
    pygame.mixer.music.stop()
    app.destroy()


def menu():
    global gridmenu
    gridmenu = Box(app, layout="grid")
    title = Text(gridmenu, text="Qui veux gagner des millions ?", size=40, font="Arial", color="blue", grid=[0,0])
    picture = Picture(gridmenu, image="menu.gif", visible=True, grid=[0,1])
    spacer = Box(gridmenu, height=100, width=10, grid=[0,2])
    button1 = PushButton(gridmenu, text="Jouer", grid=[0,3], command=menuniveaux, width=20)
    faitpar = Text(gridmenu, text="Fait par Alexandre Thénot et son groupe", grid=[0, 12], color="white")
    spacer = Box(gridmenu, height=20, width=10, grid=[0,4])
    button2 = PushButton(gridmenu, text="Quitter", grid=[0,5], command=quittertout,  width=20)
    spacer = Box(gridmenu, height=20, width=10, grid=[0,6])
    button3 = PushButton(gridmenu, text="Log systeme", grid=[0,7], command=logsection,  width=20)
    spacer = Box(gridmenu, height=20, width=10, grid=[0,8])
    button4 = PushButton(gridmenu, text="Musique", grid=[0,9], command=musiquesection,  width=20)






app = App(title="Qui veux gagner des millions ?")

app.bg = backdroundcolor
#title and a button




###MAIN###
extreme = app.yesno("Petite question", "Avant de commencer voulez vous vous faire secouer les yeux ?")

if extreme == True:
    app.info("Alors c'est parti", "Vous aller regretter d'avoir dit oui...")
else:
    app.error("PFFFFFFF", "Tant pis pour vous")
pygame.mixer.init()
if extreme == True:
    pygame.mixer.music.load("musique/Hardcore Bass Music.mp3")
else:
    pygame.mixer.music.load("musique/theme1.mp3")
pygame.mixer.music.play(loops=0)



menu()
if extreme == True:
    petiteanimationstyler()
app.full_screen = True
app.display()

