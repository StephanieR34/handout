import logging


def readlog(path):
    liste = []
    with open(path, "r", encoding="utf-8") as f:
        logging.info("ouverture du fichier par la fonction readlog")
        line = f.readline()
        liste.append(line.strip().split(" ", 1)[::-1])     
        while line:
            line = f.readline()
            newline = line.strip()
            if len(newline) != 0:
                liste = newline.split(" ", 1)[::-1]
                liste.append(liste)
    logging.info(f"stockage du fichier dans la variavle liste {liste}")
    return liste


def temps_minutes(liste_log):
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
