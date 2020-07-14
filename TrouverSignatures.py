from Bio import SeqIO as sq
import re 
from Bio import ExPASy 
from Bio.ExPASy import Prosite
import TraductionSignatureProsite

def RecupererPattern(ident):
    # la récupération des séquences à partir de la Base des données SwissProt
    handle = ExPASy.get_prosite_raw(ident)
    record = Prosite.read(handle)
    if record.type == 'PATTERN':
        return record.pattern
    elif record.type == 'MATRIX':
        print("L'identifiant que vous avez entré correspont à un profile !")


def LireFasta(ch):
    seqq = sq.parse(ch,'fasta')
    l = []
    for a in seqq:
        l.append(str(a.seq))
    return l

def Verifier(sig,seeq):
    resu = re.search(sig,seeq)
    if resu != None:
        return True
    else:
        return False
def Trouver(sign,sequ):
    res = re.finditer(sign,sequ)
    li = []
    for i in res:
        li.append(i.span())
    return li
        
def program():
    chemin = input('Entrez le chemin du fichier fasta:')
    sequence = LireFasta(chemin)
    choix2 = str()
    while (choix2 != 'Q'):
        
        print("Comment vous voulez entrez votre forme régulière?")
        print("a: Saisie par le clavier")
        print("b: récupérer la forme régulière à partir de la Base des données Prosite")
        choix = input("Entrez votre choix?: ")
        
        if choix == 'a':
            signature = input("Veuillez entrer la signature SVP: ")
            signature_py = TraductionSignatureProsite.traduireSequence(signature)
            print("La séquence traduite est: ",signature_py)
        
        elif choix == 'b':
            acc = input("Entrez Le numéro d'accession corespondant: ")
            signature = RecupererPattern(acc)
            print("La signature récupérée est: ",signature)
            signature_py = TraductionSignatureProsite.traduireSequence(signature)
            print("La signature traduite est: ",signature_py)
        print("--------------------------------------------------------")
            
        for i in range(0,len(sequence)):
            r = Verifier(signature_py,sequence[i])
            if r == True :
                print("Signature trouvée dans la ",i+1," ème séquence et sa position",Trouver(signature,sequence[i]))
            else:
                print("la signature n'exite pas dans la",i+1,"ème séquence")
        
        print("---------------------------------------------------------")
        choix2 = input("Refaire l'opération ? \nO: Oui \nQ: Quitter \nEntrez votre choix :")
        print("---------------------------------------------------------")
if __name__ =='__main__':
    program()
        
    
    