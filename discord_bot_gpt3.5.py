'''                                                             PROJECT DARK IMPULSE X

                                                           !!! DISCORD BOT IN YOUR SERVER !!!


This is the first version of my project working on creating a discord bot which will connect with openai api text model which will add into discord servers
and generate responses based on the data fed into chatgpt-3.5 version and it is integrated with it but it has a syntax error on line 40 of my text and I am waiting
for commits on my project to improve this and everthing is working fine till now unless the error is being thrown in line 49!!!


                                          Author and Patent @SadharanLadkaIsBack @CapedDemon @the-coder-boy

                                                                Github links are below!!

                                                        https://www.github.com/SadharanLadkaIsBack
                                                            https://www.github.com/CapedDemon
                                                           https://www.github.com/the-coder-boy

                                                           
                                                               Official Discord Server!!!
                                         Join Us!!!           https://discord.gg/78ZUPjYFN4   Join Us!!!

**[Sample Keys of Authors]**

APP ID : 1171478806305980446                                                              **(Please avoid using this for your own)**
PUBLIC KEY : 49bec5012084398faf2d75ad2dccb4a8a5b6b6f842ba8cdf60d138f112c5e830
TOKEN : MTE3MTQ3ODgwNjMwNTk4MDQ0Ng.GBorml.2-RDT9h1jzusvpAbtIAAIPa1xnEuTf0SFEv3nE
OPENAI API KEY : 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


This example requires the 'message_content' intent.'''

import discord   #discord client
import os        #to get keys
import openai    #to integrate with gpt--3.5 model: text-davinci-003

# openai.api_key = os.getenv("OPENAI_API_KEY")
token = 'MTE3MTQ3ODgwNjMwNTk4MDQ0Ng.GBorml.2-RDT9h1jzusvpAbtIAAIPa1xnEuTf0SFEv3nE'    #my-personal-token
openai.api_key = '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'                #my-personal-openai-api-key



class MyClient(discord.Client):                #created client class
    async def on_ready(self):                  #message response function
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):       
        print(f'Message from {message.author}: {message.content}')
        if self.user!= message.author:                                 #contition for response only when tagged/mentioned
          if self.user in message.mentions:
            
            response =  openai.chat.completions.create(         #error present in syntax "openai.chat.completions.create"   #error error error!!!
              model="text-davinci-003",                   #gpt-3.5 text model
              prompt=message.content,
              temperature=1,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0)
            channel = message.channel
            messageToSend = response.choices[0].text          #generating responses
            await channel.send(messageToSend)
            
intents = discord.Intents.default()       #intents
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)                     #lastly, running tokens



'''Thank you very much for viewing this cheap piece code


Please join the discord server for coding with us!! :: https://discord.gg/FEPYZ54NDt

Please keep supporting us!!

From,
SadharanLadkaIsBack
CapedDemon
the-coder-boy

'''