import discord
from discord.ext import commands
from discord import slash_command
from discord.ext.commands import Bot


from typing import Optional,List
import json
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove.help_command
channel = bot.get_channel(969219610148745246)


@bot.event
async def on_ready():
    print("Bot con")


@bot.event
async def on_message(message):
  if message.author.bot:
    return
  await bot.process_commands(message)

@bot.command()
async def test(ctx):
  # список свойств и методов контекста можно найти в документации по запросу context
  await ctx.send('Успешный тест!')


class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Никнейм, айди", placeholder="Пример: doom#9559"))
        self.add_item(discord.ui.InputText(label="Причинау", placeholder="Пример: Нарушение правила(1.9, 1.4)", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction, ephemeral: bool=True):
        embed = discord.Embed(title="Modal Results")
        embed.set_image(url="https://pbs.twimg.com/media/DoC1GroXUAEEqIQ.jpg")
        embed.add_field(name="Никнейм, айди", value=self.children[0].value, inline=False)
        embed.add_field(name="Причина", value=self.children[1].value, inline=False)
        await interaction.response.send_message(embed=embed)

class MyView(discord.ui.View):
    @discord.ui.button(label="Подать жалобу", style=discord.ButtonStyle.danger)
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(MyModal(title="Подача жалобы"))

@bot.slash_command()
async def i(ctx):
    view=MyView()
    await ctx.respond(view=MyView())




@bot.slash_command()
async def embed(ctx):
    channel = bot.get_channel(969219610148745246)
    embed = discord.Embed(title="Embed test", description="A test for my discord bot", color=0x5bcdee)
    embed.add_field(name="Hello!", value="Hello World!", inline=False)
    await channel.send(embed=embed)


class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Никнейм, айди", placeholder="Пример: doom#9559"))
        self.add_item(discord.ui.InputText(label="Причинау", placeholder="Пример: Нарушение правила(1.9, 1.4)", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction, ephemeral: bool=True):
        channel = bot.get_channel(969219610148745246)
        embed = discord.Embed(title="Жалоба", color=0x00ac86)
        embed.add_field(name="Никнейм, айди", value=self.children[0].value, inline=False)
        embed.add_field(name="Причина", value=self.children[1].value, inline=False)
        await channel.send(embed=embed)

class MyViiw(discord.ui.View):
    @discord.ui.button(label="Подать жалобу", style=discord.ButtonStyle.danger)
    async def button_callback(self, button, interaction):
        channel = bot.get_channel(969219610148745246)
        await interaction.response.send_modal(MyModal(title="Подача жалобы"))

@bot.slash_command()
async def ddidisdfssdf(ctx):
    view=MyViiw()
    await ctx.respond(view=MyViiw())


class MeSelect(discord.ui.View):
    @discord.ui.select( 
        placeholder = "Выбери свой путь!", 
        min_values = 1, 
        max_values = 1, 
        options = [ 
            discord.SelectOption(
                label="Набор",
                value="1",
                description="Набор в стафф и ивенторы"
            ),
            discord.SelectOption(
                label="Роли",
                value="2",
                description="Да!"
            ),
            discord.SelectOption(
                label="Информация о командах",
                value="3",
                description="Нет"
            )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction): 
        select.disabled=True
        if select.values[0] == "1":
            em = discord.Embed()
            em.set_author(name="Набор")
            em.add_field(name=">>>**Термины:**", value="Стафф - модерация сервера, отвечающая за порядок в чате. Ивентор - человек отвечающий за игровую часть на сервере.", inline=False)
            await interaction.response.edit_message(embed=em)
        if select.values[0] == "2":
            await interaction.response.send_message(content="Ебала")
        if select.values[0] == "3":
            await interaction.response.send_message("Это пизда")


@bot.slash_command()
async def select(ctx):
    await ctx.send("Подробно о долбоебе", view=MeSelect())



class ct(discord.ui.View):
    @discord.ui.select( 
        placeholder = "Выбери свой путь!", 
        min_values = 1, 
        max_values = 1, 
        options = [ 
            discord.SelectOption(
                label="Набор",
                value="1",
                description="Набор в стафф и ивенторы"
            ),
            discord.SelectOption(
                label="Роли",
                value="2",
                description="Да!"
            )
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction): 
        select.disabled=True
        if select.values[0] == "1":
            em = discord.Embed()
            em.set_author(name="Набор")
            em.add_field(name="**Термины:**", value=">>>Стафф - модерация сервера, отвечающая за порядок в чате.\n Ивентор - человек отвечающий за игровую часть на сервере.", inline=False)
            em.set_image(url="https://pbs.twimg.com/media/DoC1GroXUAEEqIQ.jpg")
            await interaction.response.edit_message(embed=em)
        if select.values[0] == "2":
            await interaction.response.send_message(content="Ебала")

@bot.slash_command()
async def mena(ctx):
    view=ct()
    view.add_item(discord.ui.Button(label="🍃Подать заявку на хелпера", style=discord.ButtonStyle.link, url="https://docs.google.com/forms/d/e/1FAIpQLSeH48OSe3jxfPZrFOXZqv3e9jwq0SCfFVJYQVn6KzIKRxbuQg/viewform?fbzx=2736639172918838574"))
    view.add_item(discord.ui.Button(label="🍃Подать заявку на ивентора", style=discord.ButtonStyle.link, url="https://docs.google.com/forms/d/e/1FAIpQLSeq8ap1KVyseOLaExCe4CKjTGV7kzq9_IrfnWoqp1K4FFLlJw/viewform"))
    await ctx.send("Menus!",view=view)


class MyModl(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Никнейм, айди", placeholder="Пример: doom#9559"))
        self.add_item(discord.ui.InputText(label="Причина", placeholder="Пример: Нарушение правила(1.9, 1.4)", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction, ephemeral: bool=True):
        embed = discord.Embed(title="Жалоба")
        embed.set_image(url="https://pbs.twimg.com/media/DoC1GroXUAEEqIQ.jpg")
        embed.add_field(name="Никнейм, айди", value=self.children[0].value, inline=False)
        embed.add_field(name="Причина", value=self.children[1].value, inline=False)
        await channel.send(embed=embed)

class MyVew(discord.ui.View):
    @discord.ui.button(label="Подать жалобу", style=discord.ButtonStyle.danger)
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(MyModal(title="Подача жалобы"))

@bot.slash_command()
async def ddidлдоi(ctx):
    embet = discord.Embed(title="Нажмите на кнопку чтобы подать жалобу на участника, модерацию, ивентора", color=0x00ac86)
    embet.add_field(name="", value="полджвапо")
    embet.set_image(url="https://pbs.twimg.com/media/DoC1GroXUAEEqIQ.jpg")
    await ctx.send(embed=embet, view=MyView())





@bot.command()
@commands.has_role(998166137172938793)
async def brawl(ctx):
    embed = discord.Embed(title=None,description="канал будет доступен к началу ивента.",color=0x00ac86)
    embed.add_field(name="Информация" ,value=f"_Ивентор -_{ctx.author.mention} ")
    embed.add_field(name="Бравл старс", value="```Бравл старс - мобильная игра, в которой мы будем играть на разных персонажах и на разных картах```", inline=False)
    embed.set_author(name="Ивент: Бравл старс")        
    embed.add_field(name="За участие ", value="3000:coin:", inline=True)
    embed.add_field(name="За 3 победы ", value="25000:coin:", inline=True)
    embed.set_image(url="https://thumbs.gfycat.com/ElementaryOddFlickertailsquirrel-size_restricted.gif")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="🍃Войти на ивент", style=discord.ButtonStyle.link, url="https://discord.com/channels/892836999940177971/1036932494127280189"))
    me = await ctx.send("<@&951475093626818601>", embed=embed, view=view)
    await me.create_thread(name=None, auto_archive_duration=40)


@bot.command()
@commands.has_role(998166137172938793)
async def amongas(ctx):
    embep = discord.Embed(title=None,description="канал будет доступен к началу ивента.",color=0x00ac86)
    embep.add_field(name="Информация" ,value=f"_Ивентор -_ {ctx.author.mention} ")
    embep.add_field(name="Among As", value="```Among As - видео игра, в ней имеется несколько ролей: импостор(Убийца) и мирные```", inline=False)
    embep.set_author(name="Ивент: Among As")        
    embep.add_field(name="За участие ", value="3000:coin:", inline=True)
    embep.add_field(name="За 3 победы ", value="25000:coin:", inline=True)
    embep.set_image(url="https://acegif.com/wp-content/uploads/2020/11/am0ngsusxh-53.gif")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="🍃Войти на ивент", style=discord.ButtonStyle.link, url="https://discord.com/channels/892836999940177971/1036932494127280189"))
    mess = await ctx.send("<@&951475093626818601>", embed=embep, view=view)
    await mess.create_thread(name=None, auto_archive_duration=44)


@bot.command()
@commands.has_role(998166137172938793)
async def mafia(ctx):
    embee = discord.Embed(title=None,description="канал будет доступен к началу ивента.",color=0x00ac86)
    embee.add_field(name="Информация" ,value=f"_Ивентор -_{ctx.author.mention} ")
    embee.add_field(name="Mafia", value="```Mafia -  игра , где есть множества ролей, цель мафии победить комисаров, цель комисаров победить мафию```", inline=False)
    embee.set_author(name="Ивент: Бравл старс")        
    embee.add_field(name="За участие ", value="3000:coin:", inline=True)
    embee.add_field(name="За 3 победы ", value="25000:coin:", inline=True)
    embee.set_image(url="https://i.pinimg.com/originals/2f/ff/ee/2fffee919f8ec1c19b34fccdf647810c.gif")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="🍃Войти на ивент", style=discord.ButtonStyle.link, url="https://discord.com/channels/892836999940177971/1036932494127280189"))
    message = await ctx.send("<@&951475093626818601>", embed=embee, view=view)
    await message.create_thread(name="Обсуждаем ивент", auto_archive_duration=1440)

@bot.command()
@commands.has_role(998166137172938793)
async def gartic(ctx):
    embe = discord.Embed(title=None,description=None,color=0x00ac86)
    embe.add_field(name="**Информация**" ,value=f">>> _Ивентор -_{ctx.author.mention}\n Kанал будет доступен к началу ивента.")
    embe.add_field(name="GarticPhone", value="```GarticPhone - браузерная игра, мотивы которой рисовать по сообщению и описывать нарисованное```", inline=False)
    embe.set_author(name="Ивент: GarticPhone")        
    embe.set_image(url="https://i.gifer.com/embedded/download/Vhww.gif")
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="🍃Войти на ивент", style=discord.ButtonStyle.link, url="https://discord.com/channels/892836999940177971/1036932494127280189"))
    mes = await ctx.send("<@&951475093626818601>", embed=embe, view=view)
    await mes.create_thread(name=None, auto_archive_duration=60)


    
      

bot.run("MTAyOTIwNDg1MzE1MjU1MDkyMg.G6IT8N.42FyE95-o5Mceh-nFIVexAUwJK-hfwfwY6BwFo")
