import statistics


def media (lista):
    med = statistics.mean(lista)
    return round(med,2)

def moda (lista):
    mod = statistics.mode(lista)
    return round(mod,2)


def mediana(lista):
    mediana_2 = statistics.median(lista)
    return round(mediana_2,2)




