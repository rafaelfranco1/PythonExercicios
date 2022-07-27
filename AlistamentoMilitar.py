ano = int(input('Ano de nascimento: '))
nascimento = (2017 - ano)
final = nascimento - 18
alistamento = 2017 - final
if (nascimento > 18):

    print('Quem nasceu em {} tem {} anos em 2017.'.format(ano,nascimento))
    print('Você já deveria ter se alistado há {} anos.'.format(final))
    print('Seu alistamento foi em {}'.format(alistamento))
elif (nascimento < 18):
    auxnascimento = (2017 - ano)
    auxfalta = 18 - auxnascimento
    auxalistamento = (18 - auxnascimento)+2017
    print('Quem nasceu em {} tem {} anos em 2017'.format(ano,auxnascimento))
    print('Ainda faltam {} 2 anos para o {} alistamento'.format(ano,auxfalta))
    print('Seu alistamento será em {}'.format(auxalistamento))
else:
    print('Quem nasceu em {} tem {} anos em 2017.'.format(ano,nascimento))
    print('Você tem que se alistar imediatamente!')