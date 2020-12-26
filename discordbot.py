from discord.ext import commands
import os
import traceback
import threading

radnes = commands.Bot(command_prefix='/')
radnes_token = os.environ['RADNES_TOKEN']

reviecer = commands.Bot(command_prefix='/')
reviecer_token = os.environ['REVIECER_TOKEN']

@radnes.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@reviecer.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@radnes.command()
async def ping(ctx):
    await ctx.send('pong')

@reviecer.command()
async def ping(ctx):
    await ctx.send('pong')


radnes_thread = threading.Thread(target=radnes.run, args=(radnes_token,))
reviecer_thread = threading.Thread(target=reviecer.run, args=(reviecer_token,))

radnes_thread.start()
reviecer_thread.start()
radnes_thread.join()
reviecer_thread.join()