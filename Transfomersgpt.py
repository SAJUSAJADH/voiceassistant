from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def generate_response(query):
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    inputs = tokenizer.encode(query, return_tensors='pt')
    attention_mask = torch.ones_like(inputs)

 
    outputs = model.generate(
        inputs,
        attention_mask=attention_mask,
        max_length=100,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_p=0.95,
        temperature=0.75,
        do_sample=True,  
        pad_token_id=tokenizer.eos_token_id
    )

    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if response.startswith(query):
        response = response[len(query):].strip()
    
    return response

