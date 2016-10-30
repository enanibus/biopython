NucFrq={"A":0.35,"C":0.25,"G":0.3,"T":0.2}
Probability_EcoRI=(NucFrq["G"]*(NucFrq["A"]**2)*(NucFrq["T"]**2)*NucFrq["C"])
print("The probability of the EcoRI site to be in the genome is",Probability_EcoRI)
Number_EcoRI_Sites=Probability_EcoRI*270000
print("The number of EcoRI sites in the genome is: ", Number_EcoRI_Sites)

