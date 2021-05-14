import logging
from collections import OrderedDict


def ordre(dico):
    dico_ord={}
    new_dico = OrderedDict(sorted(dico.items(), key=lambda t: t[0]))
    return new_dico
    

def somme(dico_minute):
    """
    cette fonction reprend la liste des temps des actions 
    et les aditionne afin d'en avoir un temps total en minute 
    pour chaque actions
    les valeurs sont ici exprimée en liste de int
    """
    logging.info("lancement de la fonction somme")
    for key, valeur in dico_minute.items():
        dico_minute[key] = [sum(valeur)]
        logging.info(valeur)
        logging.info(type(valeur))
    return dico_minute


def change_values(minutes):
    """
    cette fonction transforme le type des valeur
    de liste de int en liste de str
    """
    for key, valeur in minutes.items():
        for j in valeur:
            j = str(j)
        minutes[key] = [j]
    return minutes


def total_time(log_minutes):
    """
    cette fonction prend les valeurs et en calcul le total
    """
    logging.info("ouverture de la fonction total_time")
    total = 0
    for key, valeur in log_minutes.items():
        total += int("".join(valeur))
    logging.info(f"return {total}")
    return total


def pourcentage(minutes):
    """
    à l'aide du total calculer precedement cette fonction 
    calcul pour chaque action les pourcentage de temps passer 
    à l'executer sur l'ensembles des exercices
    """
    logging.info("ouverture fonction pourcentage")
    total = total_time(minutes)
    for valeur in minutes.values():
        a = int("".join(valeur))
        p = int(a / total * 100)
        valeur += [str(p)]
    return minutes
