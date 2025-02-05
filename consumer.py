from kafka import KafkaConsumer
import json
import psycopg2

KAFKA_BROKER = "localhost:9092"
TOPIC = "transacoes_bancarias"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

conn = psycopg2.connect(dbname="finance_db", user="admin", password="password", host="localhost", port="5432")
cursor = conn.cursor()

for message in consumer:
    data = message.value
    cursor.execute(
        "INSERT INTO transacoes (id_transacao, tipo, valor, cliente_id) VALUES (%s, %s, %s, %s)",
        (data["id"], data["tipo"], data["valor"], data["cliente_id"])
    )
    conn.commit()
    print(f"✅ Transação processada: {data}")
