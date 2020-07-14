""" -------------------Récupérer une Entrée Prosite --------------------------"""
from Bio import ExPASy 
from Bio.ExPASy import Prosite

def RecupererEntreeProsite(ident):
    
    handle = ExPASy.get_prosite_raw(ident)
    record = Prosite.read(handle)
    print("----------Lecture et affichage entrée Prosite ------")
    choix = str()
    while choix != '5':
        print("Que voulez vous afficher?")
        print("1:Le nom")
        print("2:le type")
        print("3:La description")
        print("4:La signature si l'entrée est une signature ou le profile si l'entrée est un profile")
        print("5:Pour Quitter")
        choix = input("Entrez votre choix:")
        if choix == '1':
            print("Le nom est: ",record.name)
        elif choix == '2':
            print("le type est: ",record.type)
        elif choix == '3':
            print("la description est: ",record.description)
        elif choix == '4':
            if record.type == 'MATRIX':
                print("L'entrée est une matrice, la matrice est: ",record.matrix)
            elif record.type == 'PATTERN':
                print("L'entée est une signature, La signature est: ",record.pattern)
        elif choix != '5':
            print("erreur de choix !")
        print("-----------------------------------------------------------")
def programme():
    
    numero_acc = input("Entrez le numéro d'accession correspondant à l'entrée Prosite: ")
    RecupererEntreeProsite(numero_acc)
    
if __name__ == '__main__':
    programme()
    