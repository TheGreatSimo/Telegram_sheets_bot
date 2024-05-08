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
        ["🍔 Food", "✈️  Travel" ],
        ["👥 Staff", "🏡 Rent"],
        ["💻 Software", "💃 Women"]
    ]
    
    # Create a ReplyKeyboardMarkup with buttons for each command
    reply_markup = ReplyKeyboardMarkup(commands)

    # Reply with the keyboard
    await message.reply_text("Hey bro I'm your bot \nI'll take care of all your expenses", reply_markup=reply_markup)

# Define event handlers for each command
@app.on_message(filters.text & filters.private)
async def handle_commands(client, message):
    if message.text == "🍔 Food":
        await message.reply_text("How much did you pay for food?")

    elif message.text == "✈️  Travel":
        await message.reply_text(":w")
    elif message.text == "📅 Orders":
        await message.reply_text("You chose Orders  but I can't write it but I can't add it to Excel because I still don't know the instructions yet.")
    elif message.text == "🛒 Cart":
        await message.reply_text("You chose Cart but I can't write it but I can't add it to Excel because I still don't know the instructions yet. ")
    elif message.text == "☎️ Support":
        await message.reply_text("You chose Support but I can't write it but I can't add it to Excel because I still don't know the instructions yet. ")
    elif message.text == "💬 Channel":
        await message.reply_text("You chose Channel but I can't write it but I can't add it to Excel because I still don't know the instructions yet. ")
    else:
        await message.reply_text("Bro I can't answer you that right now")

# Run the client
app.run()

