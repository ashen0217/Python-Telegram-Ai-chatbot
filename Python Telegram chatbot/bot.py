import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

# Load environment variables
load_dotenv()

# Gemini API endpoint and key
gemini_api_key = os.getenv('GEMINI_API_KEY')
gemini_url = 'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent'
headers = {'Content-Type': 'application/json'}

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    welcome_message = f"Hi {user_name}! 👋 I'm your personal AI assistant. I'm here to help you with anything you need - whether it's writing, analysis, answering questions, or just having a conversation. What can I help you with today?"
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = f"""I'm your personal AI assistant, and I'm here to help you with various tasks like:

🤔 Answering questions and providing explanations
✍️ Writing and editing assistance
💡 Brainstorming and creative ideas
🔍 Research and analysis
💬 General conversation and discussion

You can simply chat with me naturally, or use these commands:
/start - Start a fresh conversation
/help - See this help message
/new - Start a new conversation thread

Just talk to me like you would to a friend - I'm here to help!"""
    await update.message.reply_text(help_text)

async def new_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'messages' in context.user_data:
        context.user_data['messages'] = []
    await update.message.reply_text("Let's start fresh! What's on your mind?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    text = update.message.text

    # Initialize message history if it doesn't exist
    if 'messages' not in context.user_data:
        context.user_data['messages'] = []

    # Add user message to history
    context.user_data['messages'].append({"role": "user", "content": text})

    # Keep only last 10 messages to avoid hitting context limits
    if len(context.user_data['messages']) > 10:
        context.user_data['messages'] = context.user_data['messages'][-10:]

    try:
        # Prepare Gemini prompt
        prompt = f"You are a helpful and friendly AI assistant talking to {user_name}. Be conversational, empathetic, and natural in your responses. Avoid being too formal or robotic. When appropriate, use emojis to make the conversation more engaging. If you're not sure about something, be honest about it.\n" + "\n".join([m['content'] for m in context.user_data['messages'] if m['role'] == 'user'])
        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        params = {'key': gemini_api_key}
        response = requests.post(gemini_url, headers=headers, params=params, json=data)
        response.raise_for_status()
        result = response.json()
        ai_response = result['candidates'][0]['content']['parts'][0]['text']
        context.user_data['messages'].append({"role": "assistant", "content": ai_response})
        await update.message.reply_text(ai_response)
    except Exception as e:
        # Log the full response if available
        if 'response' in locals():
            logging.error(f"Gemini API response: {response.text}")
        logging.error(f"Error in message handler: {str(e)}")
        await update.message.reply_text(
            f"I apologize, {user_name}, but I encountered a technical issue. Could you try asking me again in a different way?"
        )

def main():
    # Get tokens from environment variables
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
        raise ValueError('Required environment variables are missing')

    # Create application
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('new', new_conversation))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    print('Starting your AI assistant...')
    app.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()