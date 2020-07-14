from Bio import ExPASy, SeqIO

def RecupererSwissProt(identifiant):
    
    handle = ExPASy.get_sprot_raw(identifiant)
    record = SeqIO.read(handle,'swiss')
    choix = 0
    while choix!= 5 :
        print("-----------------Lecture et Affichage------------------")
        print("Que voulez-vous afficher?")
        print("1 : Le nom")
        print("2 : La séquence")
        print("3 : La description")
        print("4 : Les mots-clés")
        print("5 : Quitter l'affichage")
        choix = int(input("Entrez votre choix : "))
        if choix == 1 :
            # Affiher le nom de la séquence
            print(record.name)
        elif choix == 2 :
            # Afficher la séquence complète
            print(record.seq)
        elif choix == 3 :
            # Afficher la description de la séquence
            print(record.description)
        elif choix == 4 :
            # Afficher les mots-clés du fichier GenBank
            print(record.annotations['keywords'])
        elif choix != 5:
            print("Erreur de choix")
    print("--------------------------------------------------------------------------------")
def programme():
    
    identifiant = input("Entrez l'identifiant SwissProt: ")
    RecupererSwissProt(identifiant)

if __name__ == '__main__':
    
    programme()
    
    