import logging


def readlog(path):
    """
    cette fonction ouvre un fichier le lit
    ligne par ligne et renvoie le resultat
    dans une liste de liste.
    """
    liste = []
    with open(path, "r", encoding="utf-8") as f:
        logging.info("ouverture du fichier par la fonction readlog")
        line = f.readline()
        liste.append(line.strip().split(" ", 1)[::-1])
        
        while line:
            line = f.readline()
            newline = line.strip()
            if len(newline) != 0:
                l = newline.split(" ", 1)[::-1]
                liste.append(l)
    logging.info(f"stockage du fichier dans la variavle liste {liste}")
    return liste

def temps_minutes(liste_log):
    """
    cette fonction prend des heures aux format
    hh:min - hh:min calcul l'ecart entre les deux
    et remplace ces indication par le temps en minute
    dans le dictionnaire
    """
    logging.info(
        "stockage du resultat de la fonction readlog() dans une variable")
    detail_minutes = []
    for t in liste_log:
        time = t[1].split("-")
        a = time[0].split(":")
        b = time[1].split(":")
        minutes = [(int(b[0])*60+int(b[1]))-(int(a[0])*60+int(a[1]))]
        detail_minutes.append([t[0], minutes])
    logging.info(f"remplacement des temps par \
                les minutes retour d'une liste {detail_minutes}")
    return detail_minutes

def regroupement(liste_minutes):
    """
    cette fonction sert a regrouper les temps
    en minutes dans une liste des actions identiques.
    Elle prend une liste de liste en entrée
    et retourne un dictionnaire avec les action comme 
    clés et une liste de valeur
    """
    dico = {}
    logging.info("lancement de la fonction regroupement")
    for word in liste_minutes:
        if word[0] in dico:
            dico[word[0]] += word[1]
        else:
            dico[word[0]] = word[1]
    logging.info(f"on a regrouper dans un dictionnaire \
                  les différente valeur pour chaque exercices {dico}")
    return dico
