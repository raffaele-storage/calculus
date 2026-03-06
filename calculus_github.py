import discord
from discord.ext import commands

BOT_TOKEN = "YOUR BOT TOKEN HERE" # Replace with your bot's token, you can get this from the Discord Developer Portal

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

#bot events

@bot.event
async def on_ready():
    print(f"calculus active") #you can see this only in the console, not in the discord server

#bot commands

@bot.command()
async def calculations(ctx):
    commands_list = """
    Here are the available commands:
    !add <a> <b> - Adds two numbers
    !subtract <a> <b> - Subtracts the second number from the first
    !multiply <a> <b> - Multiplies two numbers
    !divide <a> <b> - Divides the first number by the second
    !power <a> <b> - Raises the first number to the power of the second
    !sqrt <a> - Calculates the square root of a number
    !factorial <n> - Calculates the factorial of a non-negative integer
    """
    await ctx.send(commands_list)

@bot.command()
async def add(ctx, a: float, b: float):
    result = a + b
    await ctx.send(f"The sum of {a} and {b} is {result}")

@bot.command()
async def subtract(ctx, a: float, b: float):
    result = a - b
    await ctx.send(f"The difference of {a} and {b} is {result}")

@bot.command()
async def multiply(ctx, a: float, b: float): 
    result = a * b
    await ctx.send(f"The product of {a} and {b} is {result}")

@bot.command()
async def divide(ctx, a: float, b: float):
    if b == 0:
        await ctx.send("Error: Division by zero is undefined.")
    else:
        result = a / b
        await ctx.send(f"The quotient of {a} and {b} is {result}")

@bot.command()
async def power(ctx, a: float, b: float):
    result = a ** b
    await ctx.send(f"{a} raised to the power of {b} is {result}")

@bot.command()
async def sqrt(ctx, a: float):
    if a < 0:
        await ctx.send("Error: Square root of a negative number is undefined.")
    else:
        result = a ** 0.5
        await ctx.send(f"The square root of {a} is {result}")

@bot.command()
async def factorial(ctx, n: int):
    if n < 0:
        await ctx.send("Error: Factorial of a negative number is undefined.")
    elif n == 0 or n == 1:
        await ctx.send(f"The factorial of {n} is 1")
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        await ctx.send(f"The factorial of {n} is {result}")

# Run the bot

bot.run(BOT_TOKEN)