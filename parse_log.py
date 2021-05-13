import sys
import logging
from liste import readlog, temps_minutes
from dico import regroupement, somme, change_values, pourcentage


def main(path):
    lecture = readlog(path)
    firstdico = regroupement(temps_minutes(lecture))
    dico_final = pourcentage(change_values(somme(firstdico)))
    with open("result.txt", "w", encoding="utf-8") as f:
        for key, valeur in dico_final.items():
            espace1 = (29 - (len(key)+len(valeur[1])))*" "
            espace2 = (6-(len(valeur[1])))*" "
            f.write(
                f"{key}{espace1}{valeur[0]} minutes{espace2}{valeur[1]}%\n")


if __name__ == "__main__":
    path = sys.argv[1]
    logging.basicConfig(filename="prog.log", level=logging.DEBUG)
    sys.exit(main(path))
