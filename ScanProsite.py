from Bio import ExPASy
from Bio.ExPASy import Prosite,ScanProsite 
from Bio import SeqIO

def LireFASTA(ch):
    fi = SeqIO.read(ch,'fasta')
    return str(fi.seq)

def ScanSequence(sequ):
    handle = ScanProsite.scan(seq = sequ)
    result = ScanProsite.read(handle)
    return result

def RecupérerEntreeProsite(acc):
    handle = ExPASy.get_prosite_raw(acc)
    record = Prosite.read(handle)
    return record 

def programme():
    chemin = input("Introduire le chemin du fichier FASTA:")
    seque = LireFASTA(chemin)
    li = ScanSequence(seque)
    if len(li) != 0:
        for i in range(0,len(li)):
            a = li[i]['signature_ac']
            recc = RecupérerEntreeProsite(a)
            print('Le nom du '+ str(i)+' ème motif est:',recc.name)
            print('Le type du '+ str(i)+' ème motif est:',recc.type)
            print('Le numéro daccession du '+ str(i)+' ème motif est:',recc.accession)
            print('La documentation du '+ str(i)+' ème motif est:',recc.name)
            print("Le numéro d'occurence "+ str(i)+' ème motif est:',recc.nr_total)
    
    else:
        print("c'est une liste vide")
if __name__ =='__main__':
    programme()
    
    
    
    
    
    
    
    
