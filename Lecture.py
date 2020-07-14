from Bio import SeqIO 
from Bio.SeqRecord import SeqRecord

def LireFasta():
    
    print("----------------- Lecture & Affichage-------------")
    path = input("Entrez le chemain du fichier Fasta: ")
    record = SeqIO.parse(path, 'fasta')
    L = list()
    for i in record:
        L.append(i)
    L = SeqRecord(L)
    choix = 0
    while choix!= 3 :
        print("Que voulez-vous afficher?")
        print("1 : Le nom")
        print("2 : La séquence")
        print("3 : Quitter l'affichage")
        choix = int(input("Entrez votre choix : "))
        if choix == 1:
            j = 0
            for i in L:
                print("Le nom de la " + str(j+1) + "ème séquence du fichier FASTA est: ", i.name)
                j = j + 1
            print("-------------------------------------------------------")
        elif choix == 2:
            j = 0
            for i in L:
                print("la " + str(j+1) + "ème séquence du fichier FASTA est: ", i.seq)
                j = j + 1
            print("-------------------------------------------------------")   
    print("-------------------------------------------------------")
    
def LireGenbank():
    try:
        print("------------------------------ Lecture & Affichage -----------------------------")
        # Demande du chemin du fichier à l'utilisateur
        chemin = input("Entrez le chemin du fichier à lire : ")
        # Lecture du fichier GenBank
        record = SeqIO.read(chemin, "genbank")
        
        #Afficher le contenu selon les options choisies par l'utilisateur
        choix = 0
        while choix!= 5 :
            print("-------------------------------------------------------")
            print("Que voulez-vous afficher?")
            print("1 : Le nom")
            print("2 : La séquence")
            print("3 : La description")
            print("4 : Les mots-clés")
            print("5 : Quitter l'affichage")
            choix = int(input("Entrez votre choix : "))
            if choix == 1 :
                # Affiher le nom de la séquence
                print('le nom de la séquence est : ',record.name)
            elif choix == 2 :
                # Afficher la séquence complète
                print('la séquence est : ',record.seq)
            elif choix == 3 :
                # Afficher la description de la séquence
                print('La description est :',record.description)
            elif choix == 5 :
                # Afficher les mots-clés du fichier GenBank
                print('les mots clés sont:',record.annotations['keywords'])
            elif choix != 5:
                print("Erreur de choix")
            print("--------------------------------------------------------------------------------")
    except:
        print("Erreur de choix! veuillez répéter")
def LireSwissProt():
    try:
        print("------------------------------ Lecture & Affichage -----------------------------")
        # Demande du chemin du fichier à l'utilisateur
        chemin = input("Entrez le chemin du fichier à lire : ")
        # Lecture du fichier GenBank
        record = SeqIO.read(chemin, "swiss")
        
        #Afficher le contenu selon les options choisies par l'utilisateur
        choix = 0
        while choix!= 6 :
            print("--------------------------------------------------------")
            print("Que voulez-vous afficher?")
            print("1 : Le nom")
            print("2 : La séquence")
            print("3 : La description")
            print("4 : Le type de la molécule")
            print("5 : Les mots-clés")
            print("6 : Quitter l'affichage")
            choix = int(input("Entrez votre choix : "))
            if choix == 1 :
                # Affiher le nom de la séquence
                print('le nom de la séquence est : ',record.name)
            elif choix == 2 :
                # Afficher la séquence complète
                print('la séquence est : ',record.seq)
            elif choix == 3 :
                # Afficher la description de la séquence
                print('La description est :',record.description)
            elif choix == 4 :
                # Afficher le type de la molécule
                print(record.annotations['molecule_type'])
            elif choix == 5 :
                # Afficher les mots-clés du fichier GenBank
                print('les mots clés sont:',record.annotations['keywords'])
            elif choix != 6:
                print("Erreur de choix")
            print("-----------------------------------------------------------------")
    except:
        print("Erreur de choix! veulliez répéter ")

def Programme():
    try:
        print("Quelle est le type du fichier à lire ?")
        print("a:FASTA")
        print("b:GenBank")
        print("c:SwissProt")
        choix = input("Entrez votre choix: ")
        if choix == 'a':
            LireFasta()
            
        elif choix == 'b':
            LireGenbank()
        
        elif choix == 'c':
            LireSwissProt()
    except:
        print("Erreur de choix! répétez SVP")
if __name__ == '__main__':
    Programme()