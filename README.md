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

### Setup

```bash
git clone https://github.com/yourusername/real-time-stock-pipeline.git
cd real-time-stock-pipeline
docker-compose up -d
