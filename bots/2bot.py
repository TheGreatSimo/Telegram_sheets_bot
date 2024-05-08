#!/usr/bin/env python3

from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

# Your Telegram API credentials
api_id = 29920180
api_hash = "26c4b10bde45c44c951900706b2f77b4"
bot_token = "6329016094:AAHoNbt1VExkWp0tzPg8AwRTIEPYNC6NQ2o"

# Create a Pyrogram Client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define the /start command handler
@app.on_message(filters.command("start"))
async def start_command(client, message):
    # Create a list of commands
    commands = [
        ["💸 Lön", "🍔 Mat" ],
        ["👥 VA", "🚬 Röka"],
        ["✈️ resa", "💃 kvinna"]
    ]
    
    # Create a ReplyKeyboardMarkup with buttons for each command
    reply_markup = ReplyKeyboardMarkup(commands)

    # Reply with the keyboard
    await message.reply_text("Hej bror jag är din bot \nJag tar hand om alla dina utgifter", reply_markup=reply_markup)

# Define event handlers for each command
@app.on_message(filters.text & filters.private)
async def handle_commands(client, message):
    if message.text == "💃 kvinna":
        await message.reply_text("Hur mycket spenderade du på den kvinnan, bror?")
    elif message.text == "💸 Lön":
        await message.reply_text("Hur mycket var lönen?")
    elif message.text == "🍔 Mat":
        await message.reply_text("Hur mycket kostade maten?")
    elif message.text == "👥 VA":
        await message.reply_text("Hur mycket betalade du för VA?")
    elif message.text == "🚬 Röka":
        await message.reply_text("Hur mycket spenderade du på rök?")
    elif message.text == "✈️ resa":
        await message.reply_text("Hur mycket spenderade du på din resa?")

    else:
        await message.reply_text("Okej bror")

# Run the client
app.run()

