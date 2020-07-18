from Bio import SeqIO, ExPASy 
from Bio import SwissProt
class GetEntreeSwiss: 
    def __init__(self, ident, ext):
        self.ident = ident
        self.ext = ext

    def getSwissProtFile(self):
        handle = ExPASy.get_sprot_raw(self.ident)
        return SeqIO.read(handle, self.ext)

    def getName(self): 
        return self.getSwissProtFile().name
    
    def getSequence(self): 
        return self.getSwissProtFile().seq
    
    def getDescription(self): 
        return self.getSwissProtFile().description
    
    def getKeyWords(self): 
        return self.getSwissProtFile().annotations['keywords']

swiss = GetEntreeSwiss('Q13572', 'swiss')
swiss.getSwissProtFile()       

