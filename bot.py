import os
import logging
import dotenv
import hikari
import lightbulb
import random
from lightbulb import commands

dotenv.load_dotenv()

bot = lightbulb.BotApp(
    os.environ["BOT_TOKEN"],
    prefix="+",
    banner=None,
    intents=hikari.Intents.ALL,
    default_enabled_guilds=(867887286539518002,),
    logs={
        "version": 1,
        "incremental": True,
        "loggers": {
            "hikari": {"level": "INFO"},
            "hikari.ratelimits": {"level": "TRACE_HIKARI"},
            "lightbulb": {"level": "DEBUG"},
        },
    },
)

bot.load_extensions_from("./extensions/", must_exist=True)


@bot.command
@lightbulb.command("ping", description="Veja se o Bot está vivo e a latência dele")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Pong! Latencia: {bot.heartbeat_latency*1000:.2f}ms")


@bot.listen()
async def on_ready(_: hikari.StartedEvent):
    guilds = await bot.rest.fetch_my_guilds()
    await bot.update_presence(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            type=hikari.ActivityType.PLAYING, name=f"+help in {len(guilds)} servers!"
        ),
    )


if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

    bot.run() 
    # activity=hikari.Activity(name="+help", type=hikari.ActivityType.PLAYING),
    # asyncio_debug=True,
