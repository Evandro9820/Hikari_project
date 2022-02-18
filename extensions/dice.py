import hikari
import lightbulb
import random

dice_plugin = lightbulb.Plugin("Dice")


@dice_plugin.command()
@lightbulb.option("number", "The number of dice to roll.", int)
@lightbulb.option("bonus", "A fixed number to add to the total roll.", int, default=0)
@lightbulb.option("sides", "The number of sides each die will have.", int, default=6)
@lightbulb.command("dice", "Roll one or more dice.")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def dice(ctx: lightbulb.Context) -> None:
    print(ctx.options.number)
    print(ctx.options.sides)
    print(ctx.options.bonus)

    number = ctx.options.number
    sides = ctx.options.sides
    bonus = ctx.options.bonus

    # Option validation
    if number > 25:
        await ctx.respond("No more than 25 dice can be rolled at once.")
        return

    if sides > 100:
        await ctx.respond("The dice cannot have more than 100 sides.")
        return

    rolls = [random.randint(1, sides) for _ in range(number)]

    # To send a message, use ctx.respond. Using kwargs, you can make the
    # bot reply to a message (when not sent from a slash command
    # invocation), allow mentions, make the message ephemeral, etc.
    await ctx.respond(
        " + ".join(f"{r}" for r in rolls)
        + (f" + {bonus} (bonus)" if bonus else "")
        + f" = **{sum(rolls) + bonus:,}**"
    )


def load(bot):
    bot.add_plugin(dice_plugin)


def unload(bot):
    bot.remove_plugin(dice_plugin)
