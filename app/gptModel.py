import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class MyModel():
    def __init__(self):
        self.model_name = "ai-forever/rugpt3medium_based_on_gpt2"
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)

    def gen_short_text(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        out = self.model.generate(
                input_ids,
                max_length=300,
                repetition_penalty=5.0,
                do_sample=True,
                top_k=5, top_p=0.95, temperature=0.95,
                num_beams=10, no_repeat_ngram_size=3
        )
        return self.post_process(out)

    def gen_long_text(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        out = self.model.generate(
              input_ids,
              max_length=450,
              min_length=300,
              repetition_penalty=5.0,
              do_sample=True,
              top_k=5, top_p=0.95, temperature=0.95,
              num_beams=10, no_repeat_ngram_size=3
            )
        return self.post_process(out)

    def post_process(self, data):
        generated_text = list(map(self.tokenizer.decode, data))
        generated_text = generated_text[0]
        generated_text = generated_text.replace('\n', '')
        return generated_text