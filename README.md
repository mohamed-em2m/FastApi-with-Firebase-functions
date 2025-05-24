# 🔄 firebase_fastapi_wrapper

A lightweight wrapper to run FastAPI apps inside Firebase Functions. Enables HTTP request forwarding from Firebase to FastAPI.

## 🚀 Features

- Seamlessly proxy Firebase HTTPS requests to FastAPI.
- Handles headers, query strings, and request body.
- Works with `firebase-functions` Python SDK.

## 🧩 Install

```bash
pip install firebase_fastapi_wrapper
```
### 🔧 Usage

```python

from firebase_functions import https_fn
from fastapi import FastAPI
from firebase_fastapi_wrapper.wrapper import FastAPIWrapper

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"}

firebase_handler = FastAPIWrapper(app)

@https_fn.on_request()
def handle_request(req: https_fn.Request):
    return firebase_handler(req)
```
### 📄 requirements.txt
```txt
fastapi>=0.110.0
starlette>=0.36.3
firebase-functions>=0.2.0
```
