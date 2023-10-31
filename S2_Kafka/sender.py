import time
import requests
from confluent_kafka import Producer

def fetch_spell_from_api():
    url_base = "https://hp-api.onrender.com/api/"
    endpoint_url = "spells"
    url = url_base + endpoint_url
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def delivery_report(err, msg):
    if err is not None:
        print(f'Erro ao entregar a mensagem: {err}')
    else:
        print(f'Mensagem com feitiço enviado ao tópico {msg.topic()} - Partição {msg.partition()} \n')

def main():
    conf = {
        'bootstrap.servers': 'localhost:9092',
    }

    producer = Producer(conf)

    while True:
        spell_data = fetch_spell_from_api()

        if spell_data is not None:
            for spell in spell_data:
                spell_id = spell['id']
                message = f"ID: {spell_id} - Nome: {spell['name']} - Descrição: {spell['description']}."
                producer.produce('HarryPotter', key=spell_id, value=message, callback=delivery_report)
                producer.flush()
                print(message, '\n\n')
                time.sleep(3)
        else:
            print("Falha ao obter dados da API")

        

if __name__ == '__main__':
    main()
