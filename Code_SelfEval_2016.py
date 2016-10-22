import re
Seq=""
MySeq=open("ID1001.fasta","r")
for Line in MySeq:
  if not(">" in Line):
    Seq=Seq+Line.strip()
MySeq.close()
MyRE=r"[D,E]-[A,V,L,I]-x(0,1)-{AQWSTCDERF}"
MyRegex=re.compile(MyRE)
def SearchAll (Regex,Seq,pos):
  Res=Regex.search(Seq,pos)
  if Res==None:
    return()
  else:
    print(Res.group(),"\t",Res.start(),"t",Res.end())
    SearchAll(Regex,Seq,Res.start()+1)
SearchAll(MyRegex,MySeq,0)
