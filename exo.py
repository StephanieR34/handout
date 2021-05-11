import logging

logging.basicConfig(filename="exo.log",level=logging.DEBUG)

# def somme(dico_minute):
#     #logging.info("lancement de la fonction somme")
#     for key,valeur in dico_minute.items():
#         a=0
#         logging.info(f"print valeur = {valeur}")
#         logging.info(type(valeur))
#         for m in valeur:
#             logging.info(f"print m ={m}")
#             logging.info(type(m))
#             a += m
#             logging.info(a)
#             logging.info(type(a))
    
#         dico_minute[key]=[a]
    
#     return dico_minute

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

# def somme(dico_minute):
#     #logging.info("lancement de la fonction somme")
#     for key,valeur in dico_minute.items():
#         valeur=sum(valeur)
#         dico_minute[key]=[str(valeur)]
#         logging.info(valeur)
#         logging.info(type(valeur))
    
#     return dico_minute
          
print(change_values(somme({'Exercises': [15, 40, 80], 'Break': [20, 10], 'Lunch Break': [60]})))
#print(somme({'Exercises': [15, 40, 80], 'Break': [20, 10], 'Lunch Break': [60]}))