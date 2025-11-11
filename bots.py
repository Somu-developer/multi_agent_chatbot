from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load Once

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, 
    torch_dtype=torch.float16, 
    device_map="auto" if torch.cuda.is_available() else None
)

def generate_reply(system_prompt: str, history: list, user_msg: str, max_new_tokens=200):
    messages = []
    if system_prompt:
        messages.append(f"System: {system_prompt}")
    for turn in history:
        messages.append(f"{turn['role'].capitalize()}: {turn['content']}")
    messages.append(f"User: {user_msg}")
    messages.append("Assistant:")

    full_prompt = "\n".join(messages)
    inputs = tokenizer(full_prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]

    outputs = model.generate(
        input_ids=input_ids,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # 1. keep only what the assistant said
    if "Assistant:" in decoded:
        decoded = decoded.split("Assistant:")[-1].strip()

    # 2. if the model started a new "User:" turn, cut it off
    if "User:" in decoded:
        decoded = decoded.split("User:")[0].strip()

    return decoded

BOTS = {
    "General": "You are a helpful general assistant.",
    "teacher": "You explain things simply with short examples.",
    "doc-bot": "You help users extract and summarize info from long texts they paste.",
    "fun": "You reply in a playful tone."
}

def get_bot_names():
    return list(BOTS.keys())

def run_bot(bot_name: str, history: list, user_msg: str):
    system_prompt = BOTS.get(bot_name, BOTS["General"])
    return generate_reply(system_prompt, history, user_msg)