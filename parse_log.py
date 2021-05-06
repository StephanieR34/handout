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

# liste_log=[['Introduction', '09:20-11:00'], ['Exercises', '11:00-11:15'], ['Break', '11:15-11:35'], ['Exercises', '13:30-14:10'], ['Break', '14:30-14:40']]
def temps_minutes(liste_log):
    detail=liste_log
    logging.info("stockage du resultat de la fonction readlog() dans une variable")
    detail_minutes=[]
    for t in detail:
        logging.info("decoupage de la liste pour travailler sur les temps")
        time = t[1].split("-")        
        a=time[0].split(":")
        b=time[1].split(":") 
        minutes = (int(b[0])*60+int(b[1]))-(int(a[0])*60+int(a[1]))
        
        detail_minutes.append([t[0],minutes])
        

    logging.info(f"remplacement des temps par les minutes retour d'une liste {detail}")  
    return detail_minutes




def total_time(log_minutes):
    elements = log_minutes
    logging.info("")
    total=0
    for i in elements:
        total+= i[-1]
    return total
# log_minutes = [['Exercises', 105], ['Solutions', 15], ['Functions', 30], ['Exercises', 30]]
# print(type(total_time(log_minutes)))
# def regroupement():
    
#     for word in temps_minutes(path):
        
    
#     return cnt

def main(path):
    for l in readlog(path):
        return temps_minutes(readlog(path))

print(main("planning.log"))




        


# if __name__ == "__main__":
#     sys.exit(main())