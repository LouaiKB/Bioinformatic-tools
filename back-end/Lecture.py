from Bio import SeqIO 
from Bio.SeqRecord import SeqRecord 

class LireFasta: 
    def __init__(self, path, ext): 
        self.path = path 
        self.ext = ext 

    def getFile(self): 
        try:    
            l = []
            for i in SeqIO.parse(self.path, self.ext): 
                l.append(i)
            return SeqRecord(l)
        except FileNotFoundError: 
            return "File not found!"
    
    def getName(self): 
        try: 
            for i in self.getFile(): 
                return i.name + "\n"
        except FileNotFoundError: 
            return "File not found!"
    
    def getSequence(self):
        try:
            for i in self.getFile(): 
                return i.seq + "\n"
        except FileNotFoundError:
            return "File not found!"
 
class LireGenbank:
    def __init__(self, path, ext):
        self.path = path
        self.ext = ext 
    
    def getFile(self):
        try: 
            return SeqIO.read(self.path, self.ext)
        except FileNotFoundError: 
            return "File not found!"

    def getName(self):
        try:
            return self.getFile().name
        except FileNotFoundError: 
            return "File not found!"

    def getSequence(self): 
        try:
            return self.getFile().seq
        except FileNotFoundError: 
            return "File not found!"
    
    def getDescription(self):
        try: 
            return self.getFile().description
        except FileNotFoundError: 
            return "File not found!"

    def getKeyWords(self): 
        try: 
            return self.getFile().annotations['keywords']
        except FileNotFoundError: 
            return "File not found!"

class LireSwissProt(LireGenbank): 
    def __init__(self, path, ext):
        super().__init__(path, ext)

    def moleculeType(self): 
        return self.getFile().annoatations['molecule_type']
