class Funcionario:
    def __init__(self, nome, salario, idade):
        self.nome = nome
        self.salario = salario
        self.idade = idade

    def __repr__(self):
        return f"{self.nome} | R${self.salario:.2f} | {self.idade} anos"


def particionar_obj(arr, baixo, alto, comparar):
    pivo = arr[alto]
    i = baixo - 1
    for j in range(baixo, alto):
        if comparar(arr[j], pivo) <= 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

def quicksort_obj(arr, baixo, alto, comparar):
    if baixo < alto:
        p = particionar_obj(arr, baixo, alto, comparar)
        quicksort_obj(arr, baixo, p - 1, comparar)
        quicksort_obj(arr, p + 1, alto, comparar)

def comparar_funcionario(a, b):
    if a.salario != b.salario:
        return b.salario - a.salario
    if a.nome < b.nome:
        return -1
    if a.nome > b.nome:
        return 1
    return 0


funcionarios = [
    Funcionario("Carlos",   5200.0, 34),
    Funcionario("Ana",      8100.0, 29),
    Funcionario("Bruno",    3400.0, 41),
    Funcionario("Diana",    8100.0, 36),
    Funcionario("Eduardo",  6700.0, 45),
    Funcionario("Fernanda", 3400.0, 28),
    Funcionario("Gabriel",  9500.0, 52),
    Funcionario("Helena",   5200.0, 31),
    Funcionario("Igor",     7300.0, 38),
    Funcionario("Julia",    4100.0, 26),
    Funcionario("Kevin",    6700.0, 33),
    Funcionario("Laura",    9500.0, 47),
    Funcionario("Marcos",   4800.0, 39),
    Funcionario("Natalia",  5200.0, 30),
    Funcionario("Otto",     3900.0, 44),
]

quicksort_obj(funcionarios, 0, len(funcionarios) - 1, comparar_funcionario)

print("Funcionários ordenados (salário desc, nome asc):\n")
for f in funcionarios:
    print(f)