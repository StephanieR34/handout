import logging


def regroupement(liste_minutes):
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


def somme(dico_minute):
    logging.info("lancement de la fonction somme")
    for key, valeur in dico_minute.items():
        dico_minute[key] = [sum(valeur)]
        logging.info(valeur)
        logging.info(type(valeur))
    return dico_minute


def change_values(minutes):
    for key, valeur in minutes.items():
        for j in valeur:
            j = str(j)
        minutes[key] = [j]
    return minutes


def total_time(log_minutes):
    logging.info("ouverture de la fonction total_time")
    total = 0
    for key, valeur in log_minutes.items():
        total += int("".join(valeur))
    logging.info(f"return {total}")
    return total


def pourcentage(minutes):
    logging.info("ouverture fonction pourcentage")
    total = total_time(minutes)
    for valeur in minutes.values():
        a = int("".join(valeur))
        p = round(a / total * 100)
        valeur += [str(p)]
    return minutes
