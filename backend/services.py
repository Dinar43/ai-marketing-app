import random

def call_ai_service(product):
    # This mock version works without needing money or a real API key!
    mock_ads = [
        f"ESTABLISHED EXCELLENCE.\n\nIntroducing the all-new {product}. Designed for those who refuse to settle. Experience the future of craftsmanship today. #Luxury #Innovation",
        f"YOUR SEARCH ENDS HERE.\n\nWhy settle for ordinary when you can have {product}? Engineered for performance, styled for life. Shop the collection now.",
        f"THE {product} REVOLUTION.\n\nEverything you loved, reimagined. More power. More style. More you. Limited stock available."
    ]
    return random.choice(mock_ads)