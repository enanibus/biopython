Original_symbols='ATCG'
Secret_code='AUCG'
Trans_table=str.maketrans(Original_symbols,Secret_code)
MySeq='ACGTGG'
Coded_message=MySeq.translate(Trans_table)
Coded_message
print


