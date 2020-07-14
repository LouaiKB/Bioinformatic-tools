import Fragmentation
import TrouverSignatures
import ScanProsite
import Interaction_PDB
import AlignementGlobLoc
import NCBI
import Lecture
import Recuperer_SwissProt
import RecupererEntreeProsite
import TraductionSignatureProsite


choix = str()
while (choix != 'Q'):
    try:    
        print('------------ Bonjour --------------')
        print('Que ce que voulez vous faire?')
        print('1:Lire un fichier FASTA, GenBank, SwissProt')
        print('2:Faire une recherche NCBI')
        print('3:Récupérer une entrée SwissProt')
        print('4:faire un alignement global ou local')
        print('5:Fragmenter une séquence en sous séquences')
        print('6:Récupérer et afficher une entrée Prosite ')
        print("7:Lancer un scan avec l'outil ScanProsite et afficher les motifs trouvés")
        print('8:Traduire une signature Prosite en une expréssion Python')
        print('9:Vérifier si une signature existe dans une séquence')
        print('10:Télécharger une entrée PDB puis afficher cette entrée ou non selon votre choix ')
        print("Q: Pour Quitter")
        choix = input("Entrez votre choix: ")
        if choix == '1':
            Lecture.Programme()
        
        elif choix == '2':
            NCBI.programme()
    
        elif choix == '3':
            Recuperer_SwissProt.programme()
            
        elif choix == '4':
            AlignementGlobLoc.programme()
        
        elif choix == '5':
            Fragmentation.programme()
    
        elif choix == '6':
            RecupererEntreeProsite.programme()
    
        elif choix == '7':
            ScanProsite.programme()
    
        elif choix == '8':
            TraductionSignatureProsite.programme()
        
        elif choix == '9':
            TrouverSignatures.program()
        
        elif choix == '10':
            Interaction_PDB.programme()

    except:
        print("Erreur de choix\nVeuillez répétez!")
input()
            
        
        
            
            
            
            
