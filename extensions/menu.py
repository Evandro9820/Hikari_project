import asyncio

import hikari
import lightbulb

menu_plugin= lightbulb.Plugin("Menu")

@menu_plugin.command()
@lightbulb.command("menu",description="Um menu para ajudar as pessoas sobre algumas coisas do Bot")
@lightbulb.implements(lightbulb.PrefixCommandGroup, lightbulb.SlashCommand) 
async def menu(ctx: lightbulb.Context)-> None:
    menu = hikari.Embed(
        title="**Comandos e funções**",
        description="Aqui você vai encontrar todos os comando para ajudar você a usar o bot direito",
        
    )
    menu.add_field(
        name=f"+roll", value="Use ele para rolar dados. Ex: 1d20", inline=False
    )
    menu.add_field(
        name="+menu", value="Use ele para acessar esse menu aqui", inline=True
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

MENUDROP ={
    "SISTEMA": "📒",
    "DICE":"🎲"
}
@menu.child
@lightbulb.command("drop", description="Um menu em dropdown")
@lightbulb.implements(lightbulb.PrefixSubGroup)
async def drop(ctx: lightbulb.Context) -> None:
    select_menu =(
        ctx.bot.rest.build_action_row()
        .add_select_menu("menu_dropdown")
        .set_placeholder("Selecione para")
    )

    for name, emoji in MENUDROP.items():
        select_menu.add_option(
            name,
            name.lower().replace(" ","_"),

        ).set_emoji(emoji).add_to_menu()
    resp = await ctx.respond(
        "Selecione um elemento no menu",
        component=select_menu.add_to_container(),
    )
    msg = await resp.message()
    
    try:
        evento = await ctx.bot.wait_for(
            hikari.InteractionCreateEvent,
            timeout=60,
            predicate=lambda e:
                isinstance(e.interaction, hikari.ComponentInteraction)
                and e.interaction.user.id == ctx.author.id
                and e.interaction.message.id == msg.id
                and e.interaction.component_type == hikari.ComponentType.SELECT_MENU
        )
    except asyncio.TimeoutError:
        await msg.edit("O tempo expirou", component=[])    

def load(bot):
    bot.add_plugin(menu_plugin)


def unload(bot):
    bot.remove_plugin(menu_plugin)
