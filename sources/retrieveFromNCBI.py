from Bio import Entrez, SeqIO

class ResearchFromNcbi: 
    def __init__(self, email, research, database): 
        self.email = email 
        self.research = research 
        self.database = database 
        self.saveNumb = 0 
        self.savingPath = "" 

    def doResearch(self): 
        try: 
            return Entrez.esearch(db=self.database, term=self.research, rettype='genbank')
        except IOError:
            return "No connection!"

    def retrieve(self):
        try: 
            handle = Entrez.read(self.doResearch())
            for i in range(len(handle['IdList'])):
                newHandle = Entrez.efetch(db=self.database, id=handle['IdList'][i], rettype='genbank', retmode='text')
                record = SeqIO.read(newHandle, 'genbank')
                return "Ident: " + record.id + "Description: " + record.description
        except IOError: 
            return "No connection!"

    def saveOneFile(self):
        try: 
            record = Entrez.read(self.doResearch())
            handle = Entrez.efetch(db=self.database, id=record['IdList'][self.saveNumb - 1], rettype='genbank', retmode='text')
            SeqIO.write(SeqIO.read(handle, 'genbank'), self.savingPath + ".gb", 'genbank')
        except IOError: 
            return "No connection!"

    def saveAllFiles(self):
        try:
            record = Entrez.read(self.doResearch())
            for i in range(len(record['IdList'])):
                handle = Entrez.efetch(db=self.database, id=record['IdList'][i], rettype='genbank', retmode='text')
                SeqIO.write(SeqIO.read(handle, 'genbank'), self.savingPath + ".gb", 'genbank')
        except IOError:
            return "No connection!"
