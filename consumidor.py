import pika
import time
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='cola_facturacion', durable=True)

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f" [x] Generando PDF para la orden {data['id_orden']}...")
    time.sleep(4) 
    print(f" [x] Enviando correo a {data['email']}... Finalizado.")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='cola_facturacion', on_message_callback=callback)

print(' [*] Consumidor listo. Esperando mensajes...')
channel.start_consuming()