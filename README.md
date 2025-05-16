# Real-Time Stock Data Pipeline using Kafka, Docker and PostgreSQL

This project demonstrates a real-time data pipeline of HDFC company stocks using:

- **Kafka** for streaming stock data
- **Spark Structured Streaming** for processing
- **PostgreSQL** for storing transformed results

## Architecture

1. Kafka Producer simulates live stock prices.
2. Kafka Topic receives and buffers this stream.
3. Spark Streaming job consumes this data.
4. Spark transforms and pushes it to PostgreSQL.

## Getting Started

## Data Source
I have utilized kaggle dataset in order to implement this stock monitoring data pipeline.

Dataset Name: Stock Price Prediction || MODWT Application

Dataset link: https://www.kaggle.com/datasets/mishra5001/stock-price-prediction-modwt-application?select=HDFC.daily.csv

This dataset has following columns:
Symbol (representing the Stock Code)
t (timestamp when the following record was recorded)
o (opening price of stock)
c (closing price of the stock)
h (high price)
l (low price)
v (value of the stock)

### Prerequisites

- Docker & Docker Compose
- Python (for producer)
- Spark installed (or use PySpark in standalone mode)

### Sample Output
Loaded dataset with 4973 rows
Columns: Index(['symbol', 't', 'o', 'h', 'l', 'c', 'v'], dtype='object')
Sent: {'symbol': 'HDFC', 'price': 59.13, 'timestamp': 983232000}
Sent: {'symbol': 'HDFC', 'price': 59.35, 'timestamp': 983318400}
Sent: {'symbol': 'HDFC', 'price': 59.85, 'timestamp': 983404800}
Sent: {'symbol': 'HDFC', 'price': 55.61, 'timestamp': 983491200}
Sent: {'symbol': 'HDFC', 'price': 52.62, 'timestamp': 983750400}
Sent: {'symbol': 'HDFC', 'price': 54.41, 'timestamp': 983923200}
Sent: {'symbol': 'HDFC', 'price': 54.08, 'timestamp': 984009600}
Sent: {'symbol': 'HDFC', 'price': 54.04, 'timestamp': 984096000}
Sent: {'symbol': 'HDFC', 'price': 54.51, 'timestamp': 984355200}
Sent: {'symbol': 'HDFC', 'price': 54.6, 'timestamp': 984441600}
Sent: {'symbol': 'HDFC', 'price': 59.4, 'timestamp': 984528000}
Sent: {'symbol': 'HDFC', 'price': 57.27, 'timestamp': 984614400}
Sent: {'symbol': 'HDFC', 'price': 57.19, 'timestamp': 984700800}
Sent: {'symbol': 'HDFC', 'price': 56.95, 'timestamp': 984960000}
Sent: {'symbol': 'HDFC', 'price': 55.68, 'timestamp': 985046400}
Sent: {'symbol': 'HDFC', 'price': 56.88, 'timestamp': 985132800}
Sent: {'symbol': 'HDFC', 'price': 58.64, 'timestamp': 985219200}
Sent: {'symbol': 'HDFC', 'price': 58.62, 'timestamp': 985305600}
Sent: {'symbol': 'HDFC', 'price': 57.89, 'timestamp': 985564800}
Sent: {'symbol': 'HDFC', 'price': 58.67, 'timestamp': 985651200}

### Setup

```bash
git clone https://github.com/yourusername/real-time-stock-pipeline.git
cd real-time-stock-pipeline
docker-compose up -d
