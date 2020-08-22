from Bio.PDB import PDBList as pdbl 
from Bio.PDB import PDBParser as pdbp 
import os

def Téléchargé(idd,chemin):
    
    pdb = pdbl()
    path = pdb.retrieve_pdb_file(idd ,pdir = chemin) 
    #Overwrite c'est pour ecraser le fichier existant
    return path 

def LireEntrée(idd,ch):
    
    parser = pdbp(PERMISSIVE = 1)
    structure = parser.get_structure(idd,ch)
    return structure 

def Afficher(struct):
    
    print("le titre de l'entrée est {}".format(struct.header['name']))
    print("la méthode expérimentale utilisée est {}".format(struct.header['structure_method']))
    
    models = struct.get_list()
    print("Le nombre des modèles est {}".format(len(models)))
    
    chains = models[0].get_list()
    print("le nombre des chains dans le premier model est {}".format(len(chains)))
    
    for i in range(len(chains)):
        residus = chains[i].get_list()
        print("le nombre des résidus dans la chaine "+ chains[i].get_id() +" est {}".format(len(residus)))
    
    atom = 0
    for i in residus:
        atom = atom + len(i.get_list())
    
    print("le nombre totales d'atomes est {}".format(atom))
        
def programme():
    
    name = input("Comment voulez vous nommer le fichier: ")
    chemain = "C:\\"+name+"\\"
    os.makedirs(chemain)
    identifiant = input("Entrez l'identifiant:")   
    pathh = Téléchargé(identifiant, chemain)
    print("----Votre fichier a été téléchargé avec succés ----")
    x = input(" voulez vous lire votre fichier (oui/non): ")
    if x == 'oui':
        struct = LireEntrée(identifiant, pathh)
        Afficher(struct)
    elif x == 'non':
        print("ok!")
        
if __name__ == '__main__':
    
    programme()
    
    
    
    
    
    
    
        
    
        
    

    
    
    
    