from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('postgresql://Host:Adresse:Port/Name')
Base = declarative_base()

# Datenbanken

class Schule(Base):
    __tablename__ = 'schule'
    id = Column(Integer, primary_key=True)
    Schulname = Column(String)
    Schulort = Column(String)
    klassenzimmer = relationship("Zimmer", back_populates="schule")

class Zimmer(Base):
    __tablename__ = 'klassenzimmer'
    id = Column(Integer, primary_key=True)
    Klasse = Column(String)
    schule_id = Column(Integer, ForeignKey("schule.id"))
    schule = relationship("Schule", back_populates="klassenzimmer")
    schueler = relationship("Schueler", back_populates="klassenzimmer")
    lehrer = relationship("Lehrer", back_populates="klassenzimmer")

class Lehrer(Base):
    __tablename__ = 'lehrer'
    id = Column(Integer, primary_key=True)
    vorname = Column(String)
    nachname = Column(String)
    geburtstag = Column(Date)
    fach = Column(String)
    klassenzimmer_id = Column(Integer, ForeignKey('klassenzimmer.id'))
    klassenzimmer = relationship("Zimmer", back_populates="lehrer")

class Schueler(Base):
    __tablename__ = 'schüler'
    id = Column(Integer, primary_key=True)
    vorname = Column(String)
    nachname = Column(String)
    geburtstag = Column(Date)
    klassenzimmer_id = Column(Integer, ForeignKey('klassenzimmer.id'))
    klassenzimmer = relationship("Zimmer", back_populates="schueler")




Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

schule_liste = [

    {"Schulname": "Graf Mohr Schule", "Schulort":"Meersburg"}

]

schueler_liste = [

    {"Vorname": "Chris",    "Nachname": "Weiß",        "Geburtstag": "2005-12-24"},
    {"Vorname": "Paul",     "Nachname": "Mohr",        "Geburtstag": "2004-02-03"},
    {"Vorname": "Maik",     "Nachname": "Krämer",      "Geburtstag": "1996-04-01"},
    {"Vorname": "Marcel",   "Nachname": "Cubek",       "Geburtstag": "2002-07-18"},
    {"Vorname": "Davide",   "Nachname": "Mazzitelli",  "Geburtstag": "1993-03-15"},
    {"Vorname": "Leon",    "Nachname": "Weiß",        "Geburtstag": "2005-12-24"},
    {"Vorname": "Bob",     "Nachname": "Mohr",        "Geburtstag": "2004-02-03"},
    {"Vorname": "Gerhart",     "Nachname": "Krämer",      "Geburtstag": "1996-04-01"},
    {"Vorname": "Joe",   "Nachname": "Cubek",       "Geburtstag": "2002-07-18"},
    {"Vorname": "Günther",   "Nachname": "Mazzitelli",  "Geburtstag": "1993-03-15"},
    {"Vorname": "Marc",    "Nachname": "Weiß",        "Geburtstag": "2005-12-24"},
    {"Vorname": "Gustav",     "Nachname": "Mohr",        "Geburtstag": "2004-02-03"},
    {"Vorname": "KeineAhnung",     "Nachname": "Krämer",      "Geburtstag": "1996-04-01"},
    {"Vorname": "Gabriel",   "Nachname": "Cubek",       "Geburtstag": "2002-07-18"},
    {"Vorname": "Pascal",   "Nachname": "Mazzitelli",  "Geburtstag": "1993-03-15"},
    {"Vorname": "Can",    "Nachname": "Weiß",        "Geburtstag": "2005-12-24"},
    {"Vorname": "Naruto",     "Nachname": "Mohr",        "Geburtstag": "2004-02-03"},
    {"Vorname": "Gündogan",     "Nachname": "Krämer",      "Geburtstag": "1996-04-01"},
    {"Vorname": "OptimusPrime",   "Nachname": "Cubek",       "Geburtstag": "2002-07-18"},
    {"Vorname": "GriechischerWEIN",   "Nachname": "Mazzitelli",  "Geburtstag": "1993-03-15"},
]

lehrer_liste = [
    {"Vorname": "Michael",  "Nachname": "Litera",       "Geburtstag": "1993-05-12", "Fach": "Programmiertechnik"},
    {"Vorname": "Walter",   "Nachname": "Maulhardt",    "Geburtstag": "2002-07-18", "Fach": "Elektrotechnik"},
    {"Vorname": "Jürgen",   "Nachname": "Funke",        "Geburtstag": "1996-04-11", "Fach": "Kommunikationstechnik"},
    {"Vorname": "Uwe",      "Nachname": "Maulhardt",    "Geburtstag": "1979-03-05", "Fach": "Informationstechnik"},
]

klassenzimmer_liste = [
    {"Klasse": "10A"},
    {"Klasse": "10B"},
    {"Klasse": "10C"},
    {"Klasse": "10D"},
]

# Datensätze

for schule in schule_liste:
    new_school = Schule(Schulname=schule["Schulname"], Schulort=schule["Schulort"])
    session.add(new_school)
schueler_gruppen = [schueler_liste[i:i+5] for i in range(0, len(schueler_liste), 5)]
schueler_counter = 1


for gruppe in schueler_gruppen:
    for schueler in gruppe:
        new_schueler = Schueler(vorname=schueler["Vorname"], nachname=schueler["Nachname"], geburtstag=schueler["Geburtstag"], klassenzimmer_id=schueler_counter)
        session.add(new_schueler)
    schueler_counter += 1

lehrer_counter = 1

for lehrer in lehrer_liste:
    new_lehrer = Lehrer(vorname=lehrer['Vorname'], nachname=lehrer['Nachname'], geburtstag=lehrer['Geburtstag'], fach=lehrer['Fach'], klassenzimmer_id=lehrer_counter)
    session.add(new_lehrer)
    lehrer_counter += 1

for zimmer in klassenzimmer_liste:
    klassen_zimmer = Zimmer(Klasse=zimmer['Klasse'], schule_id=1)
    session.add(klassen_zimmer)

session.commit()
