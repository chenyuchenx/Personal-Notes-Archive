import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
import numpy as np

model_name = "gpt2-medium" 
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

for param in model.parameters():
    param.requires_grad = False
    
num_virtual_tokens = 20  # 虛擬 token 數量
prompt_embeddings = torch.nn.Embedding(num_virtual_tokens, model.config.n_embd)
torch.nn.init.normal_(prompt_embeddings.weight, std=0.02)

# 前向傳播
def forward(input_ids, attention_mask=None, labels=None):
    batch_size = input_ids.shape[0]
    prompt_embeds = prompt_embeddings.weight.repeat(batch_size, 1, 1)
    inputs_embeds = model.transformer.wte(input_ids)
    inputs_embeds = torch.cat([prompt_embeds, inputs_embeds], dim=1)
    
    outputs = model(inputs_embeds=inputs_embeds, attention_mask=attention_mask, labels=labels)
    return outputs

def prepare_dataset(subject):
    if subject == "math":
        questions = ["求解方程：2x + 5 = 15", "計算圓的面積，半徑為 3"]
        answers = ["將 5 移到等式右邊：2x = 10，然後除以 2：x = 5", "使用公式 A = πr²，代入 r = 3，得到 A = 9π ≈ 28.27"]
    elif subject == "science":
        questions = ["解釋光合作用", "牛頓第二運動定律是什麼？"]
        answers = ["光合作用是植物利用陽光、水和二氧化碳製造葡萄糖的過程", "物體的加速度與所受的合外力成正比，與質量成反比"]
    
    return [f"問題：{q}\n答案：{a}" for q, a in zip(questions, answers)]

def train_prompt(subject):
    dataset = prepare_dataset(subject)
    encoded_dataset = tokenizer(dataset, truncation=True, padding="max_length", max_length=512)
    
    train_args = TrainingArguments(
        output_dir=f"./results_{subject}",
        num_train_epochs=5,
        per_device_train_batch_size=4,
        learning_rate=1e-3,
        save_steps=100,
    )
    
    trainer = Trainer(
        model=model,
        args=train_args,
        train_dataset=encoded_dataset,
    )
    
    trainer.train()

subjects = ["math", "science", "history"]
for subject in subjects:
    train_prompt(subject)
    
def generate_answer(subject, question):
    prompt_embeds = prompt_embeddings.weight.unsqueeze(0)
    input_ids = tokenizer.encode(question, return_tensors="pt")
    
    with torch.no_grad():
        output = model.generate(
            inputs_embeds=torch.cat([prompt_embeds, model.transformer.wte(input_ids)], dim=1),
            max_length=150,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
        )
    
    return tokenizer.decode(output[0], skip_special_tokens=True)

print(generate_answer("math", "如何解一元二次方程？"))
print(generate_answer("science", "什麼是DNA？"))
