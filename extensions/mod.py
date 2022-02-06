import asyncio
import datetime
from typing_extensions import Required
import hikari
import lightbulb


mod_plugin = lightbulb.Plugin("Mod")


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

@mod_plugin.command
@lightbulb.option(
    "messages", "The number of messages to purge.", type=int, required=True
)
@lightbulb.command("purge", "Purge messages.", aliases=["clear"])
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def purge_messages(ctx: lightbulb.Context) -> None:
    num_msgs = ctx.options.messages
    channel = ctx.channel_id

    # If the command was invoked using the PrefixCommand, it will create a message
    # before we purge the messages, so you want to delete this message first
    if isinstance(ctx, lightbulb.PrefixContext):
        await ctx.event.message.delete()

    msgs = await ctx.bot.rest.fetch_messages(channel).limit(num_msgs)
    await ctx.bot.rest.delete_messages(channel, msgs)

    resp = await ctx.respond(f"{len(msgs)} messages deleted")

    await asyncio.sleep(5)
    await resp.delete()
def load(bot):
    bot.add_plugin(mod_plugin)


def unload(bot):
    bot.remove_plugin(mod_plugin)
