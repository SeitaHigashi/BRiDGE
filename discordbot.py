import discord
import sys
import os
# import traceback
import threading

radnes = discord.Client()
radnes_token = os.environ['RADNES_TOKEN']

reviecer = discord.Client()
reviecer_token = os.environ['REVIECER_TOKEN']

@radnes.event
async def on_message(message):
    if message.content == '/ping':
        await message.channel.send('pong')

@reviecer.event
async def on_message(message):
    if message.content == '/ping':
        await message.channel.send('pong')
        
radnes_thread = threading.Thread(target=radnes.run, args=(radnes_token,))
reviecer_thread = threading.Thread(target=reviecer.run, args=(reviecer_token,))

radnes_thread.start()
reviecer_thread.start()

radnes_thread.join()
reviecer_thread.join()

sys.exit(0)
