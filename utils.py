from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Adryanno', idade=49)
#    pessoa = Pessoas(nome='Fafafe', idade=29)
    print(pessoa)
    pessoa.save()


def consultar_pessoa():
    pessoa = Pessoas.query.all()
#    pessoa = Pessoas.query.filter_by(nome='Adryanno').first()
#    pessoa = Pessoas.query.filter_by(name='Adry')
    print(pessoa)
    #print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Adryanno').first()
#    pessoa.idade = 21
    pessoa.nome = 'Sonia'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Fafafe').first()
    pessoa.delete()


if __name__=='__main__':
#    insere_pessoas()
#    altera_pessoa()
    exclui_pessoa()
    consultar_pessoa()

