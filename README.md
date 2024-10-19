# FastAPI Marketplace Product Management API

This project is a **FastAPI** application that provides a RESTful API for managing products on a marketplace. The API allows users to add, update, delete, and retrieve product information, as well as fetch category details and filter products based on various parameters.

## Features

- **Product Management**: Create, update, delete, and retrieve product data.
- **Category Management**: Retrieve categories and their associated products.
- **Filtering**: Filter products based on various parameters like price, category, etc.
- **Asynchronous**: Fully asynchronous implementation using `FastAPI` and `SQLAlchemy` with `asyncpg`.


## Endpoints

### Products
- `GET /products`: Retrieve a list of products.
- `GET /products/{product_id}`: Retrieve a specific product by ID.
- `POST /products`: Add a new product.
- `PUT /products/{product_id}`: Update product details.
- `DELETE /products/{product_id}`: Delete a product by ID.

### Categories
- `GET /categories`: Retrieve all categories.
- `GET /categories/{category_id}`: Retrieve a specific category by ID.
- `GET /categories/{category_id}/products`: Get products for a specific category.

### Filtering
- `GET /products?category={category_id}&price_min={min_price}&price_max={max_price}`: Filter products by category, price range, and more.

## Tech Stack

- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: ORM for database interaction.
- **PostgreSQL**: Database backend.
- **asyncpg**: Async driver for PostgreSQL.
- **Pytest**: For unit and integration testing.
- **Poetry**: Dependency management.
- **Python json logger**: Logging in json files

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.12+
- PostgreSQL
- [Poetry](https://python-poetry.org/) for dependency management

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-marketplace-api.git
   cd fastapi-marketplace-api

2. Install dependencies:
   ```bash
    poetry install

3. Set up environment variables for database configuration:
```bash
export DB_USER=your_db_user
export DB_PASSWORD=your_db_password
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=your_db_name

4. Run database migrations (if any):
# Example using Alembic (adjust to your setup)
```bash
alembic upgrade head


```md
### Running the Application

To run the FastAPI application locally, use the following command:

```bash
poetry run uvicorn app.main:app --reload


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
