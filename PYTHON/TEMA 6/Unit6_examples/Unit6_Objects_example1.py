class DNA:
    def __init__(self,Sequence=""):
        self.Seq=Sequence.upper()
    def RevCompl(self):
        rcSeq=""
        Complement={"A":"T","C":"G","G":"C","T":"A"}
        for base in self.Seq:
            rcSeq=Complement[base]+rcSeq
        return(rcSeq)
    
