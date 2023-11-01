# **Kafka com Docker Compose**

Este arquivo fornece informações sobre a criação de um docker-compose com todos os parâmetros de um kafka e seus gerenciadores, além de um exemplo de produção e consumo de mensagem local.

## **1. Tecnologias Utilizadas e Conexões**

Neste projeto, foram utilizadas várias tecnologias que se conectam para possibilitar a criação de um ambiente de mensagens Kafka com Docker Compose. Todas elas trabalham em conjunto para criar um ambiente onde mensagens Kafka são produzidas, consumidas e gerenciadas. O Docker Compose orquestra os contêineres do Kafka e Zookeeper, enquanto Python e a biblioteca confluent-kafka são usados para produzir e consumir mensagens. A utilização de uma API REST externa demonstra a capacidade de integrar o Kafka com outros serviços e fontes de dados.

### **1.1. Docker e Docker Compose**

<img src="./assets/logoDocker.png" alt="Icon Docker" width="100" height="80">

**Docker:** É uma plataforma que permite empacotar, distribuir e executar aplicativos em contêineres, fornecendo isolamento e portabilidade.

<img src="./assets/logoDockerCompose.png" alt="Icon Docker Compose" width="100" height="100">

**Docker Compose:** É uma ferramenta para definir e executar aplicativos Docker multi-container. Permite a configuração de vários serviços em um arquivo YAML, como neste projeto.

### **1.2. Kafka**

<img src="./assets/logoKafka.png" alt="Icon Kafka" width="100" height="80">

**Apache Kafka:** É uma plataforma de streaming de eventos distribuída que permite a ingestão, armazenamento e processamento de eventos em tempo real. É a peça central deste projeto, fornecendo a funcionalidade de mensagens.

### **1.3. Zookeeper**

<br>

<img src="./assets/logoZookeeper.png" alt="Icon Zookeeper" width="110" height="60">

<br>

**Apache Zookeeper:** É um serviço de coordenação distribuída utilizado pelo Kafka para gerenciar o estado e a configuração de brokers Kafka. Garante a confiabilidade e a alta disponibilidade do Kafka.

### **1.4. Python**

<img src="./assets/logoPython.png" alt="Icon Python" width="110" height="100">

**Python:** É a linguagem de programação utilizada para desenvolver os scripts sender.py e receiver.py. Python é amplamente adotado na comunidade de desenvolvimento e oferece bibliotecas robustas para interagir com o Kafka e fazer solicitações a APIs externas.

### **1.5. Confluent-kafka**

<br>

<img src="./assets/logoConfluentKafka.png" alt="Icon Confluent-kafka" width="60" height="50">

<br>

**Confluent-kafka:** É uma biblioteca Python que fornece uma interface para interagir com o Kafka. É utilizada nos scripts sender.py e receiver.py para a produção e consumo de mensagens no Kafka.

### **1.6. REST API**

<img src="./assets/logoRestApi.png" alt="Icon REST API" width="100" height="90">

**API REST:** O script sender.py faz solicitações a uma API REST externa (API Harry Potter) para obter dados de feitiços. APIs REST são amplamente utilizadas para a comunicação com serviços web.


## **2. Configuração do Docker Compose**

O arquivo **`docker-compose.yaml`** contém a configuração do Kafka e Zookeeper com os seguintes parâmetros:

- **zookeeper**: Um serviço Zookeeper que é essencial para o funcionamento do Kafka.
- **kafka**: Um serviço Kafka que utiliza o Zookeeper para gerenciar tópicos e mensagens.

## **3. Especificação dos Parâmetros**

Os parâmetros utilizados no arquivo **`docker-compose.yaml`** são baseados nas configurações padrão do Kafka e são definidos da seguinte forma:

- **`KAFKA_BROKER_ID`**: O ID do broker Kafka.
- **`KAFKA_LISTENERS`**: Especifica os ouvintes para a conexão de clientes Kafka.
- **`KAFKA_ADVERTISED_LISTENERS`**: Define a configuração de ouvintes anunciados.
- **`KAFKA_ZOOKEEPER_CONNECT`**: Especifica a conexão com o serviço Zookeeper.
- **`KAFKA_NUM_PARTITIONS`**: Define o número de partições para tópicos.
- **`KAFKA_ALLOW_PLAINTEXT_LISTENER`**: Permite a conexão por meio do protocolo PLAINTEXT.

## **4. Exemplo de Produção e Consumo de Mensagens Kafka**

O projeto inclui dois scripts Python, **`sender.py`** e **`receiver.py`**, que demonstram a produção e o consumo de mensagens Kafka.

- **`sender.py`**: Este script faz uma solicitação a uma API externa (API Harry Potter) para obter feitiços e os envia para o tópico "HarryPotter" no Kafka.
- **`receiver.py`**: Este script consome mensagens do tópico "HarryPotter" no Kafka e imprime os feitiços recebidos.

## **5. Práticas de Programação e Uso da Documentação Oficial**

O código Python nos scripts **`sender.py`** e **`receiver.py`** segue boas práticas de programação e utiliza a biblioteca **`confluent-kafka`** para interagir com o Kafka. Aqui estão algumas práticas e exemplos específicos de como elas são aplicadas:

### **5.1. Uso de Try-Except para Tratamento de Erros**

