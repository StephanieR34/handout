import sys
import logging

logging.basicConfig(filename="prog.log",level=logging.DEBUG)

def readlog(path):
    
    liste=[]
    with open(path, "r", encoding="utf-8") as f:  
        logging.info("ouverture du fichier")  
        line = f.readline()
        liste.append(line.strip().split(" ",1)[::-1])
        logging.info("lecture de la premiere ligne du fichier")
        
        while line:

            logging.info(f"stockage de f.readline dans la variable {line}")
            line = f.readline()
            newline = line.strip()
            
            if len(newline) != 0:
                l=newline.split(" ",1)[::-1]
                liste.append(l)
                logging.info(f"on stock les lignes dans une liste")
                
    #return(dico)
    return liste


def temps_minutes(liste_log):
    logging.info("stockage du resultat de la fonction readlog() dans une variable")
    detail_minutes=[]
    for t in liste_log:
        logging.info("decoupage de la liste pour travailler sur les temps")
        time = t[1].split("-")        
        a=time[0].split(":")
        b=time[1].split(":") 
        minutes = [(int(b[0])*60+int(b[1]))-(int(a[0])*60+int(a[1]))]
        
        detail_minutes.append([t[0],minutes])
        

    logging.info(f"remplacement des temps par les minutes retour d'une liste {liste_log}")  
    return detail_minutes
#print(temps_minutes([['Introduction', '09:20-11:00'], ['Exercises', '11:00-11:15'], ['Break', '11:15-11:35'], ['Exercises', '13:30-14:10'], ['Break', '14:30-14:40']]))




def regroupement(liste_minutes):
    dico = {}
    for word in liste_minutes:
        
        if word[0] in dico:
            dico[word[0]] +=  word[1]
        else:
            dico[word[0]] = word[1]
        
    return dico


def somme(dico_minute):
    for key,valeur in dico_minute.items():
        a=0
        for m in valeur:
            a += m
        dico_minute[key]=[str(a)]
    return dico_minute
          
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
    for key,valeur in minutes.items() :
        a= int("".join(valeur))
        p=int(a / total * 100)       
        valeur+=[str(p)]
    return minutes   
        
# print(pourcentage({'Introduction': ["75"], 'Exercises': ["40"]}))

def main(path):
    for l in readlog(path):
        return pourcentage(somme(regroupement(temps_minutes(readlog(path)))))


print(main("planning.log"))



        


# if __name__ == "__main__":
#     sys.exit(main())