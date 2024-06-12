# Stage 1: Build React App
FROM node:14 as build

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install

COPY frontend/ ./

RUN npm run build

# Stage 2: Build FastAPI app
FROM python:3.8-slim

WORKDIR /app

COPY backend/ ./
COPY --from=build /app/build ./frontend/build

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
