from Bio.PDB import PDBList, PDBParser

class InteractionWithPDB: 
    def __init__(self, ident, path):
        self.ident = ident
        self.path = path

    def retrievePDB(self):
        pdb = PDBList()
        return pdb.retrieve_pdb_file(
            self.ident, 
            pdir=self.path, 
            file_format='pdb', 
            overwrite=True
        )

    def getStructure(self):
        parser = PDBParser(PERMISSIVE=1)
        return parser.get_structure(self.ident, self.retrievePDB())

    def getHeaderName(self):
        return self.getStructure().header['name']

    def getExperimentaleMethod(self):
        return self.getStructure().header['structure_method']
    
    def getModels(self):
        return {
            'models': self.getStructure().get_list(), 
            'number of models': len(self.getStructure().get_list())
        }
    
    def getChains(self):
        models = self.getModels()['models']
        return models[0].get_list()
        """
        else:
            chains = []
            for i in range(len(models)):
                chains.append({
                    'chain': models[i].get_list(),
                    'number of chains': len(models[i].get_list())
                })    
            return chains
        """
    def getResidus(self):
        chains = self.getChains()

        for i in range(len(chains)):
            residus.append({
                'number of residus in the chain ' + str(chains[i]['chain'].get_id()): len(chains[i]['chain'].get_list())
            })
        return residus

path = "C:\\Users\\lenovo\\Desktop"
getpdb = InteractionWithPDB('5ZNF', path)
print(getpdb.getChains())






    