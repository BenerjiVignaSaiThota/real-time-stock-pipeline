# Real-Time Stock Data Pipeline

This project demonstrates a real-time data pipeline using:

- **Kafka** for streaming stock data
- **Spark Structured Streaming** for processing
- **PostgreSQL** for storing transformed results

## Architecture

1. Kafka Producer simulates live stock prices.
2. Kafka Topic receives and buffers this stream.
3. Spark Streaming job consumes this data.
4. Spark transforms and pushes it to PostgreSQL.

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python (for producer)
- Spark installed (or use PySpark in standalone mode)

### Setup

```bash
git clone https://github.com/yourusername/real-time-stock-pipeline.git
cd real-time-stock-pipeline
docker-compose up -d
