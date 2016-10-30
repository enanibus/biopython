def Media (NumberList):
        suma=0
        for n in NumberList:
                suma=suma+n
        result=suma/len(NumberList)
        return(result)

Weight4Bq=[70,47,68,56,87,49,48,71,65,62]
AverageWeight4Bq=Media(Weight4Bq)
print(AverageWeight4Bq)
