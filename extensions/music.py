import hikari
import lightbulb
import lavaplayer
import logging
import os
import asyncio

music_plugin = lightbulb.Plugin("music")
lavalink = lavaplayer.LavalinkClient(
    host="localhost",  # Host
    port=2333,  # Port
    password="darkbotmusic",  # Password
    user_id=51,
)


@lavalink.listen(lavaplayer.TrackStartEvent)
async def iniciar_event_music(event: lavaplayer.TrackStartEvent):
    logging.info(f"A faixa está tocando: {event.track.title}")


@lavalink.listen(lavaplayer.TrackEndEvent)
async def finalizar_event_music(event: lavaplayer.TrackEndEvent):
    logging.info(f"A faixa chegou ao fim {event.track.title}")


@lavalink.listen(lavaplayer.WebSocketClosedEvent)
async def web_socket_closed_event(event: lavaplayer.WebSocketClosedEvent):
    logging.error(f"Erro no  websocket {event.reason}")

    # Comandos

    # Comando para o bot entrar no canal de voz
@music_plugin.command()
@lightbulb.add_checks(lightbulb.guild_only)
@lightbulb.command("join", "O bot entra no canal de voz", auto_defer=True)
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def join(ctx: lightbulb.Context) -> None:
    states = music_plugin.bot.cache.get_voice_states_view_for_guild(ctx.guild_id)
    voice_state = [state async for state in states.iterator().filter(lambda i: i.user_id == ctx.author.id)]
    if not voice_state:
        await ctx.respond("you are not in a voice channel")
        return
    channel_id = voice_state[0].channel_id
    await music_plugin.bot.update_voice_state(ctx.guild_id, channel_id, self_deaf=True)
    await ctx.respond(f"done join to <#{channel_id}>")



def load(bot):
    bot.add_plugin(music_plugin)


def unload(bot):
    bot.add_plugin(music_plugin)
