from Bio import SeqIO as sq
from Bio.SeqRecord import SeqRecord
#import os
from Bio import ExPASy

def Lirefasta(path):
    record = sq.parse(path,'fasta')
    l = list()
    for i in record:
        l.append(i)
    l = SeqRecord(l)
    return l 

def RecupereSeqSwissProt(ident):
    handle = ExPASy.get_sprot_raw(ident)
    record = sq.read(handle,'swiss')
    return record        

def fragmentation(tail, sequence, idd, descriptionn,doc):
    if len(sequence)>tail:
        j = 0
        for i in range(0,len(sequence),tail):
            fragment = sequence[i:i+tail]
            fragment = SeqRecord(fragment, id = idd, description = descriptionn)
            sq.write(fragment, doc + str(j+1) +'.fasta','fasta')
            j = j + 1       
    else:
        print("Erreur ! La taille est supérieure à la taille de la séquence")
        
def LireGenbank(path):
    record = sq.read(path,'genbank')
    return record

def programme():
    choix = str()    
    while choix != '4':
        print("--------------------------------------------------------")
        print("Quelle type de séquences voulez vous fragmenter ?")
        print("1: FASTA \n2: SwissProt \n3: Genbank \n4: Quitter")
        choix = input("Entrez votre choix:")
        if choix == '1':
            print("---Fragmenter des séquences des fichiers fasta---")
            chemain = input("Entrez le chemain du fichier fasta: ")
            record = Lirefasta(chemain)
            taille =  int(input("Entrez la taille des sous-fragments: "))
            j = 0
            #print("Vos fichiers seront enregistrés dans le Disque dure E")
            #os.makedirs("E:\\fichiersFasta\\")
            dossier = input("Entrez le chemain pour sauvegarder les sous fragments: ")
            for i in record:
                chemain = dossier + str(j+1) 
                fragmentation(taille, i.seq, i.id, i.description,chemain)
                j = j + 1
            print("Les fichiers Sont enregistrés avec succés !")
        elif choix == '2':
            print("---Fragmenter des séquences récupérées de SwissProt---")
            acc = input("Entrez l'identifiant correspondant: ")
            recordd = RecupereSeqSwissProt(acc)
            sequence = recordd.seq
            identif = recordd.id
            taille =  int(input("Entrez la taille des sous-fragments: "))
            dossier = input("Entrez le chemain pour sauvegarder les sous fragments: ")
            fragmentation(taille, sequence, identif, recordd.description,dossier)
            print("Les fichiers Sont enregistrés avec succés !")
        elif choix == '3':
            print("--------Fragmenter des séquences Genbank-------")
            ch = input("Entrez le chemain du fichier Genbank: ")
            recordgb = LireGenbank(ch)
            taille =  int(input("Entrez la taille des sous-fragments: "))
            dossier = input("Entrez le chemain pour sauvegarder les sous fragments: ")
            fragmentation(taille, recordgb.seq, recordgb.id, recordgb.description,ch)
            print("Les fichiers Sont enregistrés avec succés !")
    print("Au revoir !")
if __name__ == '__main__':
    programme()
   
    
    
    
    
    
    
    
    
    
    
    
    
