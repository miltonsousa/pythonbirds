class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprinmentar(self):
        return f'Ola, meu nome é {self.nome}'

    @staticmethod
    def metodo_sonic():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprinmentar(self):
        cumprimentar_da_classe=super().cumprinmentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3



if __name__ == '__main__':
     costa = Mutante(nome='Costa')
     daniel = Homem(costa, nome='Daniel')
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
     print(Pessoa.olhos)
     print(daniel.olhos)
     print(costa.olhos)
     print(id(Pessoa.olhos)), id(daniel.olhos), id(costa.olhos)
     print(Pessoa.metodo_sonic(), daniel.metodo_sonic())
     print(Pessoa.nome_e_atributos_de_classe(), daniel.nome_e_atributos_de_classe())
     pessoa=Pessoa('Anonimo')
     print(isinstance(pessoa, Pessoa))
     print(isinstance(pessoa, Homem))
     print(isinstance(costa, Pessoa))
     print(isinstance(costa, Homem))
     print(costa.olhos)
     print(costa.cumprinmentar())
     print(daniel.cumprinmentar())






