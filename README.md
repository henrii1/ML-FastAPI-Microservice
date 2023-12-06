# FastAPI ML Microservice

![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

This repository contains a fully-fledged machine learning-based microservice built with the FastAPI framework. The microservice exposes endpoints for seamless integration with machine learning models, making it easy to deploy and scale.

## Features

- **FastAPI Framework:** Utilizes FastAPI, a modern, fast, and web-based framework for building APIs with Python 3.7+.

- **AWS ECR and ECS Deployment:** The microservice is designed to be easily deployed on Amazon Elastic Container Registry (ECR) and Elastic Container Service (ECS), providing a scalable and reliable cloud infrastructure.

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/fastapi-ml-microservice.git
    cd fastapi-ml-microservice
    ```

2. Set up your Python environment (Python 3.8 or higher recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the streamlit app:
   ```
   streamlit run webapp/app_streamlit.py
   ```
5. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

6. Access the API at `http://127.0.0.1:8000` and explore the available endpoints.

## Deployment

For deployment on AWS ECR and ECS, follow the provided deployment scripts and configuration files. Ensure that your AWS credentials are properly configured.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

