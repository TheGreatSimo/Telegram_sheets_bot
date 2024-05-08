#!/usr/bin/env python3

from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

# Your Telegram API credentials
api_id = 29920180
api_hash = "26c4b10bde45c44c951900706b2f77b4"
bot_token = "6329016094:AAHoNbt1VExkWp0tzPg8AwRTIEPYNC6NQ2o"

# Create a Pyrogram Client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


# Create a dictionary to store the state for each user
user_state = {}


@app.on_message(filters.text & filters.private & filters.incoming)
async def handle_response(client, message):
    print("Received response:", message.text)
    # Check if the user is responding to one of the questions
    if message.chat.id in user_state:
        if user_state[message.chat.id] == "woman_expense":
            # Handle response to woman expense question
            woman_expense = message.text
            print("Woman Expense:", woman_expense)
            # After handling the response, remove the state for this user
            del user_state[message.chat.id]
        # Add similar conditions for other questions

# Define event handler for commands
@app.on_message(filters.text & filters.private)
async def handle_commands(client, message):
    if message.text == "💃 kvinna":
        await message.reply_text("Hur mycket spenderade du på den kvinnan, bror?")
        # Set state to indicate expecting a response to this question
        user_state[message.chat.id] = "woman_expense"
    elif message.text == "💸 Lön":
        await message.reply_text("Hur mycket var lönen?")
        user_state[message.chat.id] = "salary"
    elif message.text == "🍔 Mat":
        await message.reply_text("Hur mycket kostade maten?")
        user_state[message.chat.id] = "food_expense"
    elif message.text == "👥 VA":
        await message.reply_text("Hur mycket betalade du för VA?")
        user_state[message.chat.id] = "va_expense"
    elif message.text == "🚬 Röka":
        await message.reply_text("Hur mycket spenderade du på rök?")
        user_state[message.chat.id] = "smoking_expense"
    elif message.text == "✈️ resa":
        await message.reply_text("Hur mycket spenderade du på din resa?")
        user_state[message.chat.id] = "travel_expense"
    else:
        await message.reply_text("Okej bror")

# Run the client
app.run()
