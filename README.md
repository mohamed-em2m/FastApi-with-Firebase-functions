# 🔄 Firebase to FastAPI Bridge

This Firebase Function acts as a reverse proxy to forward incoming HTTP requests to a FastAPI application. It allows you to use Firebase Hosting or Cloud Functions as a serverless gateway to a FastAPI backend.

## 🧩 Features

- Supports all HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`)
- Handles query strings, headers, and body payloads
- Built-in logging and error handling
- FastAPI integration via Starlette's `TestClient`

## 🚀 Deployment

### Prerequisites

- Firebase CLI configured
- `firebase-functions`, `firebase-admin`, and Python dependencies installed
- FastAPI app defined

### File Structure

