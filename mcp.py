from bots import run_bot, get_bot_names
from memory import get_chat_history, append_message

def choose_bot(user_msg: str) -> str:
    msg = user_msg.lower()
    if "explain" in msg or "teach" in msg or "how to" in msg:
        return "teacher"
    if "summarize" in msg or "summary" in msg or "document" in msg or "paste" in msg:
        return "doc-bot"
    if "joke" in msg or "fun" in msg:
        return "fun"
    return "general"

def handle_message(user_id: str, user_msg: str):

    # decide which bot to use
    bot = choose_bot(user_msg)

    # load that bot's chat history
    history = get_chat_history(user_id, bot)

    #run the bot
    bot_reply = run_bot(bot, history, user_msg)

    #save both user and bot messages
    append_message(user_id, bot, "user", user_msg)
    append_message(user_id, bot, "assistant", bot_reply)

    return bot, bot_reply