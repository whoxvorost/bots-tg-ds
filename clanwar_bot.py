import telebot
import time
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running", 200

BOT_TOKEN = os.getenv('BOT_TOKEN', '7601073026:AAEZHoqcxlQnSvTfCqrvq2LVOhRwXfB3OuY')
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

usernames = [
    "xxvorost", "Matvii9265", "fofmen", "ga_d_zi_la",
    "merlok2_o", "iris_cm_bot", "ammedvedev", "pwixux", "Liubomyr1216",
    "sklianchukk", "LegiShop1", "Just_Nikitka", "zzooipdf", "Courage_Hi",
    "Sasha8763", "zhuchochik", "xxknows", "tiptifri", "Vovcikstec", "chaosCEO",
    "cryptomecenat", "x8x8l", "fraudhoax", "Sn1xxy", "Bob22iv", "tren_bolo_ne",
    "facelessBathory", "illia_ter", "Ar0d000", "Gfhtow", "voxlybot"
]

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
            bot.send_message(chat_id, ", ".join(chunk), parse_mode=None)
            
    except Exception as e:
        print(f"Error in handler: {e}")

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    print("🟢 Starting bot...")
    
    # Додаткове очищення перед запуском
    bot.delete_webhook()
    time.sleep(5)  # Збільшена затримка
    
    # Запускаємо Flask у окремому потоці
    import threading
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Основний цикл бота з більшою затримкою
    while True:
        try:
            print("🔄 Starting polling...")
            bot.polling(none_stop=True, interval=5, timeout=90)  # Збільшені таймаути
        except Exception as e:
            print(f"🔴 Bot crashed: {e}")
            print("🔄 Restarting in 30 seconds...")
            time.sleep(30)  # Збільшена затримка перезапуску