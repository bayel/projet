from tkinter import *
import tkinter as tk
import dbm

root = Tk()
dbmfile = dbm.open ('dbfile','c')

#permet de faire une selection sur un nom
def clic(evt): 
    i=listbox.curselection()
    return listbox.get(i)

# permet de supprimer 
def clear():
    i=listbox.curselection()
    listbox.delete(i)

# permet d'ajouter une clé et une valeur dans le fichier 
def add():
    listbox.insert(tk.END, etud.get())
    dbmfile[etud.get()]= etud.get()
    #get_list()
    for k in dbmfile.keys():
        print(dbmfile[k].decode())    
    
        
#ajouter les boutons
msg = Label(None, text = 'Etudiants ITS', fg = 'purple')
ajouter = Button(None, text = 'Ajouter', fg = 'green', command=add)
supprimer = Button(None, text = 'Supprimer', fg = 'red', command=clear)
etud = tk.Entry(width=8)

#dbmfile['1'] = etud.get()

#permet de créer une listbox pour afficher les données
listbox=Listbox(root, bg='white', fg='blue')
listbox.bind('<ButtonRelease-1>',clic)

#méthodes applicables aux widgets et qui agit sur leur disposition dans la fenêtre
msg.pack()
ajouter.pack()
supprimer.pack()
etud.pack()
listbox.pack()

#for item in ["rougui", "alex", "melina", "nassimi"]:
#   listbox.insert(END, item)


#méthode qui active la boucle du programme
root.mainloop()

dbmfile.close()