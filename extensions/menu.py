from datetime import datetime

import hikari
import lightbulb

menu_plugin= lightbulb.Plugin("Menu")

@menu_plugin.command()
@lightbulb.command("menu",description="Uma menu para ajudar as pessoas sobre algumas coisas do Bot")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand) 
async def menu(ctx: lightbulb.Context)-> None:
    menu = hikari.Embed(
        title="**Comandos e funções**",
        description="Aqui você vai encontrar todos os comando para ajudar você a usar o bot direito",
        
    )
    menu.add_field(
        name="#roll", value="Use ele para rolar dados. Ex: 1d20", inline=False
    )
    menu.add_field(
        name="#menu", value="Use ele para acessar esse menu aqui", inline=True
    )
    menu.add_field(
        name="#sistemas",
        value="Use ele para obter links de sistemas",
        inline=True,
    )
    menu.add_field(
        name="#fichas",
        value="Use ele para obter links de fichas editaveis em PDF",
        inline=True,
    )
    menu.add_field(name="#rpg", value="Use ele para saber o que é RPG de mesa")
    #menu.set_author(
    #    name=ctx.author.display_name,
    #    url="https://is.gd/Linknadasuspeito",
    #    icon_url=ctx.author.avatar_url,
    #)
    await ctx.respond(embed=menu)

def load(bot):
    bot.add_plugin(menu_plugin)


def unload(bot):
    bot.remove_plugin(menu_plugin)
