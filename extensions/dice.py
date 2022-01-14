import hikari
import lightbulb

dice_plugin = lightbulb.Plugin("Dice")

@dice_plugin.commmanda()
@lightbulb.option("bonus", "A fixed number to add to the total roll.", int, default=0)
@lightbulb.option("sides", "The number of sides each die will have.", int, default=6)
@lightbulb.option("number", "The number of dice to roll.", int)
@lightbulb.command("dice", "Roll one or more dice.")
@lightbulb.implements(commands.PrefixCommand, commands.SlashCommand)
async def dice(ctx) -> None:
    print(ctx.options.number)
    print(ctx.options.sides)
    print(ctx.options.bonus)