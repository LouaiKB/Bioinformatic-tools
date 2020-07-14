from Bio import pairwise2
from Bio.SubsMat import MatrixInfo
from Bio import SeqIO
from Bio import ExPASy

def RecupererEntreeSwissProt(ident):
    
    handle = ExPASy.get_sprot_raw(ident)
    record = SeqIO.read(handle,'swiss')
    return record.seq
        
def Alignement_Global(seq1, seq2, matrice, alpha, beta):
    return pairwise2.align.globalds(seq1, seq2, matrice, alpha, beta, one_alignment_only = True)

def Alignement_Local(seq1, seq2, matrice, alpha, beta):
    return pairwise2.align.localds(seq1, seq2, matrice, alpha, beta, one_alignment_only = True)

def Lire_Sequence(chemin):
    fichier = SeqIO.read(chemin, 'fasta')
    return(str(fichier.seq))

def programme():
    # Lire la première séquence à partir d'un fichier fasta
    print("Comment voulez vous récupérer les 2 séquences?")
    print("a: A partir des fichiers Fasta existant")
    print("b: Récupérer les séquences à partir de SwissProt")
    choise = input("Entrez votre choix ?: ")
    
    if choise == 'a':
        chemin = input("Entrez le chemin de la première séquence : ")
        seq1 = Lire_Sequence(chemin)
        # Lire la deuxième séquence à partir d'un fichier fasta
        chemin = input("Entrez le chemin de la deuxième séquence : ")
        seq2 = Lire_Sequence(chemin)
        # Lire le choix de l'alignement
        print("Quel type d'alignement voulez-vous faire?")
        choixA = int(input("1:Alignement Global \n2:Alignement Local \nEntrez votre choix : "))
        # Lire les pénalités alpha et beta
        alpha = int(input("Entrez la pénalité alpha : "))
        beta = int(input("Entrez la pénalité beta : "))
        # Cas de l'alignement global
        if choixA == 1:
            # Lire le choix de la matrice
            choixM = 0
            while choixM != 6:
                print('Quel type de matrice voulez-vous utiliser?')
                choixM = int(input("1:PAM30; \n2:PAM90; \n3:PAM250 \n4:BLOSUM30 \n5:BLOSUM62 \n6:Quitter \nEntrez votre choix : "))
                if choixM == 1: # Choix de la matrice PAM30
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.pam30, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 2: # Choix de la matrice PAM90
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.pam90, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 3 :# Choix de la matrice PAM250
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.pam250, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 4: # Choix de la matrice BLOSUM30
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.blosum30, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 5: # Choix de la matrice BLOSUM62
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.blosum62, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM != 6:
                    print("Erreur de saisie")
        # Cas de l'alignement local
        elif choixA == 2:
            # Lire le choix de la matrice
            choixM = 0
            while choixM != 6:
                print('Quel type de matrice voulez-vous utiliser?')
                choixM = int(input("1:PAM30 \n2:PAM90 \n3:PAM250 \n4:BLOSUM30 \n5:BLOSUM62 \n6:Quitter \nEntrez votre choix : "))
                if choixM == 1: # Choix de la matrice PAM30
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.pam30, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 2: # Choix de la matrice PAM90
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.pam90, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 3 :# Choix de la matrice PAM250
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.pam250, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 4: # Choix de la matrice BLOSUM30
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.blosum30, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 5: # Choix de la matrice BLOSUM62
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.blosum62, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM != 6:
                    print("Erreur de saisie")
        else:
            print("Erreur de saisie")
    elif choise == 'b':
        ident1 = input("Entrez l'identifiant de la première séquence: ")
        ident2 = input("Entrez l'identifiant de la deuxième séquence: ")
        seq1 = RecupererEntreeSwissProt(ident1)
        seq2 = RecupererEntreeSwissProt(ident2)
        print("Quel type d'alignement voulez-vous faire?")
        choixA = int(input("1:Alignement Global \n2:Alignement Local \nEntrez votre choix : "))
        # Lire les pénalités alpha et beta
        alpha = int(input("Entrez la pénalité alpha : "))
        beta = int(input("Entrez la pénalité beta : "))
        # Cas de l'alignement global
        if choixA == 1:
            # Lire le choix de la matrice
            choixM = 0
            while choixM != 6:
                print('Quel type de matrice voulez-vous utiliser?')
                choixM = int(input("1:PAM30; \n2:PAM90; \n3:PAM250 \n4:BLOSUM30 \n5:BLOSUM62 \n6:Quitter \nEntrez votre choix : "))
                if choixM == 1: # Choix de la matrice PAM30
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.pam30, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 2: # Choix de la matrice PAM90
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.pam90, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 3 :# Choix de la matrice PAM250
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.pam250, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 4: # Choix de la matrice BLOSUM30
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.blosum30, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 5: # Choix de la matrice BLOSUM62
                    alignement = Alignement_Global(seq1, seq2, MatrixInfo.blosum62, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM != 6:
                    print("Erreur de saisie")
        # Cas de l'alignement local
        elif choixA == 2:
            # Lire le choix de la matrice
            choixM = 0
            while choixM != 6:
                print('Quel type de matrice voulez-vous utiliser?')
                choixM = int(input("1:PAM30 \n2:PAM90 \n3:PAM250 \n4:BLOSUM30 \n5:BLOSUM62 \n6:Quitter \nEntrez votre choix : "))
                if choixM == 1: # Choix de la matrice PAM30
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.pam30, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 2: # Choix de la matrice PAM90
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.pam90, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 3 :# Choix de la matrice PAM250
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.pam250, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 4: # Choix de la matrice BLOSUM30
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.blosum30, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM == 5: # Choix de la matrice BLOSUM62
                    alignement = Alignement_Local(seq1, seq2, MatrixInfo.blosum62, alpha, beta)
                    print(pairwise2.format_alignment(*alignement[0]))
                elif choixM != 6:
                    print("Erreur de saisie")
        else:
            print("Erreur de saisie")                
if __name__ == "__main__"    :
    programme()