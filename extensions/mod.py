import datetime
import hikari
import lightbulb


mod_plugin = lightbulb.Plugin("Mod")


@mod_plugin.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS))
@lightbulb.option("member", "O membro que será removido", hikari.Member)
@lightbulb.option("reason", "O motivo da remoção.", required=False)
@lightbulb.command("kick", "Kick o membro.")
@lightbulb.implements(lightbulb.commands.SlashCommand)
async def cmd_kick(ctx: lightbulb.context.SlashContext) -> None:
    member = ctx.options.member
    reason = ctx.options.reason
    await member.kick(reason=reason)
    await ctx.respond(f"Kicked `{member.display_name}` for reason `{reason}`.")




def load(bot):
    bot.add_plugin(mod_plugin)


def unload(bot):
    bot.remove_plugin(mod_plugin)
