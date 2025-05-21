import time

from confluent_kafka import Producer, Consumer, TopicPartition


def test_confluent_complex(generate, process, size, batch_size):
    produce = None
    complex = None
    data = ("b"*512).encode() # 0.5Kb string (not 1Kb because no unicode symbols)
    producer = Producer({"bootstrap.servers": "localhost:9092",
                         "queue.buffering.max.messages": batch_size,
                         "queue.buffering.max.kbytes": batch_size})
    consumer = Consumer({"bootstrap.servers": "localhost:9092", "group.id": "confluent", "auto.offset.reset": "earliest"})

    if generate:
        start = time.time()
        for i in range(1, size + 1):
            producer.produce("input", data)
            if i % batch_size == 0:
                producer.flush()
        produce = time.time() - start

    if process:
        consumer.assign([TopicPartition("input", 0)])
        start = time.time()
        for _ in range(size // batch_size):
            for msg in consumer.consume(num_messages=batch_size):
                producer.produce("output", msg.value())
            producer.flush()
        complex = time.time() - start

    print(f"produce: {produce}, complex: {complex}")

