from telegram.ext import CommandHandler, Application
import logging
from telegram import Update
import random

token = '6759603718:AAGy6E4nvXP53jbSCU1mUMNL7awkTAlt1_I'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def start(update: Update, context: Application):

    welcome_message = "🤖 Welcome to the Donation Bot!\n\n" \
                      "I am here to help you make a difference through donations. " \
                      "Click the buttons below to explore the available options:\n\n" \
                      "💸 /donate - Make a donation\n" \
                      "❓ /help - Get assistance with using the bot"

    await update.message.reply_text(welcome_message)


async def donate(update: Update, context: Application):
    # Generate a 6-digit code
    deposit_code = ''.join(random.choice('0123456789') for _ in range(6))

    # Construct the donation URL with the deposit code
    donation_url = f"http://127.0.0.1:8000/deposit/{deposit_code}"

    # Construct the reply message
    reply_message = (
        f"📥 Please donate at least 0.033 SOL at: {donation_url}\n"
        f"🔑 Deposit code: {deposit_code}\n\n"
        "🔥 Thank you for choosing to make a donation!\n"
    )

    # Reply to the user with the generated message
    await update.message.reply_text(reply_message)


async def help_command(update: Update, context: Application):
    await update.message.reply_text("I am here to help! How can I assist you?")

if __name__ == '__main__':
    app = Application.builder().token(token).build()

    # Correctly add handlers and store them in variables
    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help_command)
    donate_handler = CommandHandler("donate", donate)

    # Add handlers to the Application context
    app.add_handler(start_handler)
    app.add_handler(help_handler)
    app.add_handler(donate_handler)

    # Run the polling
    app.run_polling()
