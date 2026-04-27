# FastAPI ML API

FastAPI-based REST API with authentication and database support, intended as a foundation for deploying machine learning models.

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-ml-api.git
cd fastapi-ml-api
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Run:
```bash
uvicorn product.main:app --reload
```
---

To generate a random string, that can be used as a key, open a new terminal and run:
```bash
openssl rand -hex 32
```

---

Notes:

Work in progress. The project will be extended with authentication, database integration, and an ML inference endpoint.

