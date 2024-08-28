import asyncio
import random
import requests
import discord  # Подключаем библиотеку
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True  # Необходимо для получения информации о серверах

intents = discord.Intents.default()  # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='kt!', intents=intents)
bot.remove_command('help')



@bot.event
async def on_ready():
    print(f'Бот запущен как {bot.user}')
    server_count = len(bot.guilds)
    activity = discord.Game(f' {server_count} серверах')
    await bot.change_presence(activity=activity)
    print(f'Бот {bot.user} запущен и находится на {server_count} серверах.')

# Команды бота
@bot.command()
async def sus(ctx):
    await ctx.send(':fearful:')


@bot.command()
async def help(ctx):
    help_embed = discord.Embed(
        title='ХЕЛП! Команды KlodskaTeam Bot',
        description='``kt!help`` - Показывает этот список\n``kt!sus`` - 😨\n``kt!guess <ЧИСЛО>`` - игра в угадывание числа от 1 до 10.\n``kt!trololo`` - Фановая команда, вызывает гифку с трололо\n``kt!calc <ЧИСЛО 1> <ЧИСЛО 2> <ОПЕРАЦИЯ>`` - обычный калькулятор, удобен для быстрых вычислений\n``kt!rps <ВЫБОР>`` - Игра в камень ножницы бумага с ботом.\n``kt!ball8`` - Решает вашу или чужую судьбу',
        colour=discord.Colour.from_rgb(3, 111, 252)
    )
    await ctx.send(embed=help_embed)


@bot.command()
async def guess(ctx, num: int = None):
    if num:
        number = random.randrange(1, 10)
        if num == number:
            await ctx.reply('Ты угадал!')
        else:
            await ctx.reply('Ты не угадал...')
    else:
        await ctx.send('Я загадал число от 1 до 10, угадай его, написав kt!guess <ЧИСЛО>')


@bot.command()
async def trololo(ctx):
    await ctx.send('https://tenor.com/view/trolololololololol-dance-troll-grin-gif-8138060')


@bot.command()
async def calc(ctx, num1: int = None, num2: int = None, action: int = None):
    if num1 and num2 and action:
        if action == 1:
            await ctx.reply(f'Итог: {num1 + num2}')
        elif action == 2:
            await ctx.reply(f'Итог: {num1 - num2}')
        elif action == 3:
            await ctx.reply(f'Итог: {num1 * num2}')
        elif action == 4:
            await ctx.reply(f'Итог: {num1 / num2}')
    else:
        await ctx.reply(
            'Не хватает аргументов. ``kt!calc <ЧИСЛО_1> <ЧИСЛО_2> <ДЕЙСТВИЕ>``\n**Действия:**\n- 1 - Сумма (+)\n- 2 - Вычитание (-)\n- 3 - Умножение (*)\n- 4 - Деление (/)')


@bot.command()
async def rps(ctx, select: int = None):
    if select:
        if select == random.randint(1, 3):
            await ctx.reply('Ты выиграл!')
        else:
            await ctx.reply('Ты проиграл!')
    else:
        await ctx.send(
            'Давай поиграем в камень ножницы бумага! Напиши kt!rps <ВЫБОР>\n- 1 - Камень\n- 2 - Ножницы\n- 3 - Бумага')


@bot.command()
async def ball8(ctx):
    responses = ['Да', 'Нет', 'Наверное', 'Попробуй ещё раз']
    await ctx.reply(random.choice(responses))


bot.run('YOUR-TOKEN')