import pika
import json

# Conexión al RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar la cola
channel.queue_declare(queue='cola_facturacion', durable=True)

# Mensaje de prueba
data = {"id_orden": 1024, "cliente": "Juan Perez", "monto": 99.50, "email": "juan@espe.edu.ec"}

channel.basic_publish(
    exchange='',
    routing_key='cola_facturacion',
    body=json.dumps(data),
    properties=pika.BasicProperties(delivery_mode=2)
)
print(" [x] Orden enviada: %r" % data)
connection.close()