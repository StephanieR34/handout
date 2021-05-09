import sys
import logging



def readlog(path):
    
    liste=[]
    with open(path, "r", encoding="utf-8") as f:  
        logging.info("ouverture du fichier par la fonction readlog")  
        line = f.readline()
        liste.append(line.strip().split(" ",1)[::-1])
        
        while line:
            line = f.readline()
            newline = line.strip()            
            if len(newline) != 0:
                l=newline.split(" ",1)[::-1]
                liste.append(l)               
    logging.info(f"stockage du fichier dans la variavle liste {liste}")           
    return liste


def temps_minutes(liste_log):
    logging.info("stockage du resultat de la fonction readlog() dans une variable")
    detail_minutes=[]
    for t in liste_log:
        time = t[1].split("-")        
        a=time[0].split(":")
        b=time[1].split(":") 
        minutes = [(int(b[0])*60+int(b[1]))-(int(a[0])*60+int(a[1]))] 
        detail_minutes.append([t[0],minutes])
    logging.info(f"remplacement des temps par les minutes retour d'une liste {detail_minutes}")  
    return detail_minutes




def regroupement(liste_minutes):
    dico = {}
    logging.info("lancement de la fonction regroupement")
    for word in liste_minutes:
        
        if word[0] in dico:
            dico[word[0]] +=  word[1]
        else:
            dico[word[0]] = word[1]
    logging.info(f"on a regrouper dans un dictionnaire les différente valeur pour chaque exercices {dico}")   
    return dico


def somme(dico_minute):
    #logging.info("lancement de la fonction somme")
    for key,valeur in dico_minute.items():
        dico_minute[key]=[sum(valeur)]
        logging.info(valeur)
        logging.info(type(valeur))

    return dico_minute

def change_values(minutes):
    for key,valeur in minutes.items():
        for j in valeur :
            j= str(j)
        minutes[key]=[j]
            
    return minutes

def total_time(log_minutes):
    logging.info("ouverture de la fonction total_time")
    total=0
    for key, valeur in log_minutes.items():
        total+=int("".join(valeur))
    logging.info(f"return {total}")
    return total


def pourcentage(minutes):
    logging.info("ouverture fonction pourcentage")
    total =total_time(minutes)
    for valeur in minutes.values() :
        a= int("".join(valeur))
        p=round(a / total * 100)       
        valeur+=[str(p)]
    return minutes   
        

def main(path):
    
    dico_final=pourcentage(change_values(somme(regroupement(temps_minutes(readlog(path))))))
        
    with open("result.txt", "w", encoding="utf-8") as f:  
        for key,valeur in dico_final.items():
            espace1= (29 - (len(key)+len(valeur[1])))*" "
            espace2= (6-(len(valeur[1])))*" "
            f.write(f"{key}{espace1}{valeur[0]} minutes{espace2}{valeur[1]}%\n")


if __name__ == "__main__":

    path = sys.argv[1]

    logging.basicConfig(filename="prog.log",level=logging.DEBUG)
    sys.exit(main(path))