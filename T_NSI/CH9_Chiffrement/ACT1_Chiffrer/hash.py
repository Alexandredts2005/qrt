import hashlib

def attaque_dico_hash(hash, dic):
    dico = open(dic, mode="r")
    n = 0   # pour compter le nombre de mots

    for mot in dico:
        mot = mot.strip()
        n = n + 1
 
        if hashlib.sha256(mot.encode()).hexdigest() == hash:
            print("TROUVÉ ! Le mot ", mot)
            dico.close()
            return
        
        if n % 1000 == 0:
            print(n, " ", end="")
   
    print(n, " mots ont été testés, mais le hash ne correspond pas.")
    
attaque_dico_hash("11f48731001d3a8e81b2305036b5cb2a19309d7fe86983e05fe16a2cb900e522", "dico.txt")