import re
MySeq=""
DNA=open("ID1001.fasta","r")
for Line in DNA:
  if not(">" in Line):
    MySeq=MySeq+Line.strip()
DNA.close()
MyRE=r"[DE][AVLI]\w{0,1}[^AQWSTCDERF]"
MyRegex=re.compile(MyRE)
def SearchAll (Regex,Seq,pos):
  Res=Regex.search(Seq,pos)
  if Res==None:
    return()
  else:
    print(Res.group(),"\t",Res.start(),"\t",Res.end())
    SearchAll(Regex,Seq,Res.start()+1)
SearchAll(MyRegex,MySeq,0)
