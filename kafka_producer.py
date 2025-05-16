import pandas as pd
import json
from kafka import KafkaProducer
import time

def main():
    df = pd.read_csv('/mnt/c/Users/venka/Downloads/HDFC.daily.csv')
    print("Loaded dataset with", len(df), "rows")
    print("Columns:", df.columns)

    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    for _, row in df.iterrows():
        data = {
            'symbol': row['symbol'],
            'price': row['c'],        # close price
            'timestamp': row['t']     # timestamp
        }
        producer.send('stock_prices', value=data)
        print("Sent:", data)
        time.sleep(1)  # optional delay

    producer.flush()
    producer.close()

if __name__ == "__main__":
    main()
