import random
import time

import paho.mqtt.client as mqtt

# Configuração
broker = "test.mosquitto.org"
port = 1883
topic = "siChat/mqtt"

# Criação do cliente MQTT
client = mqtt.Client()

# Conexão ao broker
client.connect(broker, port, 60)

# Publicação em loop
while True:
    client.publish(topic, "OLA RAFAEL")
    # Lista de mensagens aleatórias
    messages = ["Rafael", "Oi", "Tudo Bem?", "Hey there", "Olá", "Como vai?", "Bom dia", "Boa tarde", "Boa noite"]
    # Lista de piadas sem graça
    jokes = [
        "Por que o peixe não gosta de computador? Porque ele tem medo do mouse!",
        "Qual é o doce que é mais azedo? O azedinho de bateria!",
        "Por que o livro de matemática se suicidou? Porque tinha muitos problemas!",
        "Qual é o cúmulo da rapidez? Fechar a geladeira com a luz apagada!",
        "Por que a aranha é o animal mais carente do mundo? Porque ela é um aracneedyou!",
        "Qual é o animal que é um exemplo? O elefante, porque ele nunca esquece!",
        "Por que o jacaré tirou o jacarezinho da escola? Porque ele réptil de ano!",
        "Qual é o doce que é mais salgado? O salgadinho de bateria!",
        "Por que o pato não usa drogas? Porque ele toma patoléptico!",
        "Qual é o cúmulo da força? Chupar a cana e assoprar o bagaço!",
        "Por que a galinha atravessou a rua? Para mostrar que não era um frango medroso!",
        "Qual é o animal mais antigo? A zebra, porque está sempre em preto e branco!",
        "Por que o gato não gosta de apostar corrida? Porque ele sempre acaba empatando!",
        "Qual é o cúmulo da economia? Passar o dia inteiro no banco de trás do táxi!",
        "Por que o livro de receitas foi preso? Porque ele matou a fome de leitura!",
        "Qual é o doce que é mais quente? O pimentão doce!",
        "Por que o avião não pode ser eleito presidente? Porque ele sempre está em campanha!",
        "Qual é o cúmulo da paciência? Plantar uma árvore e esperar virar floresta!",
        "Por que o cachorro não usa celular? Porque ele já tem um telefone sem fio!",
        "Qual é o doce que é mais gelado? O sorvetinho de bateria!"
    ]
    jokes = ["Por que o peixe não gosta de computador? Porque ele tem medo do mouse!",
             "Qual é o doce que é mais azedo? O azedinho de bateria!",
             "Por que o livro de matemática se suicidou? Porque tinha muitos problemas!",
             "Qual é o cúmulo da rapidez? Fechar a geladeira com a luz apagada!",
             "Por que a aranha é o animal mais carente do mundo? Porque ela é um aracneedyou!",
             "Qual é o animal que é um exemplo? O elefante, porque ele nunca esquece!",
             "Por que o jacaré tirou o jacarezinho da escola? Porque ele réptil de ano!",
             "Qual é o doce que é mais salgado? O salgadinho de bateria!",
             "Por que o pato não usa drogas? Porque ele toma patoléptico!",
             "Qual é o cúmulo da força? Chupar a cana e assoprar o bagaço!"]

    # Publicação em loop
    while True:        # Escolhe uma piada sem graça aleatória da listaen        joke = random.choice(jokes)        client.publish(topic, joke)a da lista
        message = random.choice(jokes)
        client.publish(topic, message)
        time.sleep(0.5)
