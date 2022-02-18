from __future__ import annotations
from distutils import errors

import hikari
import lightbulb
import aiohttp

nsfw_plugin = lightbulb.Plugin("nfsw")


@nsfw_plugin.command
@lightbulb.add_checks(lightbulb.nsfw_channel_only)
@lightbulb.option("tags", "A(s) que você irá procurar.")
@lightbulb.command("rule34", "Procurar por post no Rule34.")
@lightbulb.implements(lightbulb.commands.SlashCommand)
async def cmd_rule34(ctx: lightbulb.context.SlashContext) -> None:
    async with aiohttp.request(
        "GET",
        "https://api.rule34.xxx/index.php",
        params={
            "page": "dapi",
            "s": "post",
            "q": "index",
            "json": 1,
            "limit": 1,
            "tags": ctx.options.tags.replace(" ", "+"),
        },
    ) as resp:
        json = await resp.json()
        if json is None:
            await ctx.respond("Não há nenhum post com essa tag(s).")
            return
        post = json[0]
    await ctx.respond(post["sample_url"])


@nsfw_plugin.command()
@lightbulb.add_checks(lightbulb.nsfw_channel_only)
@lightbulb.option("query", "The query to search for.")
@lightbulb.command("porn", "Search a video on eporner.")
@lightbulb.implements(lightbulb.commands.SlashCommand)
async def cmd_porn(ctx: lightbulb.context.SlashContext) -> None:
    async with aiohttp.request(
        "GET",
        "https://www.eporner.com/api/v2/video/search/",
        params={"per_page": 1, "query": ctx.options.query.replace(" ", "+")},
    ) as resp:
        json = await resp.json()
        if json is None:
            await ctx.respond("No video was found with that query.")
            return
        video = json["videos"][0]
    await ctx.respond(video["url"])


def load(bot):
    bot.add_plugin(nsfw_plugin)


def unload(bot):
    bot.remove_plugin(nsfw_plugin)
