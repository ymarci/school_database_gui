import customtkinter as ctk
import pywinstyles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datenbank_definitionen import Schule, Zimmer, Lehrer, Schueler
from tkinter import messagebox


# Verbindung zur Datenbank herstellen
db_url = 'postgresql://Host:Adresse:Port/Name'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()


# Funktion um Schülerdaten aus der Datenbank abzurufen

def retrieve_school_from_db():
    try:
        schulen_list = session.query(Schule).all()
        schulen_names = [schule.Schulname for schule in schulen_list]
        schule_menu.configure(values=schulen_names)

    except Exception as e:
        messagebox.showerror("Database Error", f"Error retrieving school data from the database: {e}")

def retrieve_class_from_db():
    try:
        Klassen_List = session.query(Zimmer).all()
        Klassen_names = [f"{zimmer.Klasse}" for zimmer in Klassen_List]
        klasse_menu.configure(values=Klassen_names)

    except Exception as e:
        messagebox.showerror("Database Error", f"Error retrieving class data from the database: {e}")

def retrieve_teacher_from_db():
    try:
        teacher_list = session.query(Lehrer).join(Zimmer).all()
        teacher_names = [f"{teacher.vorname} {teacher.nachname}" for teacher in teacher_list]
        teacher_data = "\n".join(teacher_names)
        teacher_entry.configure(text=teacher_data)

    except Exception as e:
        messagebox.showerror("Database Error", f"Fehler: {e}")

def retrieve_pupils_from_db():
    try:
        schueler_list = session.query(Schueler).join(Zimmer).all()
        schueler_names = [f"{schueler.vorname} {schueler.nachname}" for schueler in schueler_list]
        for name in schueler_names:
            label = ctk.CTkLabel(scroll_pupils, text=name)
            label.pack()

    except Exception as e:
        messagebox.showerror("Fehler: {e}")

# GUI

# Fenstereinstellungen

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("800x700")
root.title("Datenbank V1.0 Pre-Alpha")
pywinstyles.apply_style(window=root, style="acrylic")

# Überschrift
title_label = ctk.CTkLabel(root, text="Schuldatenbank", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(pady=20)

# Schulauswahl Optionenmenü
txt_school = ctk.CTkLabel(root, text="Schulauswahl", font=ctk.CTkFont(size=20))
txt_school.pack(pady=20)
schule_menu = ctk.CTkOptionMenu(root, width=500, height=40, values=["Bitte auswählen."])
schule_menu.pack()
retrieve_school_from_db()

# Klassenauswahl Optionenmenü
txt_class = ctk.CTkLabel(root, text="Klassenauswahl", font=ctk.CTkFont(size=20))
txt_class.pack(pady=20)
klasse_menu = ctk.CTkOptionMenu(root, width=500, height=40, values=["Bitte auswählen."])
klasse_menu.pack()
retrieve_class_from_db()

# Lehrer Button
txt_class = ctk.CTkLabel(root, text="Lehrer", font=ctk.CTkFont(size=20))
txt_class.pack(pady=20)
teacher_entry = ctk.CTkButton(root, width=500, height=25)
teacher_entry.pack()
retrieve_teacher_from_db()


# Schülerliste Scrollableframe
txt_pupil = ctk.CTkLabel(root, text="Schülerliste", font=ctk.CTkFont(size=20))
txt_pupil.pack(pady=20)
scroll_pupils = ctk.CTkScrollableFrame(root, width=500, height=200)
scroll_pupils.pack()
#retrieve_pupils_from_db()

root.mainloop()
