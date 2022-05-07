from tkinter import *
from tkinter import ttk
class app:
    def __init__(self):
        # Principale window :
        self.window = Tk()
        self.primary_color = "#1E90FF"
        self.secondary_color = "black"
        self.window.geometry("1080x750")
        self.window.resizable(0, 0)
        self.name = StringVar()
        self.mo1 = StringVar()
        self.mo2 = StringVar()
        self.mo3 = StringVar()
        #ajoute des composantes :
        self.window.label_name = Label(self.window,text="Nom&Prenom", bd=0,fg=self.primary_color,
            font="Courrier 14")
        self.window.entry_name = Entry(self.window,textvariable=self.name, bd=0,fg=self.primary_color,
            font="Courrier 10")
        #exemple pour 3 modules :
        self.window.label_module1 = Label(self.window,text="Note M1", bd=0,fg=self.primary_color,
            font="Courrier 14")
        self.window.entry_module1 = Entry(self.window,textvariable=self.mo1, bd=0,fg=self.primary_color,
            font="Courrier 10")
        self.window.label_module2 = Label(self.window,text="Note M2", bd=0,fg=self.primary_color,
            font="Courrier 14")
        self.window.entry_module2 = Entry(self.window,textvariable=self.mo2, bd=0,fg=self.primary_color,
            font="Courrier 10")
        self.window.label_module3 = Label(self.window,text="Note M3", bd=0,fg=self.primary_color,
            font="Courrier 14")
        self.window.entry_module3 = Entry(self.window,textvariable=self.mo3, bd=0,fg=self.primary_color,
            font="Courrier 10")
        #ajoute d une btn pour le calcule et l affichage : 
        self.window.btn_calc = Button(self.window,text="enregistré", bd=1 ,bg=self.primary_color,
            font="Courrier 14",fg=self.secondary_color, width=15)
        #ajoute tableau  :
        tete = ('Nom', 'Moyenne','statue')
        self.window.tableau = ttk.Treeview(self.window, height=12, show="headings", column=tete)
        # ------> Creation des colones :
        self.window.tableau.column("Nom", width="300", anchor=W)
        self.window.tableau.column("Moyenne", width="100", anchor=CENTER)
        self.window.tableau.column("statue", width="150", anchor=CENTER)
        # ------> Creation des tetes :
        self.window.tableau.heading("Nom", text="Nom")
        self.window.tableau.heading("Moyenne", text="Moyenne")
        self.window.tableau.heading("statue", text="Statue")
        #emplacer les elements dans la fenetre :
        self.window.label_name.place(relx=0.01,rely=0.05)
        self.window.entry_name.place(relx=0.25,rely=0.05)
        self.window.label_module1.place(relx=0.01,rely=0.1)
        self.window.entry_module1.place(relx=0.25,rely=0.1)
        self.window.label_module2.place(relx=0.01,rely=0.15)
        self.window.entry_module2.place(relx=0.25,rely=0.15)
        self.window.label_module3.place(relx=0.01,rely=0.2)
        self.window.entry_module3.place(relx=0.25,rely=0.2)
        #self.window.btn_calc.place(relx=0.01,rely=0.3)
        self.window.tableau.place(relx=0.45,rely=0.05)
    def run(self):
        self.window.mainloop()
        return


if __name__ == "__main__":
    my_app = app()
    my_app.run()