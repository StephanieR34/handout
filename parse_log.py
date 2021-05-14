import sys
import logging
from liste import readlog, regroupement, temps_minutes
from dico import  ordre, somme, change_values, pourcentage


def main(path):
    """
    Fonction principale qui prend le résultat disponible
    en format dictionaire et l'ecris dans un fichier txt
    en respectant les consignes
    43 caractères
    6 carateères aprés le s de minutes
    """
    dico_final = pourcentage(
        change_values(somme(ordre(regroupement(temps_minutes(readlog(path)))))))
    with open("result.txt", "w", encoding="utf-8") as f:
        for key, valeur in dico_final.items():
            espace1 = (26 - (len(key)+len(valeur[0])))*" "
            logging.info(f"l'espace 1 = {len(espace1)} \
                        la clé = {len(key)} la valeur[1] = {len(valeur[0])}")
            espace2 = (6-(len(valeur[1])))*" "
            logging.info(f"l'espace 2 = {len(espace2)} la valeur[2] = {len(valeur[1])} ")
            tableau = f"{key}{espace1}{valeur[0]} minutes{espace2}{valeur[1]}%\n"
            f.write(tableau)
            logging.info(f"la longueur des lignes est de = {len(tableau)}")


if __name__ == "__main__":
    path = sys.argv[1]
    logging.basicConfig(filename="prog.log", level=logging.DEBUG)
    sys.exit(main(path))
