Semana = {}
Semana["Segunda"] = "EF44", "EF44", "RL44", "ET44"
Semana["Terça"] = "RL44", "AE41", "PJ42", "PJ42"
Semana["Quarta"] = "AE41", "ET44", "PR43", "PR43",
Semana["Quinta"] = "LP42", "LP42", "ES41", "ES41"
Semana["Sexta"] = "DS44", "DS44", "PR43", "PR43"

request = input("Qual é o dia da semana? ").strip()

if request in Semana:
    print("As aulas de {} serão {}.".format(request, Semana.get(request)))
else:
    print("Este dia não existe.")