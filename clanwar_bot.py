import telebot
import time
import os
from flask import Flask, request
import threading

# Flask app for health checks
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Bot is running!", 200

# Token
BOT_TOKEN = os.getenv('BOT_TOKEN', '7601073026:AAEZHoqcxlQnSvTfCqrvq2LVOhRwXfB3OuY')
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

# Usernames list
usernames = [
    "xxvorost", "Matvii9265", "fofmen", "ga_d_zi_la",
    "merlok2_o", "iris_cm_bot", "ammedvedev", "pwixux", "Liubomyr1216",
    "sklianchukk", "LegiShop1", "Just_Nikitka", "zzooipdf", "Courage_Hi",
    "Sasha8763", "zhuchochik", "xxknows", "tiptifri", "Vovcikstec", "chaosCEO",
    "cryptomecenat", "x8x8l", "fraudhoax", "Sn1xxy", "Bob22iv", "tren_bolo_ne",
    "facelessBathory", "illia_ter", "Ar0d000", "Gfhtow", "voxlybot"
]

# Handler for /clanwar command in group chats
@bot.message_handler(commands=['clanwar'], chat_types=['group', 'supergroup'])
def send_clanwar_announcement(message):
    try:
        chat_id = message.chat.id
        announcement = "⚔️ CLAN WAR ⚔️\n! Проводим атаки, мінімум 1600 медалей за кв !"
        bot.send_message(chat_id, announcement)

        mentions = [f"@{username}" for username in usernames]
        chunk_size = 5

        for i in range(0, len(mentions), chunk_size):
            chunk = mentions[i:i + chunk_size]
            bot.send_message(chat_id, ", ".join(chunk))
            time.sleep(1)  # антифлуд-пауза

    except Exception as e:
        print(f"❌ Error in /clanwar handler: {e}")

# Run Flask app
def run_flask():
    port = int(os.environ.get("PORT", 8080))  # підтримка змінної PORT
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    print("🟢 Starting bot...")

    # Очищення вебхука (на випадок зміни режиму роботи)
    bot.delete_webhook()
    time.sleep(3)

    # Flask у фоні
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Polling (нескінченний цикл)
    while True:
        try:
            print("🔁 Bot polling started.")
            bot.polling(non_stop=True, interval=2, timeout=30)
        except Exception as e:
            print(f"🔴 Bot crashed with error: {e}")
            print("⏳ Restarting in 30 seconds...")
            time.sleep(30)
