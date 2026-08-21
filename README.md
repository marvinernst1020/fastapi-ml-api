# FastAPI ML API

FastAPI-based REST API with JWT authentication and database support, intended as a foundation for deploying machine learning models.

## Features

- Seller accounts with hashed passwords (bcrypt via passlib)
- JWT-based login and route protection (`python-jose`)
- Product CRUD, scoped to authenticated sellers
- SQLAlchemy models with a seller/product relationship
- API metadata (title, description, contact, license) exposed via the auto-generated docs

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-ml-api.git
cd fastapi-ml-api
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Create a `.env` file in the project root with:
```
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=20
```

To generate a random string for `SECRET_KEY`, run:
```bash
openssl rand -hex 32
```

Run the app:
```bash
uvicorn product.main:app --reload
```

Interactive API docs are available at `http://127.0.0.1:8000/docs`.

## API overview

- `POST /login` - authenticate with a seller's username/password, returns a JWT access token
- `POST /seller` - create a seller (requires authentication)
- `DELETE /seller/{id}` - delete a seller (requires authentication)
- `GET /product/` - list all products (requires authentication)
- `GET /product/{id}` - get a single product (requires authentication)
- `POST /product/` - create a product (requires authentication)
- `PUT /product/{id}` - update a product (requires authentication)
- `DELETE /product/{id}` - delete a product (requires authentication)

All routes except `/login` require a `Bearer` token in the `Authorization` header.

## Notes

Work in progress. The ML inference endpoint is not yet implemented.
