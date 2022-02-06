from lightbulb.ext import neon
import hikari
import lightbulb

rpg_plugin = lightbulb.Plugin("RPG")

# Esse comando criar os botões que irão aparecer nas mensagens
class Menu(neon.ComponentMenu):
    @neon.button("D&D", "d&d", hikari.ButtonStyle.PRIMARY, emoji="🎲")
    @neon.button("2D6", "2d6", hikari.ButtonStyle.SECONDARY, emoji="🥈")
    @neon.button("Ficha D&D", "fded", hikari.ButtonStyle.PRIMARY, emoji="📒")
    @neon.button("Ficha 2d6", "f2d6", hikari.ButtonStyle.SECONDARY, emoji="📘")
    # async def ficha2d6(self, button: neon.Button)-> None:
    @neon.button_group()
    async def links(self, button: neon.Button) -> None:
        print(f"{button.custom_id}")
        if button.custom_id == "fded":
            await self.edit_msg("https://is.gd/FichaD")
        if button.custom_id == "f2d6":
            await self.edit_msg("https://is.gd/Ficha2D6")
        if button.custom_id == "d&d":
            await self.edit_msg("https://is.gd/sistemaded")
        if button.custom_id == "2d6":
            await self.edit_msg("https://is.gd/Sistema2d6")

    @neon.on_timeout(disable_components=True)
    async def on_timeout(self) -> None:
        await self.edit_msg("\N{ALARM CLOCK} O tempo expirou!")


# Comando slash que irá fazer a interligação com a classe acima
@rpg_plugin.command()
@lightbulb.command("links_rpg", "Use para ter acesso aos links de sistemas no nosso bd")
@lightbulb.implements(lightbulb.SlashCommand)
async def ficha_cmd(ctx: lightbulb.Context) -> None:
    menu = Menu(ctx, timeout=30)
    resp = await ctx.respond("Escolha uma ficha", components=menu.build())
    await menu.run(resp)


# D&D - https://is.gd/sistemaded
# 2D6 - https://is.gd/Sistema2d6
# class Menu2(neon.ComponentMenu):
#     @neon.button("sysD&D", "sysd&d", hikari.ButtonStyle.PRIMARY, emoji="📘")
#     async def sys_cmd(self, button: neon.Button) -> None:
#         await self.edit_msg("https://is.gd/sistemaded")


# @rpg_plugin.command()
# @lightbulb.command("sys_rpg","Use para ter acesso ao links para os sitemas de rpg")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def syst_cmd(ctx: lightbulb.SlashContext) -> None:
#     menu2 = Menu(ctx, timeout=30)
#     resp2 = ctx.respond('Escolha um sistema', components=menu2.build())
#     await menu2.run(resp2)
# Carrega as extensões
def load(bot):
    bot.add_plugin(rpg_plugin)


def unload(bot):
    bot.add_plugin(rpg_plugin)
