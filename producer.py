from kafka import KafkaProducer
import json
import time

KAFKA_BROKER = "localhost:9092"
TOPIC = "transacoes_bancarias"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

transactions = [
    {"id": 1, "tipo": "deposito", "valor": 1000, "cliente_id": 101},
    {"id": 2, "tipo": "transferencia", "valor": 500, "cliente_id": 102}
]

for transaction in transactions:
    producer.send(TOPIC, transaction)
    print(f"📤 Transação enviada: {transaction}")
    time.sleep(1)
