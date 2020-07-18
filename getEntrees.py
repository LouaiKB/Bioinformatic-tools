from Bio import ExPASy, SwissProt
from Bio.ExPASy import Prosite

class GetEntreeProsite: 
    def __init__(self, ident):
        self.ident = ident

    def getPrositeEntree(self):
        try: 
            handle = ExPASy.get_prosite_raw(self.ident)
            return Prosite.read(handle)
        except ConnectionError:
            return "No connection!"
        except IOError: 
            return "No connection!" 
    def getName(self):
        try: 
            return self.getPrositeEntree().name
        except IOError: 
            return "Not Found!"

    def getPrositeType(self):
        try:
            return self.getPrositeEntree().type
        except IOError:
            return "Not Found!"
        
    def getDescription(self):
        try: 
            return self.getPrositeEntree().description
        except IOError: 
            return "Not Found!"

class GetEntreeSwiss: 
    def __init__(self, ident, ext):
        self.ident = ident
        self.ext = ext

    def getSwissProtFile(self):
        handle = ExPASy.get_sprot_raw(self.ident)
        return SwissProt.read(handle)

    def getName(self): 
        return self.getSwissProtFile().name
    
    def getSequence(self): 
        return self.getSwissProtFile().seq
    
    def getDescription(self): 
        return self.getSwissProtFile().description
    
    def getKeyWords(self): 
        return self.getSwissProtFile().annotations['keywords']
