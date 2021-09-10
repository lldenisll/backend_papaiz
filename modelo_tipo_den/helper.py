
from banco_de_dados.models import Exame, Exame_alt_anatomia

def get_denticao(n_os):
    id_exame = Exame.objects.get(cd_exame = n_os.lower()).id_exame
    denticao = Exame_alt_anatomia.objects.get(id_exame = id_exame).id_alteracao
    if denticao == 67:
        denticao = 'decidua'
    elif denticao == 68:
        denticao = 'mista'
    elif denticao == 69:
        denticao = 'permanente'
    return denticao 