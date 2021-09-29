Filme1 = {
    "Super-Homem": "Clark Kent"
}
Filme2= {
    "Homem-Aranha": "Tobey Maguire"
}
Filme3 = {
    "Homem de Ferro": "Tony Stark"
}
Filme4 = {
    "Hulk": "Bruce Banner"
}
Filme5 = {
    "Mercúrio": "Pietro Maximoff"
}

Filmes = {
    "Super-Homem": Filme1,
    "Homem-Aranha": Filme2,
    "Homem de Ferro 3": Filme3, 
    "O incrível Hulk": Filme4,
    "Os Vingadores": Filme5 
}
escolhaFilme = input("Escolha um filme: {} ".format(Filmes.keys()))

if escolhaFilme in Filmes:
    escolhaNome = input("Deseja saber o nome ou a identidade do herói de {}? ".format(escolhaFilme)).lower()
else:
    print("Este filme não é válido.")

if escolhaNome == "nome":
    print("O nome do herói é {}.".format(Filmes(escolhaFilme.keys())))

if escolhaNome == "identidade":
    print("A identidade do herói é {}.".format(Filmes(escolhaFilme.items())))