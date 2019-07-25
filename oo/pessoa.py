class Pessoa:
    def cumprinmentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
     p = Pessoa()
     print(Pessoa.cumprinmentar(p))
     print(id(p))
     print(p.cumprinmentar())
