'''                                                        PROJECT DARK IMPULSE X DISCORD BOT

                                                           !!! DISCORD BOT IN YOUR SERVER !!!

                                                    Author and Patent @SadharanLadkaIsBack @the-coder-boy

                                                         Github links of maintainers are below!!

                                                        https://www.github.com/SadharanLadkaIsBack
                                                           https://www.github.com/the-coder-boy

                                                           
                                                               ! Official Discord Server !
                                                              https://discord.gg/78ZUPjYFN4   
'''

import discord 
import os  
from openai import OpenAI  
import sys     
from dotenv import load_dotenv
from discordLang import DiscordLangModel
import asyncio

load_dotenv()

token = os.getenv("TOKEN")    
openai_api_key = os.getenv("OPENAI_API_KEY")     

openClient = OpenAI(api_key = openai_api_key) # gaining access to openai

class MyClient(discord.Client):  
    dixLang = DiscordLangModel() 
     
    voiceChannel = None
    commands = ['join']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):                 
        print(f'Logged on as {self.user}!')   #console logging on connection with discord api

    async def on_message(self, message):       
        print(f'Message from {message.author}: {message.content}')

        # just you need to mention the bot in the query message and thats it!
        if self.user!= message.author:
          if self.user in message.mentions:
            
            # checking if user asks bot to join a voice channel or not
            if "join" in message.content.lower():
                
                # checks whether user is in the voice channel or not
                if message.author.voice and message.author.voice.channel:
                        channel = message.author.voice.channel
                        voiceChannel = await channel.connect()
                        self.voiceChannel = voiceChannel
                        
                        await message.channel.send(f"Connected to voice channel: {channel} 📣")
                        
                        return
                    
                else:
                    await message.channel.send("You need to be in a voice channel to use this command.")
                    return
            
            # leaving the voice channel on user command
            elif "leave" in message.content.lower():
                channel = message.author.voice.channel
                
                if self.voiceChannel:
                    await message.channel.send(f'Left voice channel: {channel}')
                    await self.voiceChannel.disconnect()
                    
                    self.voiceChannel = None  # Reset the current voice channel
                    return
                else:
                    await message.channel.send("I am not currently in a voice channel.")
                    return
            
            response = await self.dixLang.ChatResponse(msg =message.content)
            channel = message.channel
            await channel.send(response)

    # if no one in the voice channel, the bot will leave after 1 minute
    async def on_voice_state_update(self, member, before, after):
        print(self.voiceChannel)
        if self.voiceChannel and len(self.voiceChannel.channel.members) == 1:
            # sleep for 1 min
            await asyncio.sleep(60)
            
            if len(self.voiceChannel.channel.members) == 1:
                if self.voiceChannel.guild:
                    await self.voiceChannel.disconnect()
                    print(f'Left voice channel: {self.voiceChannel.channel} as no one here 😴')
                    self.voiceChannel = None

    async def on_member_join(self, member):
        guild = member.guild

        # Find the default text channel for the server
        channel = guild.text_channels[0]
    
        welcomeMessage = await self.dixLang.WelcomeMessage(member.mention)

        await channel.send(welcomeMessage)
             

           
intents = discord.Intents.default()      
intents.message_content = True
intents.members = True
intents.voice_states = True

client = MyClient(intents=intents)
client.run(token)

#adding logs
# sys.stdout = open('logs/bot.log', 'w')
# sys.stdout.close() #added logging support in folder directory logs/bot.log for tracking