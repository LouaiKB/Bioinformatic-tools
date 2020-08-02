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
    
    def getAccessionNumber(self): 
        try: 
            return self.getPrositeEntree().accession
        except IOError: 
            return 'Not Found!'
    
    def getOccurenceNumber(self): 
        try:
            return self.getPrositeEntree().nr_total
        except IOError: 
            return 'Not Found!'
    
class GetEntreeSwiss: 
    def __init__(self, ident):
        self.ident = ident

    def getSwissProtFile(self):
        try:
            handle = ExPASy.get_sprot_raw(self.ident)
            return SwissProt.read(handle)
        except IOError: 
            return 'Not Found!'
        except AssertionError: 
            return 'Page contains more than one record!'

    def getOrganism(self):
        try:
            return self.getSwissProtFile().organism
        except IOError: 
            return 'Not Found!'
        except AssertionError:
            return 'Page contains more than one record!'

    def getGeneName(self):
        try:
            return self.getSwissProtFile().gene_name
        except IOError: 
            return 'Not Found!'
        except AssertionError:
            return 'Page contains more than one record!'

    def getName(self): 
        try:
            return self.getSwissProtFile().entry_name
        except IOError: 
            return 'Not Found!'
        except AssertionError:
            return 'Page contains more than one record!'

    def getSequence(self): 
        try:
            return self.getSwissProtFile().sequence
        except IOError: 
            return 'Not Found!'
        except AssertionError:
            return 'Page contains more than one record!'
    
    def getDescription(self): 
        try:
            return self.getSwissProtFile().description
        except IOError: 
            return 'Not Found!'
        except AssertionError:
            return 'Page contains more than one record!'

    def getKeyWords(self): 
        try:
            return self.getSwissProtFile().keywords
        except IOError: 
            return 'Not Found!'
        except AssertionError:
            return 'Page contains more than one record!'
    
    def getAccessions(self):
        try:
            return self.getSwissProtFile().accessions
        except IOError: 
            return 'Not Found!'
        except AssertionError:
            return 'Page contains more than one record!'
    
    def getAnnotationUpdate(self):
        try:
            return self.getSwissProtFile().annotation_update
        except IOError: 
            return 'Not Found!'
        except AssertionError:
            return 'Page contains more than one record!'
        
    def dataClass(self):
        try:
            return self.getSwissProtFile().data_class
        except IOError: 
            return 'Not Found!'
        except AssertionError:
            return 'Page contains more than one record!'
        
            