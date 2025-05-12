import telebot

BOT_TOKEN = '7601073026:AAGNyoBtTMmQIr7FgRfeC8iPTofv-36doh0'

if BOT_TOKEN == 'YOUR_BOT_TOKEN':
    print("ПОМИЛКА: Будь ласка, замініть 'YOUR_BOT_TOKEN' на токен вашого бота!")
    print("Бот не запуститься без дійсного токена.")
    exit()

bot = telebot.TeleBot(BOT_TOKEN)

provided_usernames = [
    "r3gz00", "xxvorost", "Matvii9265", "fofmen", "ga_d_zi_la",
    "merlok2_o", "iris_cm_bot", "ammedvedev", "pwixux", "Liubomyr1216",
    "sklianchukk", "LegiShop1", "Just_Nikitka", "zzooipdf", "Courage_Hi",
    "Sasha8763", "zhuchochik", "xxknows", "tiptifri", "Vovcikstec", "chaosCEO",
    "cryptomecenat", "x8x8l", "fraudhoax", "Sn1xxy", "Bob22iv", "tren_bolo_ne",
    "facelessBathory", "illia_ter", "Ar0d000", "Gfhtow", "r3gz00", "Matvii9265",
    "fofmen", "ga_d_zi_la", "merlok2_o", "iris_cm_bot", "ammedvedev", "pwixux",
    "Liubomyr1216", "sklianchukk", "LegiShop1", "Just_Nikitka", "zzooipdf",
    "Courage_Hi", "Sasha8763", "zhuchochik", "xxknows", "tiptifri", "voxlybot" # Додав voxlybot, Mementioner пропущено
]

excluded_usernames = ["r3gz00", "Fantom_chekk"]

cleaned_usernames = list(set(provided_usernames) - set(excluded_usernames))

@bot.message_handler(commands=['clanwar'], chat_types=['group', 'supergroup'])
def send_clanwar_announcement_in_chunks(message):
    chat_id = message.chat.id

    announcement_text = "⚔️ CLAN WAR БЛЯДИ ⚔️\n" \
                        "ВСЕ НАХУЙ АТАЧИТЬ ПОШЛИ!"

    try:
        bot.send_message(chat_id, announcement_text)
        print(f"Надіслано основне оголошення у чат ID: {chat_id}")
    except Exception as e:
        print(f"Помилка надсилання основного оголошення у чат ID {chat_id}: {e}")

    mentions = []
    for username in cleaned_usernames:
        mentions.append(f"@{username}")

    chunk_size = 5
    for i in range(0, len(mentions), chunk_size):
        chunk = mentions[i:i + chunk_size]
        chunk_text = ", ".join(chunk)

        try:
            bot.send_message(chat_id, chunk_text, parse_mode='MarkdownV2')
            print(f"Надіслано частину згадок ({i//chunk_size + 1}) у чат ID: {chat_id}")
        except Exception as e:
            print(f"Помилка надсилання частини згадок ({i//chunk_size + 1}) у чат ID {chat_id}: {e}")
            try:
                bot.send_message(chat_id, chunk_text)
                print(f"Надіслано частину згадок ({i//chunk_size + 1}) як звичайний текст у чат ID: {chat_id}")
            except Exception as e2:
                print(f"Повторна помилка надсилання частини згадок ({i//chunk_size + 1}, як звичайний текст) у чат ID {chat_id}: {e2}")


print("Бот запущено. Очікую повідомлень...")
try:
    bot.polling(none_stop=True, interval=0)
except Exception as e:
    print(f"Сталася помилка під час роботи бота: {e}")
    print("Бот зупинено. Можливо, проблема з токеном або підключенням.")