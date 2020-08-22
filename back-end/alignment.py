from Bio.SubsMat import MatrixInfo 
from Bio import pairwise2
"""
    Matrix = {
        PAM30,
        PAM90, 
        PAM250,
        BLOSUM30,
        BLOSUM62
    }

"""
class Alignment:
    def __init__(self, firstSequence, secondSequence, matrix, alpha, beta):
        self.firstSequence = firstSequence
        self.secondSequence = secondSequence
        self.matrix = matrix 
        self.alpha = alpha
        self.beta = beta

    def globalAlignement(self):
        if self.matrix == 'PAM30':
            alignment = pairwise2.align.globalds(
                self.firstSequence,
                self.secondSequence, 
                MatrixInfo.pam30, 
                self.alpha, 
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])
        
        elif self.matrix == 'PAM90':
            alignment = pairwise2.align.globalds(
                self.firstSequence,
                self.secondSequence, 
                MatrixInfo.pam90, 
                self.alpha, 
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])

        elif self.matrix == 'PAM250':
            alignment = pairwise2.align.globalds(
                self.firstSequence,
                self.secondSequence, 
                MatrixInfo.pam250, 
                self.alpha, 
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])

        elif self.matrix == 'BLOSUM30':
            alignment = pairwise2.align.globalds(
                self.firstSequence,
                self.secondSequence, 
                MatrixInfo.blosum30, 
                self.alpha, 
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])

        elif self.matrix == 'BLOSUM62':
            alignment = pairwise2.align.globalds(
                self.firstSequence,
                self.secondSequence, 
                MatrixInfo.blosum62, 
                self.alpha, 
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])

    def localAlignement(self):
        if self.matrix == 'PAM30':
            alignment = pairwise2.align.localds(
                self.firstSequence, 
                self.secondSequence,
                MatrixInfo.pam30,
                self.alpha,
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])

        elif self.matrix == 'PAM90':
            alignment = pairwise2.align.localds(
                self.firstSequence, 
                self.secondSequence,
                MatrixInfo.pam90,
                self.alpha,
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])

        elif self.matrix == 'PAM250':
            alignment = pairwise2.align.localds(
                self.firstSequence, 
                self.secondSequence,
                MatrixInfo.pam250,
                self.alpha,
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])

        elif self.matrix == 'BLOSUM30':
            alignment = pairwise2.align.localds(
                self.firstSequence, 
                self.secondSequence,
                MatrixInfo.blosum30,
                self.alpha,
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])

        elif self.matrix == 'BLOSUM62':
            alignment = pairwise2.align.localds(
                self.firstSequence, 
                self.secondSequence,
                MatrixInfo.blosum62,
                self.alpha,
                self.beta,
                one_alignment_only=True
            )
            return pairwise2.format_alignment(*alignment[0])
