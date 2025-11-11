# 💬 Multi-Agent AI Chatbot (Zero-Budget)

This project is a **multi-bot AI assistant** built completely for free using open-source tools.

It uses:
- 🧠 **Hugging Face open-source LLMs** (e.g., TinyLlama)
- ⚙️ **Streamlit** for the web interface
- 🗃️ **JSON-based persistent memory**
- 🤖 **MCP (Main Control Program)** to decide which bot should reply
- 💡 100% **zero-cost setup** — no OpenAI API, no paid hosting

---

## 🚀 Features

✅ Multiple specialized bots:
- **Teacher Bot** – explains concepts and teaches step-by-step  
- **Doc Bot** – summarizes pasted text  
- **Fun Bot** – tells jokes and lighthearted replies  
- **General Bot** – handles normal questions  

✅ Persistent memory stored in `data/memory.json`  
✅ MCP (Main Control Program) automatically chooses the right bot  
✅ Works **offline** or on **Hugging Face Spaces**  
✅ Fully open source and customizable  

---

## 🧩 Folder Structure

multi_agent_chatbot/
- app.py # Streamlit UI
- bots.py # Bot logic + LLM loading
- mcp.py # Main Control Program (decides which bot to use)
- memory.py # Persistent JSON memory
- requirements.txt # Dependencies
- data/
- memory.json # Created automatically


---

## 🛠️ Installation

1. **Clone the repo**

- git clone https://github.com/<your-username>/multi_agent_chatbot.git
- cd multi_agent_chatbot

2.  **Install dependencies**

pip install -r requirements.txt

3. **Run the app**

streamlit run app.py

- Then open the local URL shown (usually http://localhost:8501).


Example Prompts
🧑‍🏫 Teacher bot

- Teach me 5 English letters and a word for each.
- Explain the difference between “a” and “an”.
- How to form simple present tense sentences?

📄 Doc bot

- Summarise this text in 3 bullet points

😄 Fun bot

- Tell me a joke!
- Write a playful message to my friend.

🧭 General bot

Give me 5 daily English practice ideas.
What can you do?
