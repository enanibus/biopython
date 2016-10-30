MySeq="ACGTGG"
TransTable=str.maketrans("AGCT","TCGA")
complMySeq=MySeq.translate(TransTable)
print(complMySeq)
