# Personal AI Assistant (Telegram)

A personalized AI assistant powered by GPT-3.5-turbo that lives in Telegram. It's designed to be your helpful companion for various tasks, conversations, and creative endeavors.

## Features

- 🧠 Intelligent conversations using GPT-3.5-turbo
- 👥 Personalized interactions (remembers and uses your name)
- 💭 Conversation memory (maintains context of last 10 messages)
- 😊 Natural, friendly communication style with emojis
- 🔄 Easy conversation management with /new command

## Prerequisites

- Python 3.7 or higher
- A Telegram account
- Telegram Bot Token (from @BotFather)
- OpenAI API Key (from OpenAI platform)

## Setup

1. Clone this repository:

```bash
git clone <your-repo-url>
cd Python-chatbot
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Configure your assistant:
   - Add your Telegram Bot Token to `.env` (get it from @BotFather)
   - Add your OpenAI API Key to `.env` (get it from https://platform.openai.com/api-keys)

## Starting Your Assistant

Run this command in your terminal:

```bash
python bot.py
```

## Interacting With Your Assistant

Your AI assistant is designed to be conversational and helpful. You can:

- 👋 Send `/start` to begin chatting
- ❓ Use `/help` to see what it can do
- 🔄 Use `/new` to start a fresh conversation
- 💬 Simply chat naturally about anything!

## Capabilities

Your assistant can help with:

1. **Writing & Editing**

   - Content creation
   - Proofreading
   - Suggestions and improvements

2. **Analysis & Research**

   - Information gathering
   - Data interpretation
   - Explaining complex topics

3. **Creative Tasks**

   - Brainstorming ideas
   - Problem-solving
   - Creative writing

4. **General Assistance**
   - Answering questions
   - Providing explanations
   - Friendly conversation

## Customization

You can personalize your assistant by:

1. Modifying the system message in `handle_message()`
2. Adjusting conversation style and emoji usage
3. Adding new commands or features
4. Customizing response parameters

## Error Handling

Your assistant includes:

- Friendly error messages
- Automatic recovery suggestions
- Logging for troubleshooting

## Security

- Never share your API keys
- Keep your `.env` file private
- Regularly monitor usage

## Contributing

Feel free to enhance your assistant! Pull requests are welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Code Overview

### 1. `.env` File

This file stores your sensitive API keys and tokens. It should never be shared publicly. It contains:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token from @BotFather.
- `GEMINI_API_KEY`: Your Gemini (Google AI) API key.

### 2. `requirements.txt`

Lists all Python dependencies needed for the project:

- `python-telegram-bot`: Telegram bot framework.
- `python-dotenv`: Loads environment variables from `.env`.
- `requests`: For making HTTP requests to the Gemini API.
- `pytz`: Timezone support (not currently used, but may be useful for future features).
- `openai`: OpenAI API client (not used in current code, but can be used for GPT models).

### 3. `bot.py`

This is the main bot script. Here’s a breakdown of its structure:

#### Imports

- `os`, `logging`: Standard Python modules for environment and logging.
- `dotenv.load_dotenv`: Loads environment variables from `.env`.
- `telegram`, `telegram.ext`: Telegram bot API and framework.
- `requests`: For making API calls to Gemini.

#### Environment Setup

- Loads environment variables for API keys.
- Sets up Gemini API endpoint and headers.

#### Logging

- Configures logging for debugging and monitoring.

#### Command Handlers

- `start_command`: Greets the user and introduces the bot.
- `help_command`: Explains what the bot can do and available commands.
- `new_conversation`: Clears the conversation history for a fresh start.

#### Message Handler

- `handle_message`: Handles all user messages.
  - Maintains a message history (last 10 messages) for context.
  - Builds a prompt for Gemini, including the user’s name and conversation history.
  - Sends the prompt to Gemini API and returns the AI’s response.
  - Handles errors gracefully and logs them.

#### Main Function

- Loads tokens from environment variables.
- Checks for required keys and raises an error if missing.
- Sets up the Telegram bot application and adds all handlers.
- Starts polling for messages.

#### Error Handling

- If the Gemini API fails, the bot sends a friendly error message and logs details for troubleshooting.

---

For more details, see comments in the code or refer to each section above for a high-level understanding of how the bot works.
