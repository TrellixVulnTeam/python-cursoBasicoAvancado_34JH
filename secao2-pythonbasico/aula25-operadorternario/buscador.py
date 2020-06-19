class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
            return -1

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista)-1
        while primeiro <= ultimo:
                meio = (primeiro+ultimo)//2
                if lista[meio] == x:
                    return meio
                else:
                    if x <lista[meio]:
                        ultimo = meio -1
                    else:
                        primeiro = meio + 1
        return -1

#testes
lista = [-100, 0, 20,30, 50,100,3000,5000]
print(lista)
b = Buscador()
b.busca_binaria(lista, 100)
b.busca_binaria(lista, 0)
b.busca_binaria(lista, -100)
b.busca_binaria(lista, 5000)
len(lista)
b.busca_binaria(lista, 7000)
b.busca_binaria(lista, 70)