class DNA3:
    """Generates an object of class DNA"""
    def __init__(self,Sequence=""):
        self.Seq=Sequence.upper()
    def RevCompl(self):
        """Computes the reverse-complement of the sequence"""
        rcSeq=""
        Complement={"A":"T","C":"G","G":"C","T":"A"}
        for base in self.Seq:
            rcSeq=Complement[base]+rcSeq
        return(rcSeq)
    def Translate(self,frame=0):
        if frame>2:print("Legal frames: 0,1,2");return
        """Returns translation at the indicated frame.
        Note that frames are 0,1 and 2"""
        stdGC={"TTT":"F","TTC":"F","TTA":"L","TTG":"L","CTT":"L","CTC":"L","CTA":"L","CTG":"L","ATT":"I","ATC":"I","ATA":"I","ATG":"M","GTT":"V","GTC":"V","GTA":"V","GTG":"V","TCT":"S","TCC":"S","TCA":"S","TCG":"S","CCT":"P","CCC":"P","CCA":"P","CCG":"P","ACT":"T","ACC":"T","ACA":"T","ACG":"T","GCT":"A","GCC":"A","GCA":"A","GCG":"A","TAT":"Y","TAC":"Y","TAA":"*","TAG":"*","CAT":"H","CAC":"H","CAA":"Q","CAG":"Q","AAT":"N","AAC":"N","AAA":"K","AAG":"K","GAT":"D","GAC":"D","GAA":"E","GAG":"E","TGT":"C","TGC":"C","TGA":"*","TGG":"W","CGT":"R","CGC":"R","CGA":"R","CGG":"R","AGT":"S","AGC":"S","AGA":"R","AGG":"R","GGT":"G","GGC":"G","GGA":"G","GGG":"G"}
        prot=""
        for pos in range(frame,len(self.Seq),3):
            if (len(self.Seq[pos:pos+3])<3):return(prot)
            prot=prot+stdGC[self.Seq[pos:pos+3]]
        return(prot)
    
