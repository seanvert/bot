from twitchio.ext import commands
import os
from dotenv import load_dotenv

class Bot(commands.Bot):

    def __init__(self):
        CLIENT_ID = os.environ.get('TWITCH_CLIENT_ID_SECRET')
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=CLIENT_ID, prefix='!', initial_channels=['putStrLn'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    

    @commands.command(name='github')
    async def github(self, ctx):
        projeto = 'botpython'
        # TODO: trocar isso daqui pra o que eu estiver fazendo na live
        await ctx.send(f'https://github.com/seanvert/{projeto}')

    @commands.command(name='game')
    async def game(self, ctx: commands.Context):
        await ctx.channel.whisper('ijijijij')
    # async def event_message(self, message):
    #    print(message.author.name, message.content)

load_dotenv()
bot = Bot()
bot.run()