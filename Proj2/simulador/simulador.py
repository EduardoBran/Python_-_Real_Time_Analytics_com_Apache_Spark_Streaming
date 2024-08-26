import sys
import random
import string
import datetime
import json  # Importa a biblioteca JSON

# Define o número de mensagens (leituras) que serão geradas
# Se nenhum valor for informado, vamos gerar apenas 10 registros
if len(sys.argv) > 1:
    num_msgs = int(sys.argv[1])
else:
    num_msgs = 10

# Possíveis locais onde os sensores podem estar instalados
locations = ['Corredor_A', 'Corredor_B', 'Caixa', 'Sessao_de_Eletronicos', 'Sessao_de_Roupas']

# Lista de letras do alfabeto em maiúsculo
letras = string.ascii_uppercase

# Gera o arquivo de saída em formato JSON
if __name__ == "__main__":

    # Loop de 0 até o número de mensagens (valor definido ao executar o simulador)
    for counter in range(0, num_msgs):

        # Gera uma combinação com 3 números randômicos
        rand_num = ''.join(random.choices(string.digits, k=3))

        # Gera uma combinação com 2 letras randômicas
        rand_letter = ''.join(random.choices(letras, k=2))

        # O id do sensor recebe o valor base mais os valores randômicos gerados anteriormente
        id_sensor = "SM-" + rand_num + rand_letter

        # Seleciona uma localização de forma randômica da lista de locations
        location = random.choice(locations)

        # Gera um identificador único para o cliente (pode ser anônimo)
        customer_id = "Cliente_" + ''.join(random.choices(string.digits, k=4))

        # Define se o movimento foi detectado (sempre True, mas incluído para consistência)
        movement_detected = True

        # Gera um valor randômico para a duração (tempo em segundos) que o cliente permaneceu na área
        duration = round(random.uniform(5, 300), 2)  # Duração entre 5 segundos e 5 minutos

        # Gera um valor randômico para a contagem de tráfego (número de clientes detectados)
        traffic_count = random.randint(1, 10)

        # Formata a data atual de execução do script para usar como data do evento
        today = datetime.datetime.today()
        timestamp = today.isoformat()

        # Formata os dados do sensor em um dicionário
        sensor_data = {
            "timestamp": timestamp,
            "id_sensor": id_sensor,
            "location": location,
            "customer_id": customer_id,
            "movement_detected": movement_detected,
            "duration": duration,
            "traffic_count": traffic_count
        }

        # Serializa o dicionário em uma string JSON bem-formada e imprime
        print(json.dumps(sensor_data))

