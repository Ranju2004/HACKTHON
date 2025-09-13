import json
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "Your Telegram Bot Token"
LOG_FILE = "log.txt"
DATA_FILE = "data.json"

# Load JSON database
with open(DATA_FILE, "r", encoding="utf-8") as f:
    db = json.load(f)

# ---------------- Logging ----------------
def save_log(user, role, text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {user} ({role}): {text}\n")

# ---------------- Search Functions ----------------
def search_by_mobile(mobile):
    mobile = mobile.strip().replace(" ", "")
    for record in db:
        if record.get("mobile") and mobile in record["mobile"].replace(" ", ""):
            return record
    return None

def search_by_email(email):
    email = email.strip().lower()
    for record in db:
        if record.get("email") and email == record["email"].lower():
            return record
    return None

def search_by_id(id_number):
    id_number = id_number.strip()
    for record in db:
        if record.get("id_number") and id_number == record["id_number"]:
            return record
    return None

def search_by_name(name):
    name = name.strip().lower()
    for record in db:
        if record.get("name") and name in record["name"].lower():
            return record
    return None

# ---------------- Format Result ----------------
def format_record(record):
    return (
        f"✅ Record Found:\n"
        f"Name: {record.get('name','')}\n"
        f"Father: {record.get('father_name','')}\n"
        f"Mobile: {record.get('mobile','')}\n"
        f"Alt: {record.get('alt_mobile','')}\n"
        f"Address: {record.get('address','')}\n"
        f"Circle: {record.get('circle','')}\n"
        f"ID: {record.get('id_number','')}\n"
        f"Email: {record.get('email','')}"
    )

# ---------------- Bot Commands ----------------
def start(update, context):
    user = update.message.from_user.username or update.message.from_user.first_name
    reply = "👋 Welcome! Use /help to see available features."
    update.message.reply_text(reply)
    save_log(user, "BOT", reply)

def help_command(update, context):
    user = update.message.from_user.username or update.message.from_user.first_name
    reply = (
        "📖 Bot Help Menu\n\n"
        "Available commands:\n"
        "👉 /start - Welcome message\n"
        "👉 /help - Show this help menu\n"
        "👉 /checkphone <number> - Search by phone number\n"
        "👉 /checkemail <email> - Search by email\n"
        "👉 /checkid <id_number> - Search by ID number\n"
        "👉 /checkname <name> - Search by name (partial match allowed)\n"
    )
    update.message.reply_text(reply)
    save_log(user, "BOT", reply)

def check_phone(update, context):
    user = update.message.from_user.username or update.message.from_user.first_name
    text = " ".join(context.args)
    save_log(user, "USER", text)

    if not text:
        reply = "❌ Please provide a phone number. Example: /checkphone 9876543210"
    else:
        record = search_by_mobile(text)
        reply = format_record(record) if record else f"❌ No record found for {text}"

    update.message.reply_text(reply)
    save_log(user, "BOT", reply)

def check_email(update, context):
    user = update.message.from_user.username or update.message.from_user.first_name
    text = " ".join(context.args)
    save_log(user, "USER", text)

    if not text:
        reply = "❌ Please provide an email. Example: /checkemail test@mail.com"
    else:
        record = search_by_email(text)
        reply = format_record(record) if record else f"❌ No record found for {text}"

    update.message.reply_text(reply)
    save_log(user, "BOT", reply)

def check_id(update, context):
    user = update.message.from_user.username or update.message.from_user.first_name
    text = " ".join(context.args)
    save_log(user, "USER", text)

    if not text:
        reply = "❌ Please provide an ID number. Example: /checkid 1234567890"
    else:
        record = search_by_id(text)
        reply = format_record(record) if record else f"❌ No record found for {text}"

    update.message.reply_text(reply)
    save_log(user, "BOT", reply)

def check_name(update, context):
    user = update.message.from_user.username or update.message.from_user.first_name
    text = " ".join(context.args)
    save_log(user, "USER", text)

    if not text:
        reply = "❌ Please provide a name. Example: /checkname Ram"
    else:
        record = search_by_name(text)
        reply = format_record(record) if record else f"❌ No record found for {text}"

    update.message.reply_text(reply)
    save_log(user, "BOT", reply)

# ---------------- Main ----------------
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("checkphone", check_phone))
    dp.add_handler(CommandHandler("checkemail", check_email))
    dp.add_handler(CommandHandler("checkid", check_id))
    dp.add_handler(CommandHandler("checkname", check_name))

    # Log any other text
    def log_text(update, context):
        user = update.message.from_user.username or update.message.from_user.first_name
        text = update.message.text
        reply = "ℹ️ Please use /help to see available commands."
        update.message.reply_text(reply)
        save_log(user, "USER", text)
        save_log(user, "BOT", reply)

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, log_text))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
