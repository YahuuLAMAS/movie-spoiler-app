from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
model.load_state_dict(torch.load('best_model.pt'))  # After you train & save

def is_spoiler(comment, threshold=0.8):
    spoiler_keywords = ['villain', 'betrayal', 'secret', 'ending', 'dies', 'identity', 'twist', 'sacrifice']
    comment_lower = comment.lower()
    inputs = tokenizer(comment, return_tensors='pt', truncation=True, padding=True, max_length=256)
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    spoiler_prob = probs[0][1].item()
    return spoiler_prob >= threshold
