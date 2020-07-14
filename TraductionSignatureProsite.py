from Bio import ExPASy
from Bio.ExPASy import Prosite
import string

def traduireSequence(sign):
    
    sign = sign.replace('-','')
    sign = sign.replace('{','[^')
    sign = sign.replace('}',']')
    sign = sign.replace('(','{')
    sign = sign.replace(')','}')
    sign = sign.replace('x{','(.){')
    sign = sign.replace('x','.')
    alphabet = string.ascii_uppercase
    for i in alphabet:
        sign = sign.replace(i+'{','('+i+')'+'{')
    return sign

def RecupererPattern(ident):
    
    handle = ExPASy.get_prosite_raw(ident)
    record = Prosite.read(handle)
    if record.type == 'PATTERN':
        print("La forme régulière est: ",record.pattern)
        print("La traduction en Python est: ",traduireSequence(record.pattern))
    elif record.type == 'MATRIX':
        print("L'identifiant que vous avez entré correspont à un profile !")

def programme():
    print("---------Traduction des formes régulières en Python ------------")
    choix = str()
    while choix != 'Q':
        print("Comment vous voulez entrez votre forme régulière?")
        print("a: Saisie par le clavier")
        print("b: récupérer la forme régulière à partir de la Base des données Prosite")
        print("Q:Pour quitter le programme")
        choix = input("Entrez votre choix ?: ")
        if choix == 'a':
            signature = input("Entrez votre signature: ")
            print("La signature en python est: ",traduireSequence(signature))
        elif choix == 'b':
            identifiant = input("Entrez le numéro d'accession correspondant: ")
            signature = RecupererPattern(identifiant)
        elif choix != 'Q':
            print("erreur de choix !")
        print("---------------------------------------------------------")
       
if __name__ == '__main__':
    programme()
        