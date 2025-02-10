# CDC Ghost Blogger

A Real-Time Event Streaming Application incorporating Redis Cached DB and a RediSearch powered Frontend Utility along with Data Pipelines to Dashboard Event Logs, Statistics, and Retention Metrics using Kafka and Elasticsearch.

## Overview

CDC Ghost Blogger is designed to handle real-time event streaming by integrating a Redis-cached database and a RediSearch-powered frontend utility. It features data pipelines that dashboard event logs, statistics, and retention metrics utilizing Kafka and Elasticsearch.

## Repository Contents

- `application/`: Contains the main application code and related resources.
- `clickstream_pipeline/`: Includes the CDC (Change Data Capture) data pipeline setup.
- `.DS_Store`: System file (can be ignored).
- `README.md`: Project documentation.

## Requirements

- Docker
- Docker Compose
- Python 3.x
- Pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AkshadK7/CDC-Ghost-Blogger.git
   cd CDC-Ghost-Blogger
   ```

2. **Application Setup**:
   - Navigate to the `application` directory:
     ```bash
     cd application
     ```
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Build and start the application using Docker Compose:
     ```bash
     docker compose up --build
     ```

3. **CDC Data Pipeline Setup**:
   - Open a new terminal window and navigate to the `clickstream_pipeline` directory:
     ```bash
     cd clickstream_pipeline
     ```
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
   - Build and start the CDC data pipeline using Docker Compose:
     ```bash
     docker compose up --build
     ```

## Usage

- **Application**:
  - The application is set up to handle real-time event streaming with a Redis-cached database and a RediSearch-powered frontend.
  - Access the frontend utility to monitor and interact with the event data.

- **CDC Data Pipeline**:
  - The CDC data pipeline captures and processes change data, providing dashboards for event logs, statistics, and retention metrics.
  - Utilize the dashboards to gain insights into the event data and system performance.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/AkshadK7/CDC-Ghost-Blogger/blob/main/LICENSE) file for details.

## Acknowledgements

Special thanks to the open-source community and contributors for their support and resources.
```

*Note: Ensure that Docker and Docker Compose are installed on your system before proceeding with the setup. Additionally, verify that the `requirements.txt` files in both the `application` and `clickstream_pipeline` directories list all necessary dependencies.* 
