NucFrq=[0.4,0.3,0.2,0.1]
Probability_HindIII=NucFrq[0]**2*NucFrq[2]*NucFrq[1]*NucFrq[3]**2
print ("The probability of HindII site in the genome is: ", Probability_HindIII)
Number_HindIII_sites=Probability_HindIII*(3.4*10**9)
print("The number of HindIII sites in the genome is: ", Number_HindIII_sites)
