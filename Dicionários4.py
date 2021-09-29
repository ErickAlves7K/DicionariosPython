tamanhos = {
    "Erick": 42,
    "Lucas": 43,
    "Pedro": 41,
    "Marco": 42,
    "Miguel": 39
}
nome = input("Informe o nome do aluno ").strip()

if nome in tamanhos:
    print("O tamanho do calçado é {}".format(tamanhos.get(nome)))
else:
    print("Este aluno não existe.")