#!/bin/bash

# Запустить Flask приложение в фоновом режиме
gunicorn -w 4 -b 0.0.0.0:5000 converter.app:app &

# Запустить FastAPI приложение
uvicorn converter.api:app --host 0.0.0.0 --port 8000
