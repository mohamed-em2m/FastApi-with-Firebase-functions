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
- \`firebase-functions\`, \`firebase-admin\`, and Python dependencies installed
- FastAPI app defined

### File Structure

\`\`\`
project/
│
├── main.py               # Firebase function file (contains this handler)
├── app.py or embedded    # FastAPI application instance
├── requirements.txt
└── firebase.json
\`\`\`

### Deploy to Firebase

\`\`\`bash
firebase deploy --only functions
\`\`\`

Make sure you define the function in your \`firebase.json\` under \`"functions"\`.

## ⚙️ How it works

This function:

1. Receives an HTTP request from Firebase.
2. Uses Starlette’s \`TestClient\` to simulate a request to a local FastAPI app.
3. Returns the response from the FastAPI app to the original Firebase client.

## 🧪 Local Testing

Use \`functions-framework\` or mock HTTP calls to test locally. You can also use \`TestClient\` directly with your FastAPI app for unit testing.
