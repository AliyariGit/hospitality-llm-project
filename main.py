from transformers import pipeline

# Load a pre-trained model and tokenizer 
model_name ="distilbert-base-uncased"
nlp=pipeline("sentiment-analysis", model=model_name)

# Define a simple function to analyze text
def analyze_text(text):
    return nlp(text)

if __name__ =="__name__":
    text="this is sample text for sentiment analysis."
    result =analyze_text(text)
    print(result)


