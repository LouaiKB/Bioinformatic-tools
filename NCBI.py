from Bio import SeqIO
from Bio import Entrez

def LireAfficher():
    print("------------------------------ Lecture & Affichage -----------------------------")
    # Demande du chemin du fichier à l'utilisateur
    chemin = input("Entrez le chemin du fichier à lire : ")
    # Lecture du fichier GenBank
    record = SeqIO.read(chemin, "genbank")

    #Afficher le contenu selon les options choisies par l'utilisateur
    choix = 0
    while choix!= 6 :
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
            print(record.name)
        elif choix == 2 :
            # Afficher la séquence complète
            print(record.seq)
        elif choix == 3 :
            # Afficher la description de la séquence
            print(record.description)
        elif choix == 4 :
            # Afficher le type de la molécule
            print(record.annotations['molecule_type'])
        elif choix == 5 :
            # Afficher les mots-clés du fichier GenBank
            print(record.annotations['keywords'])
        elif choix != 6:
            print("Erreur de choix")
    print("--------------------------------------------------------------------------------")

def ConsulterNet():
    print("------------------------ Recherche en Ligne sur NCBI ---------------------------")
    # Demander l'adresse mail à l'utilisateur
    Entrez.email = input("Entrez votre adresse mail : ")
    # Demander à l'utilisateur le type de la recherche (simple ou avancée)
    print("Quelle recherche voulez-vous effectuer?")
    print("1: Recherche simple")
    print("2: Recherche avancée")
    print("3: Quitter la recherche")
    choix = int(input("Entrez votre choix :"))
    if choix == 1 :
        print("-------------------- Recherche Simple --------------------")
        recherche = input("Entrez les mots de votre recherche : ")
        database = input("Entrez la base des données correspondante (Protein ou nucleotide): ")
        # Faire la recherche dans la base de données nucleotide ou protein avec la fonction esearch
        handle = Entrez.esearch(db = database, term = recherche, rettype = "gb")
        record = Entrez.read(handle)
        # Demander le dossier de sauvegarde des fichiers GenBank à l'utlisateur
        # dossier = input("Entrez le dossier de sauvegarde des fichiers GenBank : ")
        # Pour chaque identifiant des résultats de recherche, on récupère le fichier GenBank correspondant
        for i in range(0,len(record['IdList'])) :
            # On récupère d'abord le résultat de la base de données nucleotide avec la fonction efetch
            handle2 = Entrez.efetch(db = database, id=record['IdList'][i], rettype = "gb", retmode = "text")
            recordd = SeqIO.read(handle2,'gb')
            print(i+1,": Identifiant: ",recordd.id , " Description: ",recordd.description)
        print("-----------------------------------------------------------")
        # après l'affichage du résultat, l'utilisateur doit saisir qu'est ce qu'il veut faire 
        choise = str()
        while choise != '4':
            print("Que voulez vous faire ?")
            print("1: Afficher un résultat")
            print("2: Sauvegarder un résultat")
            print("3: Sauvegarder tous les fichiers")
            print("4: Quitter")
            choise = input("Entrez votre choix: ")
            if choise == '1':
                numbre = int(input("Entrez le numéro du résultat à lire: "))
                # handle_choix permet de lire le fichier récupérer
                handle_choix = Entrez.efetch(db = database, id=record['IdList'][numbre - 1], rettype = "gb", retmode = "text")
                record_choix = SeqIO.read(handle_choix, 'gb')
                print("Le nom est: ",record_choix.name)
                print("---------------------------------------------------")
                print("Le ID est: ",record_choix.id)
                print("---------------------------------------------------")
                print("La Description est: ",record_choix.description)
                print("---------------------------------------------------")
                print("La séquence est: ",record_choix.seq)
                print("---------------------------------------------------")
            elif choise == '2':
                sauv_number = int(input("Entrez le numéro du fichier à sauvegarder: "))
                chemain = input("Entrez le chemain du dossier pour sauvegarder: ")
                handle_sauv =  Entrez.efetch(db = database, id=record['IdList'][sauv_number - 1], rettype = "gb", retmode = "text")
                seq_record_sauv = SeqIO.read(handle_sauv,'gb')
                SeqIO.write(seq_record_sauv, chemain + " f" + str(sauv_number) + ".gb", "genbank") 
                print("Votre fichier a été téléchargé avec succés !")
            elif choise == '3':
                n = 0
                dossier = input("Entrez le dossier de sauvegarde des fichiers genbank: ")
                for i in range(0,len(record['IdList'])) :
                    # On récupère d'abord le résultat de la base de données nucleotide avec la fonction efetch
                    handle21 = Entrez.efetch(db = "nucleotide", id=record['IdList'][i], rettype = "gb", retmode = "text")
                    seq_record = SeqIO.read(handle21, "gb")
                    # On enregistre le fichier GenBank avec la fonction write
                    n = n + SeqIO.write(seq_record, dossier + "f" + str(i+1) + ".gb", "genbank")
                print('Nombre de fichiers GenBank récupérés :', n)
    elif choix == 2 :
        print("-------------------- Recherche Avancée --------------------")
        gene = input("Entrez le nom du gène : ")
        organisme = input("Entrez le nom de l'organisme : ")
        database = input("Entrez la base des données correspondante (Protein ou nucleotide): ")
        # Créer la requête avancée avec le nom du gène et de l'organisme
        terms = gene+"[GENE] AND "+organisme+"[ORGN] AND GenBank[Filter]"
        # Faire la recherche avancée dans la base de données nucleotide avec la fonction esearch
        handle= Entrez.esearch(db = "nucleotide", term = terms, rettype = "gb")
        record = Entrez.read(handle)
        
        for i in range(0,len(record['IdList'])) :
            # On récupère d'abord le résultat de la base de données choisie avec la fonction efetch
            handle2 = Entrez.efetch(db = database, id=record['IdList'][i], rettype = "gb", retmode = "text")
            recordd = SeqIO.read(handle2,'gb')
            print(i+1,": Identifiant: ",recordd.id , " Description: ",recordd.description)
        print("-----------------------------------------------------------")
        choise = str()
        while choise != '4':
            print("-------------------------------------------------------")
            print("Que voulez vous faire ?")
            print("1: Afficher un résultat")
            print("2: Sauvegarder un résultat")
            print("3: Sauvegarder tous les fichiers")
            print("4: Quitter")
            choise = input("Entrez votre choix: ")
            if choise == '1':
                numbre = int(input("Entrez le numéro du résultat à lire: "))
                # handle_choix permet de lire le fichier récupérer
                handle_choix = Entrez.efetch(db = database, id=record['IdList'][numbre - 1], rettype = "gb", retmode = "text")
                record_choix = SeqIO.read(handle_choix, 'gb')
                print("Le nom est: ",record_choix.name)
                print("---------------------------------------------------")
                print("Le ID est: ",record_choix.id)
                print("---------------------------------------------------")
                print("La Description est: ",record_choix.description)
                print("---------------------------------------------------")
                print("La séquence est: ",record_choix.seq)
                print("---------------------------------------------------")
            elif choise == '2':
                sauv_number = int(input("Entrez le numéro du fichier à sauvegarder: "))
                chemain = input("Entrez le chemain du dossier pour sauvegarder: ")
                handle_sauv =  Entrez.efetch(db = database, id=record['IdList'][sauv_number - 1], rettype = "gb", retmode = "text")
                seq_record_sauv = SeqIO.read(handle_sauv,'gb')
                SeqIO.write(seq_record_sauv, chemain + " f" + str(sauv_number) + ".gb", "genbank") 
                print("Votre fichier a été téléchargé avec succés !")
            elif choise == '3':
                n = 0
                dossier = input("Entrez le dossier de sauvegarde des fichiers genban: k")
                for i in range(0,len(record['IdList'])) :
                    # On récupère d'abord le résultat de la base de données nucleotide avec la fonction efetch
                    handle21 = Entrez.efetch(db = "nucleotide", id=record['IdList'][i], rettype = "gb", retmode = "text")
                    seq_record = SeqIO.read(handle21, "gb")
                    # On enregistre le fichier GenBank avec la fonction write
                    n = n + SeqIO.write(seq_record, dossier + "f" + str(i+1) + ".gb", "genbank")
                print('Nombre de fichiers GenBank récupérés :', n)
                print("---------------------------------------------------")
    elif choix != 3 :
        print("Erreur de choix")
    print("--------------------------------------------------------------------------------")
        
def programme():
    choix1 = 0
    while choix1 != 3 :
        print("Bonjour! que voulez-vous faire?")
        print("1 : Lire un fichier Genbank existant")
        print("2 : Faire une recherche en ligne sur NCBI")
        print("3 : Quitter le programme")
        choix1 = int(input("Entrez votre choix : "))
        if choix1 == 1 :
            LireAfficher()
        elif choix1 == 2 :
            ConsulterNet()
        elif choix1 != 3 :
            print("Erreur de choix")
    print("Au revoir et à bientôt")

if __name__ == '__main__':
    programme()
