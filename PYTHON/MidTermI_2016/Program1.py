import sys
import re
Seq=""
DNA=open("Seq_BLAST.fasta", "r")
for Line in DNA:
  if("M" in Line):
    Seq=Seq+Line.strip()
DNA.close()
MyRe="r[M]{1}"
MyRegex=re.compile(MyRe)
MyRes2=MyRegex.search(Seq)
MyRes2.count("M")
