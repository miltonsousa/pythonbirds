class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprinmentar(self):
        return f'Ola {id(self)}'



if __name__ == '__main__':
     costa = Pessoa(nome='Costa')
     daniel = Pessoa(costa, nome='Daniel')
     print(Pessoa.cumprinmentar(daniel))
     print(id(daniel))
     print(daniel.cumprinmentar())
     print(daniel.nome)
     print(daniel.idade)
     for filho in daniel.filhos:
         print(daniel.filhos)
     daniel.sobrenome='Sousa'
     del daniel.filhos
     daniel.olhos = 1
     del daniel.olhos
     print(daniel.__dict__)
     print(costa.__dict__)
     Pessoa.olhos = 3
     print(Pessoa.olhos)
     print(daniel.olhos)
     print(costa.olhos)
     print(id(Pessoa.olhos)), id(daniel.olhos), id(costa.olhos)