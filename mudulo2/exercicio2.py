def MultpliFunction(numero):
    def multiplicador(multiplicar):
        return numero * multiplicar
    return multiplicador  

s1 = MultpliFunction(10)
s2 = MultpliFunction(10)
s3 = MultpliFunction(10)
print(s1(2))
print(s2(3))
print(s3(4))
