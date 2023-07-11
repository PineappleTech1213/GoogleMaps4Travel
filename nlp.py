#import huggingface related libraries
import torch
from transformers import AutoTokenizer, BertForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("textattack/bert-base-uncased-yelp-polarity")
model = BertForSequenceClassification.from_pretrained("textattack/bert-base-uncased-yelp-polarity")
tweets= ['hello world',' i hate this world','i love this world']
inputs = tokenizer(tweets,padding=True,truncation=True, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

print(logits.argmax(dim=1)) # [1,0,1]
predicted_class_id = logits.argmax().item() # 5 (the index of the class with the highest score)
print(predicted_class_id)

# To train a model on `num_labels` classes, you can pass `num_labels=num_labels` to `.from_pretrained(...)`
num_labels = len(model.config.id2label) # 2
model = BertForSequenceClassification.from_pretrained("textattack/bert-base-uncased-yelp-polarity", num_labels=num_labels)
#change the labels to the correct number of labels

labels = torch.tensor([1]* len(tweets))
loss = model(**inputs, labels=labels).loss

print(loss.item())