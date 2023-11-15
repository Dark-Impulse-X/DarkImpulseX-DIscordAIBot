'''                                                             PROJECT DARK IMPULSE X DISCORD BOT

                                                           !!! DISCORD BOT IN YOUR SERVER !!!

                                                    Author and Patent @SadharanLadkaIsBack @the-coder-boy

                                                              Github links of maintainers are below!!

                                                        https://www.github.com/SadharanLadkaIsBack
                                                           https://www.github.com/the-coder-boy

                                                           
                                                               Official Discord Server!!!
                                                             https://discord.gg/78ZUPjYFN4   
'''

import discord   
import os   
from openai import OpenAI           

TOKEN = os.getenv("TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openClient = OpenAI(api_key = OPENAI_API_KEY)

class MyClient(discord.Client):      
    prompt = [
        "You are a helpful assistant and you are cool and a gigachad guy who knows everything..",
        "\nHuman: What time is it?",
        "\nAI: The time is 12:00. But you should not waste your time just asking these type stupid questions you ass",
    ]
          
    async def on_ready(self):                  
        print(f'Logged on as {self.user}!')
        
    async def getApiResponse(self):
        apiResponse: str| None = None   
    
        try:
            response = openClient.completions.create(model='text-davinci-003', #used the text-davinci-003 ai model
            prompt=self.prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:'])
            
            # taking the response text from the last
            apiResponse = response.choices[-1].text
            
        except Exception as e:
            print(e)
        
        return apiResponse
      
    
    async def updateMsg(self, msg):
        self.prompt.append(msg)
        
    async def createPrompt(self, question):
        prompt_msg = f'\nHuman: {question}'  # the prompt message should be according to the prompt list
        await self.updateMsg(prompt_msg)
    
    async def getBotResponse(self, question):
        await self.createPrompt(question)
        botResponse = await self.getApiResponse()
        
        if botResponse:
            await self.updateMsg(botResponse)
            
            # this thing basically cuts off the before: in the response and instead shows you the message
            pos = botResponse.find(':')
            botResponse = botResponse[pos+1:]
            
        else:
            botResponse = "Something went fu*k"
        return botResponse
    
    async def chatResponse(self, msg):
        question = msg[5:]
        response = await self.getBotResponse(question)
        return response

    async def on_message(self, message):       
        print(f'Message from {message.author}: {message.content}')
        
        # the command should start with /dix
        if message.content.startswith('/dix '):
            response = await self.chatResponse(message.content)
            channel = message.channel
            await channel.send(response)
            
# intents are created 
# this syntax is for the working of the bot in discord            
intents = discord.Intents.default()      
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)                    
