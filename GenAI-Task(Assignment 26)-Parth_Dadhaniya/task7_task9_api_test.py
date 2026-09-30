# task7_task9_api_test.py
# Tasks 7 & 9: Testing FastAPI App & End-to-End API Verification
# Student: Parth Dadhaniya

import time
import warnings
warnings.filterwarnings("ignore")

from fastapi.testclient import TestClient
from app import app

print("=== Tasks 7 & 9: Run & Test FastAPI App Locally ===")

client = TestClient(app)

# 1. Test root endpoint
print("\n--- 1. Testing GET / ---")
r_root = client.get("/")
print("Status:", r_root.status_code)
print("Body  :", r_root.json())
assert r_root.status_code == 200

# 2. Test health check
print("\n--- 2. Testing GET /health ---")
r_health = client.get("/health")
print("Status:", r_health.status_code)
print("Body  :", r_health.json())
assert r_health.status_code == 200
assert r_health.json()["status"] == "healthy"

# 3. Test direct chat endpoint
print("\n--- 3. Testing POST /chat (Direct Chat) ---")
q_direct = "Why is Groq fast compared to standard cloud LLM hosting?"
t0 = time.time()
r_direct = client.post("/chat", json={"query": q_direct, "use_rag": False})
t_elapsed = round(time.time() - t0, 3)

print("Query   :", q_direct)
print("Status  :", r_direct.status_code)
print("Answer  :", r_direct.json()["answer"])
print(f"Latency : {r_direct.json()['latency_seconds']}s (roundtrip: {t_elapsed}s)")
assert r_direct.status_code == 200

# 4. Test RAG endpoint
print("\n--- 4. Testing POST /chat (RAG Document Query) ---")
q_rag = "What is the annual leave policy according to the employee handbook?"
r_rag = client.post("/chat", json={"query": q_rag, "use_rag": True})
print("Query   :", q_rag)
print("Status  :", r_rag.status_code)
print("Answer  :", r_rag.json()["answer"])
print("Sources :", r_rag.json()["sources"])
print(f"Latency : {r_rag.json()['latency_seconds']}s")
assert r_rag.status_code == 200

# 5. Test validation error handling
print("\n--- 5. Testing Validation Error (Empty Query) ---")
r_err = client.post("/chat", json={"query": ""})
print(f"Status  : {r_err.status_code} (Expected 422 Unprocessable Entity)")
assert r_err.status_code == 422

print("\n" + "=" * 50)
print("All FastAPI endpoint tests passed successfully!")
print("Interactive docs available at: http://127.0.0.1:8000/docs")
print("=" * 50)
