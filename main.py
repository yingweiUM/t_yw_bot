import logging
import asyncio
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import streamlit as st

tele_token = st.secrets["tele_token"]

print(tele_token)
st.text(tele_token)

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello world")
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def my_async_function():
    application = ApplicationBuilder().token(tele_token).build()
    start_handler = CommandHandler('start', start)
    hello_handler = CommandHandler('hello', hello)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(hello_handler)
    application.add_handler(echo_handler)
    application.run_polling()

if __name__ == '__main__':
    try:
        asyncio.run(my_async_function())
    except KeyboardInterrupt:
        pass
