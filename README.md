# LangchainAI-TelegramBot

LangchainAI-TelegramBot is a bot on Telegram that leverages the OpenAI API along with several other technologies to provide an interactive, AI-driven experience. It utilizes the GPT-3 model for text generation, the DALL-E model for image generation, and other tools for functionalities like web search, Wikipedia search, and advanced mathematical problem-solving.

## Features

- **Text Generation:** The bot generates human-like text with OpenAI's GPT-3 model based on a given prompt.
- **Image Generation:** It uses OpenAI's DALL-E model to generate images from textual descriptions.
- **Web Search:** The bot fetches and presents information from the web.
- **Wikipedia Search:** It accesses Wikipedia to gather and display information.
- **Deep Math:** The bot solves complex mathematical problems using Wolfram Alpha and a math language model.

## Libraries Used

| Library | Description |
| --- | --- |
| `openai` | For generating texts and images using OpenAI's GPT-3 and DALL-E models |
| `aiogram` | A fully asynchronous framework for Telegram Bot API |
| `telegraph` | For creating Telegraph articles |
| `logging` | Standard Python library for generating logging messages |
| `os` | Standard Python library for OS-dependent functionality |
| `wikipedia` | Python wrapper for the Wikipedia API |
| `langchain` | A library developed for language model operations |
| `wolframalpha` | A package for interacting with the Wolfram Alpha API |

## Installation

1. Clone this repository to your local machine using `https://github.com/Illia-the-coder/LangchainAI-TelegramBot.git`.
2. Navigate to the project directory.
3. Install the necessary packages using `pip install -r requirements.txt`.
4. Visit [BotFather](https://t.me/botfather) on Telegram to create a new bot and obtain the API token. Follow the instructions provided by BotFather to set up your bot.
5. Set up the necessary API keys and environment variables. Include the API token you received from BotFather in a `.env` file within your project directory.
6. Run the bot using `python main.py`.

## Usage

The bot responds to several commands. Here are some examples:

- Use `/start` to initiate interaction with the bot.
- Use `/image <description>` to generate an image based on the given description. 
- Use `/search <query>` to search the web and present information related to the query.
- For a full list of commands, use the `/help` command.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
