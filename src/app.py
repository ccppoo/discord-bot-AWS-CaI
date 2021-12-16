from discord import Intents
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_slash.model import SlashCommandOptionType
from get_secret import get_token, get_guild_id
from typing import List

bot = commands.Bot(command_prefix='$', intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)

_token = get_token()

guild_id: List[int] = get_guild_id()


@slash.slash(
    name="갤",
    description="갤러리로 이동합니다.",
    options=[
        create_option(
            name="이름",
            description="갤러리의 이름을 입력해주세요.",
            option_type=SlashCommandOptionType.STRING,
            required=True,
            choices=[
                create_choice(
                    name='안녕',
                    value='hello'
                ),
                create_choice(
                    name='이름',
                    value='name'
                )
            ]
        )
    ],
    guild_ids=guild_id,
    connector={
        '이름': 'name'
    }
)
async def command_gall(ctx, name):
    await ctx.send(f'{name}을 선택했네요')

bot.run(_token)
