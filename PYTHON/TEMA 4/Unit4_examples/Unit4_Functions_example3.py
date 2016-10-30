#! usr/bin/python
# Exercise Unit 4
# Luis del Peso, oct 2016

from Unit4_Functions_example2a import GetDNA
from Unit4_Functions_example2a import SeqStats
from Unit4_Functions_example2a import DigestionTF
from Unit4_Functions_example2a import DigestionPos

def Main():
  DNA=GetDNA(sys.argv[1])
  SeqStats(DNA)
  DigestionTF(DNA)

if __name__=='__main__':
  import sys
  Main()