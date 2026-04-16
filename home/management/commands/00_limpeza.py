# Lembre-se de substituir 'seu_app' pelo nome real do aplicativo onde o models.py está
from home.models import (
    CrescimentoMedioPorte, CrescimentoMedioUf, MedianaPorteReceita, RegiaoMetropolitana, Percentis, Municipio, ContaDetalhada, 
    ContaDetalhadaPercentil, ContaEspecifica, ContaEspecificaPercentil, 
    ContaMaisEspecifica, ContaMaisEspecificaPercentil, MediaNacionalReceita,
    MediaUfReceita, MediaPorteReceita, MedianaNacionalReceita, MedianaUfReceita,
    MedianaUfReceita, MedianaPorteReceita, CrescimentoMedioUf, CrescimentoMedioPorte
    
)

def limpar_banco_exceto_noticias():
    print("Iniciando a exclusão dos dados...")

    # 1. Tabelas independentes (sem dependência de cascade)
    RegiaoMetropolitana.objects.all().delete()
    Percentis.objects.all().delete()
    MediaNacionalReceita.objects.all().delete()
    MediaUfReceita.objects.all().delete()
    MediaPorteReceita.objects.all().delete()
    MedianaNacionalReceita.objects.all().delete()
    MedianaUfReceita.objects.all().delete()
    MedianaUfReceita.objects.all().delete()
    MedianaPorteReceita.objects.all().delete()
    CrescimentoMedioUf.objects.all().delete()
    CrescimentoMedioPorte.objects.all().delete()

    # 2. Tabelas dependentes (Para garantir, podemos deletar explicitamente antes do Município)
    ContaDetalhada.objects.all().delete()
    ContaDetalhadaPercentil.objects.all().delete()
    ContaEspecifica.objects.all().delete()
    ContaEspecificaPercentil.objects.all().delete()
    ContaMaisEspecifica.objects.all().delete()
    ContaMaisEspecificaPercentil.objects.all().delete()

    # 3. Deletar Municípios
    Municipio.objects.all().delete()

    print("Todos os dados foram excluídos com sucesso, exceto as Notícias!")

# Executa a função
limpar_banco_exceto_noticias()