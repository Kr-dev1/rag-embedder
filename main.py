from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

class EmbedRequest(BaseModel):
    text: str

@app.get("/ping")
def ping():
    print("✅ Ping received.")
    return {"status": "alive"}

@app.post("/embed")
def embed_text(req: EmbedRequest):
    print(f"🧠 Embedding text: {req.text[:30]}...")
    embedding = model.encode(req.text).tolist()
    return {"embedding": embedding}
