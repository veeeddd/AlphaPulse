from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
from config import MODEL_NAME

class SentimentEngine:
    def __init__(self):
        print(f"[*] Loading model: {MODEL_NAME}...")
        # Load the specialized FinBERT tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        self.labels = ["positive", "negative", "neutral"]

    def analyze_sentiment(self, text):
        """Processes text and returns sentiment probabilities."""
        # Tokenize the headline
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        
        # Run Inference
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Convert raw output (logits) to probabilities
        probs = F.softmax(outputs.logits, dim=-1)
        
        # Get the highest probability label
        best_index = torch.argmax(probs).item()
        confidence = probs[0][best_index].item()
        
        return {
            "sentiment": self.labels[best_index],
            "confidence": confidence,
            "probs": probs[0].tolist() # [pos, neg, neu]
        }

if __name__ == "__main__":
    # Quick Test
    engine = SentimentEngine()
    test_headline = "NVIDIA stocks surge as AI demand reaches all-time high."
    result = engine.analyze_sentiment(test_headline)
    
    print(f"\nHeadline: {test_headline}")
    print(f"Result: {result['sentiment'].upper()} ({result['confidence']:.2%} confidence)")