![CI/CD Status](https://github.com/NikGor/currency-converter/actions/workflows/status.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/e3055c1f877bd15a2904/maintainability)](https://codeclimate.com/github/NikGor/currency-converter/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e3055c1f877bd15a2904/test_coverage)](https://codeclimate.com/github/NikGor/currency-converter/test_coverage)

# Currency Converter API

This is a simple API for currency conversion using FastAPI and SQLAlchemy.

## Installation and Setup

1. Make sure you have Docker and Docker Compose installed.

2. Clone the repository:

   ```bash
   git clone https://github.com/NikGor/currency-converter.git
   ```

3. Navigate to the project directory:

   ```bash
   cd currency-converter-api
   ```

4. Create a `.env` file in the project root and set the environment variable values:

   ```
   DATABASE_URL=postgresql://postgres:your_password_here@db/currency_converter
   ```

   Replace `your_password_here` with your PostgreSQL password.

5. Start the application and PostgreSQL in containers:

   ```bash
   docker-compose -f docker-compose.yml up --build -d
   ```

   The application will be available at `http://localhost:8000`.

6. Access the currency converter interface in your browser at `http://localhost:8000/currency-converter`.

## Using the API

The API provides the following endpoints:

- Update currency rates:
  ```
  POST /update-currency-rates
  ```

- Get the date and time of the last currency rates update:
  ```
  GET /last-updated
  ```

- Currency conversion:
  ```
  POST /convert-currency
  ```

  Example request for conversion:
  ```json
  {
    "from_currency": "USD",
    "to_currency": "EUR",
    "amount": 100.0
  }
  ```

  Example response:
  ```json
  {
    "request": {
      "from_currency": "USD",
      "to_currency": "EUR",
      "amount": 100.0
    },
    "result": 85.0
  }
  ```

## Templating

The API also includes a simple web interface for currency conversion. You can use the `/currency-converter` page in your browser for easy data input.

## License

This project is distributed under the MIT License. See the `LICENSE` file for details.