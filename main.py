import random
import numpy as np
import pandas as pd
from data import *

jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
heures_cours = ["7h30-8h15", "8h15-9h", "9h-9h45", "9h45-10h30", "10h50-11h35", "11h35-12h20", "12h20-13h05", "13h05-13h50"]
all_prof = list(prof_cours.keys())

def generate_horaire(level,section,year,cours):
 
    horaire=np.full((8,5),"              ")
    profs_assigned = set()  # Ensemble pour stocker les professeurs déjà assignés
    prof_i=10

    for i in range(len(cours)):
        cour = cours[i]
        profs_available = [prof for prof in all_prof if prof not in profs_assigned]
        
      
        
        
        
        
        while Class_cours[level][section][year][cour] > 0 :
            
                    ligne = random.randint(0, 7)
                    colonne = random.randint(0, 4)
                    if horaire[ligne, colonne] == "              ":
                        horaire[ligne, colonne] = cour
                        Class_cours[level][section] [year][cour] -= 1
        
    return horaire




for level in level_list:
    if level=="fondamental":
        
        for year in year_fond:
            
            print("\n\n\n")
            print(f"Horaire de la classe de {year}\n********************************\n")
            affi_horaire = pd.DataFrame(generate_horaire(level=level,section="sect",year=year,cours=fondomatal_cours), columns=jours_semaine, index=heures_cours)
            print(affi_horaire)
            
    elif level=="post_fondamental":
        
        for i in range(3):
            section=section_post_fond[i]
            for year in all_year[i]:
                print("\n\n\n")        
                print(f"Horaire de la classe de {year}\n********************************\n")
                affi_horaire = pd.DataFrame(generate_horaire(level=level,section=section,year=year,cours=all_cours[i]), columns=jours_semaine, index=heures_cours)
                print(affi_horaire)
       