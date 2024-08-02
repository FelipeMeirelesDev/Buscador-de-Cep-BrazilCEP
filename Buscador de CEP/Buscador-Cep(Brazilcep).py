#importando a biblioteca
import brazilcep

#brazilcep.get_address_from_cep("[Digite o cep]").
#aqui vamos atribuir as informações na variavel "endereco".
#coloquei o cep da capital do Brasil como exemplo.
endereco = brazilcep.get_address_from_cep("70070600")

#colando especificamente as informações cidade e estado nas respectivas variaveis.
cidade = endereco.get("city")
estado = endereco.get("uf")

#Mostrando o resultado.
print("A sua cidade é {} e seu estado é {}.".format(cidade, estado))
