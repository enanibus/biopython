Seq=""
MyFile=open("HIF1A.fasta","r")
for Line in MyFile:
    if not(">" in Line):
      Seq=Seq+Line.strip()
MyFile.close()
REnz={"SALI":"GTCGAC","XBAI":"TCTAGA","BPI1":"GAAGAC","ECORI":"GAATTC","XHOI":"CTCGAG"}
print(Seq.count("GAATTC"))
