#! usr/bin/python3
# Luis del Peso
# Oct 2016
# prueba Biopython for HPBBM

## requires two arguments: file with TF binding sequences and fasta file with sequences to scan

from Bio import SeqIO

for seq_record in SeqIO.parse("MITF_reg.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
    
