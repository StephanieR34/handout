import sys
import logging

logging.basicConfig(filename="prog.log",level=logging.DEBUG)

def readlog(path):
    #dico={}
    liste=[]
    with open(path, "r", encoding="utf-8") as f:  
        logging.info("ouverture du fichier")  
        line = f.readline()
        logging.info("lecture de la premiere ligne du fichier")
        
        while line:
            logging.info(f"stockage de f.readline dans la variable {line}")
            line = f.readline()
            newline = line.strip()
            
            if len(newline) != 0:
                l=newline.split(" ",1)[::-1]
                #dico[l[0]]=l[1]

                liste.append(l)
                logging.info(f"on stock les lignes dans une liste")
                
    #return(dico)
    return liste


def temps_minutes(path):
    detail=readlog(path)
    logging.info("stockage du resultat de la fonction readlog() dans une variable")
    for t in detail:
        logging.info("decoupage de la liste pour travailler sur les temps")
        time = t[1].split("-")
        
        a=time[0].split(":")
        b=time[1].split(":")
        
        minutes = (int(b[0])*60+int(b[1]))-(int(a[0])*60+int(a[1]))
        t[1]=minutes

    logging.info(f"remplacement des temps par les minutes retour d'une liste {detail}")  
    return detail


        

        
    
print(temps_minutes('planning.log'))

# if __name__ == "__main__":
#     sys.exit(main())