Em ambos os scripts, um bloco **`try-except`** é usado para lidar com erros, incluindo erros ao consumir mensagens Kafka ou ao enviar mensagens para o tópico. Isso garante que o código possa lidar com situações de erro sem interromper a execução do programa.

Exemplo em **`receiver.py`**:

```python

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Erro ao consumir mensagem: {msg.error()}")
        else:
            print(f"Feitiço novo recebido: {msg.value().decode('utf-8')}\n\n")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()

```

### **5.2. Nomes Significativos de Variáveis e Funções**

As variáveis e funções nos scripts têm nomes significativos que refletem seu propósito, facilitando a compreensão do código. Por exemplo, a função **`fetch_spell_from_api()`** é nomeada para indicar que ela busca feitiços de uma API externa.

Exemplo em **`sender.py`**:

```python
def fetch_spell_from_api():
    # ...continuação do código...
```

### **5.3. Documentação Oficial do Kafka**

O código foi desenvolvido com base na documentação oficial do Kafka. Isso inclui a configuração de parâmetros e o uso de métodos e classes fornecidos pela biblioteca **`confluent-kafka`**.

Exemplo em **`sender.py`**:

```python
conf = {
    'bootstrap.servers': 'localhost:9092',
}

producer = Producer(conf)
```

- **Documentação do Kafka**: [Documentação oficial do Apache Kafka](https://kafka.apache.org/documentation/)

### **5.4. Uso de Callbacks para Mensagens Kafka**

O código utiliza callbacks para lidar com a entrega de mensagens Kafka. Isso permite monitorar o status das mensagens enviadas e tratar possíveis erros de entrega.

Exemplo em **`sender.py`**:

```python

def delivery_report(err, msg):
    if err is not None:
        print(f'Erro ao entregar a mensagem: {err}')
    else:
        print(f'Mensagem com feitiço enviado ao tópico {msg.topic()} - Partição {msg.partition()}\n')

# ...

producer.produce('HarryPotter', key=spell_id, value=message, callback=delivery_report)

```

### **5.5. Manipulação de Exceções**

O código manipula exceções de acordo com as boas práticas de programação. Por exemplo, ele lida com exceções que podem ocorrer ao fazer solicitações à API externa.

Exemplo em **`sender.py`**:

```python

def fetch_spell_from_api():
    url_base = "https://hp-api.onrender.com/api/"
    endpoint_url = "spells"
    url = url_base + endpoint_url
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

```

Esses são exemplos de como as práticas de programação são aplicadas nos scripts e como a documentação oficial do Kafka é utilizada para configurar e interagir com o Kafka. 

## **6. Executando o Projeto**

Para executar o projeto, siga estas etapas:

1. Certifique-se de ter o Docker e o Docker Compose instalados no seu sistema.
2. Clone este repositório.
3. Navegue até a pasta do projeto e execute o seguinte comando para iniciar os serviços Kafka e Zookeeper:
    
    ```bash
   docker-compose up
    ```
    
4. Em um terminal separado, execute o script **`sender.py`** para produzir mensagens Kafka:
    
    ```bash
    python sender.py
    ```
    
5. Em outro terminal separado, execute o script **`receiver.py`** para consumir mensagens Kafka:
    
    ```bash
    python receiver.py
    ```

Agora o projeto está pronto para produzir e consumir mensagens Kafka de feitiços utilizando o Kafka com Docker Compose. Certifique-se de estar **dentro do terminal na pasta S2_Kafka ao executar os scripts**.

## 7. Resultados esperados


1. O Docker Compose iniciará os serviços Kafka e Zookeeper no ambiente de contêineres.
2. O script **`sender.py`** fará solicitações na API Harry Potter para obter feitiços. Esses feitiços serão produzidos no tópico "HarryPotter" no Kafka.
3. O script **`receiver.py`** estará constantemente consumindo mensagens do tópico "HarryPotter" no Kafka e exibindo os feitiços recebidos no console.
4. Você verá mensagens impressas no console indicando que os feitiços foram enviados com sucesso para o tópico Kafka e que estão sendo consumidos pelo consumidor Kafka.


<br>

<img src="./assets/resultadoProjeto.gif" alt="Resultados esperados">

<br>

Certifique-se de que o Docker Compose esteja em execução e que ambos os scripts Python estejam em execução em terminais separados para obter esses resultados. Isso demonstrará o fluxo de produção e consumo de mensagens no ambiente Kafka configurado.


## 8. Referências Bibliográficas 

1. **Docker Compose Documentação.** Disponível em: [github.com/mrugankray](https://github.com/mrugankray). Acesso em: 30 out. 2023.

2. **Confluent Kafka Python.** Disponível em: [github.com/felipesilvamelo28](https://github.com/felipesilvamelo28). Acesso em: 30 out. 2023.

3. **API universo Harry Potter.** Disponível em: [https://hp-api.onrender.com/api/spells](https://hp-api.onrender.com/api/spells). Acesso em: 30 out. 2023.

4. **Exemplo de configuração Kafka.** Disponível em: [github.com/mrugankray](https://github.com/mrugankray). Acesso em: 30 out. 2023.

5. **Exemplo de configuração Kafka e Python.** Disponível em: [github.com/felipesilvamelo28](https://github.com/felipesilvamelo28). Acesso em: 30 out. 2023.




