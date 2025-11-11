import os
import json

MEMORY_PATH = "data/memory.json"

def _ensure_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, 'w') as f:
            json.dump({}, f)

def load_memory():
    _ensure_file()
    with open(MEMORY_PATH, 'r') as f:
        return json.load(f)

def save_memory(mem):
    with open(MEMORY_PATH, 'w') as f:
        json.dump(mem, f, indent=2)

def get_chat_history(user_id: str, bot_name: str):
    mem = load_memory()
    return mem.get(user_id, {}).get(bot_name, [])

def append_message(user_id: str, bot_name: str, role: str, content: str):
    mem = load_memory()
    if user_id not in mem:
        mem[user_id] = {}
    if bot_name not in mem[user_id]:
        mem[user_id][bot_name] = []
    mem[user_id][bot_name].append({"role": role, "content": content})
    save_memory(mem)