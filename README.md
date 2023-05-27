# LangchainAI-TelegramBot

LangchainAI-TelegramBot is a powerful, feature-rich bot that leverages the capabilities of the OpenAI API along with several other technologies to provide an interactive, AI-driven experience on Telegram. It utilizes the GPT-3 model for text generation, the DALL-E model for image generation, and several other tools for functionalities like web search, Wikipedia search, and advanced mathematical problem-solving.

## Features

- **Text Generation:** The bot uses OpenAI's GPT-3 model to generate human-like text based on a given prompt.
- **Image Generation:** It uses OpenAI's DALL-E model to generate images from textual descriptions.
- **Web Search:** The bot can fetch and present information from the web.
- **Wikipedia Search:** It can access Wikipedia to gather and display information.
- **Deep Math:** The bot has capabilities to solve complex mathematical problems using Wolfram Alpha and a math language model.

## Libraries Used

| Library | Description |
| --- | --- |
| `openai` | Used for generating texts and images using OpenAI's GPT-3 and DALL-E models |
| `aiogram` | A fully asynchronous framework for Telegram Bot API |
| `telegraph` | Used for creating Telegraph articles |
| `logging` | Standard Python library for generating logging messages |
| `os` | Standard Python library for OS-dependent functionality |
| `wikipedia` | Python wrapper for the Wikipedia API |
| `langchain` | A library developed for language model operations |
| `wolframalpha` | A package for interacting with the Wolfram Alpha API |

## Installation

1. Clone this repository to your local machine using `https://github.com/Illia-the-coder/LangchainAI-TelegramBot.git`.
2. Navigate to the project directory.
3. Install the necessary packages using `pip install -r requirements.txt`.
4. Set up the necessary API keys and environment variables.
5. Run the bot using `python main.py`.

## Usage

The bot responds to several commands. For example, use `/image <description>` to generate an image based on the given description. For a full list of commands, use the `/help` command.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
