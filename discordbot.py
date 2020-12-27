import discord
import sys
import os
# import traceback
# import threading

radnes = discord.Client()
radnes_token = os.environ['RADNES_TOKEN']

# reviecer = discord.Client()
# reviecer_token = os.environ['REVIECER_TOKEN']

# @radnes.event
# async def on_message(message):
    # if message.content == '/ping':
        # await message.channel.send('pong')

radnes.run(radnes_token)

sys.exit(0)
