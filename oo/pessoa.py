class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome


    def cumprinmentar(self):
        return f'Ola {id(self)}'



if __name__ == '__main__':
     p = Pessoa('Costa')
     print(Pessoa.cumprinmentar(p))
     print(id(p))
     print(p.cumprinmentar())
     print(p.nome)
     p.nome = 'Daniel'
     print(p.nome)
     print(p.idade)
