MySeq="ACGTGG"
TransTable=str.maketrans("AGCT","TCGA")
revMySeq=MySeq[::-1]
revcomplMySeq=revMySeq.translate(TransTable)
print("Your reverse complement sequence is: ", revcomplMySeq)
