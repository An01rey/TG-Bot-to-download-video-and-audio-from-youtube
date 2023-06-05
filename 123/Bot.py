from aiogram import Bot, types, executor, Dispatcher
import logging
import os
from pytube import YouTube

logging.basicConfig(level=logging.INFO)
bot = Bot(token='6020255157:AAEJbNRjg_A8thQ5zIZqvhyK368800sPWbw')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Привет\n bot, который скачивает видео с Ютуба!')


@dp.message_handler(commands=['download_video_youtube'])
async def video(message: types.Message):
    url = message.get_args()
    if len(url) == 0:
        await message.answer('Ссылка отсутсвует. \nПример:\n /download_video_youtube https://www.youtube/_trzqmAhTfs')
    else:
        load = YouTube(url)
        await message.reply('Отправка видео на сервер!')
        video = load.streams.filter(progressive=True, file_extension='mp4')
        video.get_highest_resolution().download(filename='video.mp4')
        await message.reply(f'Начинаю загрузку видео:\n"{load.title}"')
        await message.bot.send_video(chat_id=message.chat.id, video=open('video.mp4', 'rb'), caption='Вот ваше видео')
        os.remove('video.mp4')


@dp.message_handler(commands=['audio_youtube'])
async def video(message: types.Message):
    url = message.get_args()
    if len(url) == 0:
        await message.answer('Ссылка отсутсвует. \nПример:\n /audio_youtube https://www.youtube/_trzqmAhTfs')
    else:
        yt = YouTube(url)
        await message.reply('Отправка аудио на сервер!')
        audio = yt.streams.filter(only_audio=True).first()
        audio.download(filename='audio.mp3')
        await message.reply(f'Начинаю загрузку аудио')
        await message.bot.send_audio(chat_id=message.chat.id, audio=open('audio.mp3', 'rb'), caption='Вот ваше аудио')
        os.remove('audio.mp3')

if __name__ == '__main__':
    executor.start_polling(dp)
