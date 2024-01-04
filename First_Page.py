import subprocess
from tkinter import *
w=Tk()
w.geometry('300x148')
def btn(x,y,text,bcolor,fcolor,path):
    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor
    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolor

    def on_click():
        # Run the external script when the button is clicked
        subprocess.run(["python", path])
    mybutton = Button(w, width=43, height=2, text=text,fg=bcolor,bg=fcolor,border=0,activebackground=bcolor,activeforeground=fcolor,command=on_click)
    mybutton.bind('<Enter>',on_enter)
    mybutton.bind('<Leave>',on_leave)
    mybutton.place(x=x, y=y)

w.configure(bg='#040c0c')
btn(0,0,"Créer les données",'#24baa3','#197069','createdata.py')
btn(0,37,"Importer un fichier des données",'#24baa3','#197069','ImporterData.py')
btn(0,74,"Représnter les données",'#24baa3','#197069','RepData.py')
btn(0,111,"Gestion des données",'#24baa3','#197069','manageData.py')
btn(0,148,"Algorithmes de machine learning",'#24baa3','#197069','algo.py')

w.mainloop()