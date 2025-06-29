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