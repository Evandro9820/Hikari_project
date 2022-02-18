import asyncio
import datetime
from typing_extensions import Required
import hikari
import lightbulb


mod_plugin = lightbulb.Plugin("Mod")

# Comando de kickar um membro do servidorS
@mod_plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS))
@lightbulb.option("member", "O membro que será removido", hikari.Member)
@lightbulb.option("reason", "O motivo da remoção.", required=False)
@lightbulb.command("kick", description="Kick o membro.")
@lightbulb.implements(lightbulb.commands.SlashCommand)
async def cmd_kick(ctx: lightbulb.context.SlashContext) -> None:
    member = ctx.options.member
    reason = ctx.options.reason
    await member.kick(reason=reason)
    await ctx.respond(f"Kicked `{member.display_name}` for reason `{reason}`.")


""" @mod_plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS))
@lightbulb.option("Membro","Que você irá banir", hikari.User)
@lightbulb.option("Motivo", "O motivo do banimento", required=False)
@lightbulb.command("ban",description="Banir membro do servidor")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_ban(ctx: lightbulb.context.SlashContext) -> None:
    delete_message_days = ctx.options.delete_message_days
    if not 0 <= delete_message_days <= 7:
        await ctx.respond("delete mensagens de 0 a 7 dias.")
        return
    user = ctx.options.user
    reason = ctx.options.reason
    await ctx.get_guild().ban(
        user, delete_message_days=delete_message_days, reason=reason
    )
    await ctx.respond(
        f"Foi `{user.username}` pelo motivo `{reason}` "
        f"e foi deletado mensagens de `{delete_message_days}` dias atrás."
    )
 """
# Esse comando excluí as mensagens de até 14 dia atrás acima disso não funciona.
@mod_plugin.command()
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES)
)
@lightbulb.option(
    "qtd", "quantidade de mensagens que irá ser apagadas", type=int, required=True
)
@lightbulb.command("del_msg", "excluí as mensagens do chat")
@lightbulb.implements(lightbulb.SlashCommand)
async def del_cmd(ctx: lightbulb.Context) -> None:
    qtd_msg = ctx.options.qtd
    canal = ctx.channel_id

    msg = await ctx.bot.rest.fetch_messages(canal).limit(qtd_msg)
    await ctx.bot.rest.delete_messages(canal, msg)

    resposta = await ctx.respond(f"{len(msg)} mensagens deletadas")

    await asyncio.sleep(5)
    await resposta.delete()


def load(bot):
    bot.add_plugin(mod_plugin)


def unload(bot):
    bot.remove_plugin(mod_plugin)
