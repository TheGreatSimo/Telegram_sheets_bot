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

def haja():
    @app.on_message(filters.text & filters.private & filters.incoming)
    async def handle_response(client, message):
        try:
            print("Received response:", message.text, )

            # Your code to handle the message goes here
        except Exception as e:
            print("Error handling message:", e)


# Define event handlers for each command
@app.on_message(filters.text & filters.private)
async def handle_commands(client, message):
    if message.text == "💃 kvinna":
        await message.reply_text("Hur mycket spenderade du på den kvinnan, bror?")
        # Set state to indicate expecting a response to this question
        haja()
    elif message.text == "💸 Lön":
        await message.reply_text("Hur mycket var lönen?")
        haja()
        user_state[message.chat.id] = "salary"
    elif message.text == "🍔 Mat":
        await message.reply_text("Hur mycket kostade maten?")
        haja()
        user_state[message.chat.id] = "food_expense"
    elif message.text == "👥 VA":
        await message.reply_text("Hur mycket betalade du för VA?")
        haja()
        user_state[message.chat.id] = "va_expense"
    elif message.text == "🚬 Röka":
        await message.reply_text("Hur mycket spenderade du på rök?")
        haja()
        user_state[message.chat.id] = "smoking_expense"
    elif message.text == "✈️ resa":
        await message.reply_text("Hur mycket spenderade du på din resa?")
        haja()
        user_state[message.chat.id] = "travel_expense"
    else:
        await message.reply_text("Okej bror")

"""
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
"""

try:
    app.run()
except Exception as e:
    print("An error occurred:", e)

