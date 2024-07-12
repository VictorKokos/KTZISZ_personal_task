# main.py
import telebot
from telebot import types
from database import get_session, Document  # Импорт функции get_session

# Токен вашего бота
BOT_TOKEN = 'secret_token'

# Создаем объект бота
bot = telebot.TeleBot(BOT_TOKEN)

# Функция создания меню
def create_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    item1 = types.KeyboardButton('Читать документы')
    item2 = types.KeyboardButton('Ответы на вопросы')
    item3 = types.KeyboardButton('Смотреть наши видео')  # Новая кнопка
    markup.add(item1, item2, item3)  # Добавляем кнопку в меню
    return markup

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! 👋 Выберите действие из нижней панели", reply_markup=create_menu())

# Обработчик выбора "Читать документы"
@bot.message_handler(func=lambda message: message.text == 'Читать документы')
def show_documents(message):
    bot.reply_to(message, "Вот список документов, которые вы можете открыть:", reply_markup=create_menu())

    # Получаем сессию
    session = get_session() 
    # Получаем список документов из базы данных
    documents = session.query(Document).all()

    # Отправляем список документов
    for document in documents:
        bot.send_message(message.chat.id, f"<a href='{document.link}'>{document.title}</a>", parse_mode="HTML")
    session.close()

# Обработчик выбора "Ответы на вопросы"
@bot.message_handler(func=lambda message: message.text == 'Ответы на вопросы')
def start_chat(message):
    bot.reply_to(message, "Задайте свой вопрос:", reply_markup=create_menu())


# Обработчик выбора "Смотреть видео"
@bot.message_handler(func=lambda message: message.text == 'Смотреть наши видео')
def send_playlist_videos(message):
    video_url = 'https://youtube.com/playlist?list=PLHeepYrE_oeE8ieiv8z57kK4H6m6hfsti&si=XgTQZPzdOLhIBb2N'

    # Отправка сообщения с видео
    bot.send_message(message.chat.id, video_url) 
# Запуск бота
bot.polling() 