from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Import your AI service here (Gemini, OpenAI, etc.)
from backend.services import call_ai_service 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate")
def generate(product: str, platform: str = "Instagram"):
    # The prompt now changes based on the platform!
    prompt = f"Write a high-converting {platform} ad for {product}. Use emojis and a tone perfect for {platform} users."
    
    # Call your AI function
    ai_response = call_ai_service(prompt)
    
    return {"ad": ai_response}