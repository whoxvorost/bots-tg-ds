import telebot
import time
import os

BOT_TOKEN = os.getenv('BOT_TOKEN', '7601073026:AAGNyoBtTMmQIr7FgRfeC8iPTofv-36doh0')
bot = telebot.TeleBot(BOT_TOKEN)

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

def start_bot():
    print("🟢 Starting bot...")
    while True:
        try:
            bot.remove_webhook()
            print("🔄 Webhook removed, starting polling...")
            bot.polling(none_stop=True, interval=2, timeout=30)
        except Exception as e:
            print(f"🔴 Bot crashed: {e}")
            print("🔄 Restarting in 10 seconds...")
            time.sleep(10)

if __name__ == '__main__':
    start_bot()