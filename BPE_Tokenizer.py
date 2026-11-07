from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer

texts=[
    "Hello, how are you?",
    "I am fine, thank you!",
    "What is your name?",
    "My name is Tokenizer.",
    "I can tokenize text using BPE."
]
tokenizer = Tokenizer(BPE())
trainer = BpeTrainer(vocal_size=10000)

#tokenizer.train(["/home/user/corpus.txt"], trainer)
tokenizer.train_from_iterator(texts, trainer)
#output=tokenizer.encode("Hello, how are you?")
#print(output.tokens)
print(tokenizer.encode("machine learning is fun").tokens)