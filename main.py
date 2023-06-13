import os
import logging
from aiogram import Bot, Dispatcher, executor, types
import openai

BOT_TOKEN = os.getenv('BOT_TOKEN')
NUM_IMAGES = 3

help_ = """Example of input data from user - 
<b>/image Portret of Elon Musk</b>

Available commands:
/start - starts the bot and prompts the user to input the description
/image - prompts the user to input the description for the image and generates an image based on the description
/about - provides information about the bot and its features
/help - lists all available commands and their usage
/default - default output from gpt_3
/web - default model but with access to web
/wiki - default model but with access to wikipedia
/deep_math - default model but with access to wolfram alpha and math llm
"""

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "/start"}
    ]
)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


def get_image(prompt, num_images=NUM_IMAGES):
    try:
        response = openai.Image.create(prompt=prompt, n=num_images, size="1024x1024")
        return [response["data"][i]["url"] for i in range(num_images)]
    except Exception as e:
        logging.error(f"Error generating image: {e}")
        return None


@dp.message_handler(commands=['web', 'wiki', 'deep_math', 'default'])
async def process_text_generation_command(message: types.Message):
    logging.info("text_generation command received")
    command = message.get_command()
    await bot.send_message(chat_id=message.chat.id, text='Loading...')
    prompt = message.text.replace(command, "")
    text = ''
    tools = []
    
    if command == '/web':
        tools = ["google-serper", 'human']
    elif command == '/wiki':
        tools = ["wikipedia", 'human']
    elif command == '/deep_math':
        tools = ['wolfram-alpha', 'human', "llm-math"]
    elif command == '/default':
        tools = ['human']

    try:
        text = langchain_answer(prompt, tools) if len(prompt) else 'Invalid format. Write info after function'
    except Exception as e:
        text = f'sorry... something went wrong {e}'
    
    await bot.send_message(chat_id=message.chat.id, text=text, parse_mode="HTML")


@dp.message_handler(commands=['image'])
async def process_image_command(message: types.Message):
    logging.info("image command received")
    prompt = message.text.replace("/image", "")
    image_urls = get_image(prompt, num_images=NUM_IMAGES) if len(prompt) else 'Invalid format. Write info after function'
    
    if image_urls is None:
        await bot.send_message(chat_id=message.chat.id, text="An error occurred while generating the image.")
    
    for url in image_urls:
        await bot.send_photo(chat_id=message.chat.id, photo=url, caption=prompt)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    logging.info("/start command received")
    await bot.send_message(chat_id=message.chat.id, text="Please use /help to see next steps. \nAlso, you can use /about to see info about the bot.")


@dp.message_handler(commands=['about'])
async def process_about_command(message: types.Message):
    logging.info("/about command received")
    await bot.send_message(chat_id=message.chat.id, text="This is an example bot that generates images and text based on a user's description. It uses OpenAI's image generation and text generation API.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    logging.info("/help command received")
    await bot.send_message(chat_id=message.chat.id, text=help_, parse_mode="HTML")


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
