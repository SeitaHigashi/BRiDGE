from discord.ext import commands
import os
import traceback

Radnes = commands.Bot(command_prefix='/')
Radnes_token = os.environ['RADNES_TOKEN']

Reviecer = commands.Bot(command_prefix='/')
Reviecer_token = os.environ['REVIECER_TOKEN']

@Radnes.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@Reviecer.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@Radnes.command()
async def ping(ctx):
    await ctx.send('pong')

@Reviecer.command()
async def ping(ctx):
    await ctx.send('pong')


#Radnes.run(Radnes_token)
Reviecer.run(Reviecer_token)
