#!/usr/bin/env python3






from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

# Your Telegram API credentials
api_id = 29920180
api_hash = "26c4b10bde45c44c951900706b2f77b4"
bot_token = "7187067068:AAEdSpJfIJ8aVtfKHkI0KMCuPupCQ71f4g8"


# Create a Pyrogram Client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define the /start command handler
@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Create a list of commands
    commands = [
        ["🛒 Store ", "💸 Wallet" ],
        ["📅 Orders", "🛒 Cart"],
        ["☎️ Support", "💬 Channel"]
    ]
    
    # Create a ReplyKeyboardMarkup with buttons for each command
    reply_markup = ReplyKeyboardMarkup(commands)

    # Reply with the keyboard
    await message.reply_text("Hey bro I'm your bot \nI'll take care of all your expenses", reply_markup=reply_markup)

# Define event handlers for each command
@app.on_message(filters.command("command1"))
async def command1(client, message):
    await message.reply_text("You chose Command 1")

@app.on_message(filters.command("command1"))
async def command2(client, message):
    await message.reply_text("You chose Command 2")

# Define handlers for other commands in a similar way...

# Run the client
app.run()

