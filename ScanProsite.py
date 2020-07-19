from Lecture import LireFasta
from Bio.ExPASy import ScanProsite 
from getEntrees import GetEntreeProsite 

#we will get a sequence from a fasta file 
#we will get an prosite entree

def scanSequence(sequence): 
    handle = ScanProsite.scan(seq=sequence)
    return ScanProsite.read(handle)

path = r'sources\sequence.fasta'

def getMotifs(path):
    fastaSeq = LireFasta(path, 'fasta')
    sequence = fastaSeq.getSequence()
    result = scanSequence(sequence)
    motifs = []
    results = []
    if len(result):
        for i in range(len(result)):  
            a = result[i]['signature_ac']
            motifs.append(a)

        for i in motifs: 
            res = GetEntreeProsite(i)
            results.append({
                'name': res.getName(), 
                'type': res.getPrositeType(), 
                'accession number': res.getAccessionNumber(), 
                'occurence': res.getOccurenceNumber()
            })
        
        return results
    else: 
        return "There is no sequence!" 


  

