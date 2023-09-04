import logging
import os
from os.path import join, dirname

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

load_dotenv()

def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)

my_token = get_from_env('TG_BOT_TOKEN')


my_github = 'https://github.com/vikagrshkYaP/bot-vkgrshk'
telegram_chat_id = os.getenv('telegram_chat_id')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def bot_menu(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([['/my_photo', '/my_old_photo', '/my_hobby'],
                                  ['/my_first_love',
                                   '/what_is_GPT',
                                   '/SQL_vs_NoSQL']],
                                  resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Итак, {}, вот некоторая информация про меня :).'.format(name),
        reply_markup=buttons
    )



def hello(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([['/my_photo', '/my_old_photo'],
                                  ['/my_hobby']],
                                  resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Будем знакомы! '
        'Предлагаю узнать меня получше'.format(name),
        reply_markup=buttons
    )
    
    
def goodbye(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(chat_id=chat.id,
                             text='{}, была рада рассказать о себе подробнее!'.format
                             (name))
    
def selfie(update, context):
    chat = update.effective_chat
    my_photo = open('photo/my_photo.png', 'rb')
    context.bot.send_photo(chat.id, my_photo)
    button = ReplyKeyboardMarkup([['/my_old_photo',
                                   '/my_hobby']],
                                 resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Это мое недавнее фото.',
        reply_markup=button
    )


def photo_11(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    my_old_photo = open('photo/old_photo.png', 'rb')
    button_2 = ReplyKeyboardMarkup([['/my_hobby']], resize_keyboard=True)
    context.bot.send_photo(chat.id, my_old_photo)
    context.bot.send_message(
        chat_id=chat.id,
        text='{}, а так я выглядела в 11 классе.'.format(name),
        reply_markup=button_2
    )


def hobby(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([['/my_first_love', '/what_is_GPT'],
                                  ['/SQL_vs_NoSQL']],
                                  resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text='Недавно я стала настоящим сникерхедом - теперь это моя страсть. В моей коллекции уже около 50 пар кроссовок, и она продолжает пополняться',
        reply_markup=buttons
    )
    context.bot.send_message(
        chat_id=chat.id,
        text='Также можешь послушать несколько аудио: различие SQL и NoSQL баз данных, понятное объяснение GPT, а также историю о моей первой любви',
        reply_markup=buttons
    )


def send_love_story(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([['/what_is_GPT']],
                                  resize_keyboard=True)
    context.bot.send_audio(chat.id, open('audio/my_first_love.wav',
                                         'rb'))
    photo_Batu = open('photo/batu.png', 'rb')
    context.bot.send_photo(chat.id, photo_Batu)
    context.bot.send_message(
        chat_id=chat.id,
        text='Моя история довольно милая :).',
        reply_markup=buttons
    )


def send_gpt_audio(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([['/SQL_vs_NoSQL']],
                                  resize_keyboard=True)
    context.bot.send_audio(chat.id, open('audio/GPT.wav', 'rb'))
    context.bot.send_message(
        chat_id=chat.id,
        text='Такое объяснение GPT поймет даже бабушка :)',
        reply_markup=buttons
    )


def send_sql_audio(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([['/my_photo', '/my_old_photo', '/my_hobby'],
                                  ['/my_first_love',
                                   '/what_is_GPT',
                                   '/SQL_vs_NoSQL',
                                   '/my_github']],
                                  resize_keyboard=True)
    context.bot.send_audio(chat.id, open('audio/SQL.wav', 'rb'))
    context.bot.send_message(
        chat_id=chat.id,
        text='{}, надеюсь, тебе было интересно :).'.format(name),
        reply_markup=buttons
    )


def send_github_link(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(chat_id=chat.id,
                             text='{}, вот ссылка на мой репозиторий с '
                             'исходниками этого бота: '
                             f'{my_github}.'.format(name))




def main():
    updater = Updater(token = my_token)

    updater.dispatcher.add_handler(CommandHandler('start', hello))
    updater.dispatcher.add_handler(CommandHandler('my_photo', selfie))
    updater.dispatcher.add_handler(CommandHandler('my_old_photo', photo_11))
    updater.dispatcher.add_handler(CommandHandler('my_hobby', hobby))
    updater.dispatcher.add_handler(CommandHandler('my_first_love', send_love_story))
    updater.dispatcher.add_handler(CommandHandler('what_is_gpt', send_gpt_audio))
    updater.dispatcher.add_handler(CommandHandler('sql_vs_nosql',send_sql_audio))
    updater.dispatcher.add_handler(CommandHandler('my_github', send_github_link))
    updater.dispatcher.add_handler(CommandHandler('stop', goodbye))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, bot_menu))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()