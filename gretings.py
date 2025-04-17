nom = input("Bonjour, donnez moi votre nom pour commencer s'il vous plait")
prenom = input("votre prénom s'il vous plait")
sexe = input("et enfin votre genre s'il vous plait (h/f)")
if sexe == "h":
    print("Enchanté Monsieur " + nom + " " + prenom + ".")
elif sexe == "f":
    print("Enchanté Madame " + nom + " " + prenom + ".")
else:
    print("Je ne reconnais pas votre sexe verifier que vous avez bien mis f si vous êtes de genre féminin et m si vous etes de genre masculin ")
