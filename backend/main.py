from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Add this line
from backend.services import generate_ai_ad

app = FastAPI()

# --- ADD THIS SECURITY SECTION ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This allows all "waiters" to talk to the kitchen
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------------

@app.get("/")
def home():
    return {"message": "AI Marketing Server is Online"}

@app.get("/generate")
def get_ad(product: str):
    ad_text = generate_ai_ad(product)
    return {"product": product, "ad": ad_text}