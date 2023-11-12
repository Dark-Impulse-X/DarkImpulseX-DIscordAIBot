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

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

class MyClient(discord.Client):                
    async def on_ready(self):                  #message response function
        print(f'Logged on as {self.user}!')
        
    #get api response
    def get_api_response(prompt: str) -> str | None:
        text: str| None = None   # This is new syntax of defining whether a variable is of a particular type or none. It is none initially
    
        # generating the response
        try:
            response = client.completions.create(model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:'])
            choices = response.choices[0]
            # print(choices)  #-> CompletionChoice(finish_reason='stop', index=0, logprobs=None, text=', how are you?\n')
            text = choices.text
            
        except Exception as e:
            print(e)
        
        return text
      
    #function to save msg history
    def  update_msg(self, msg, msgList):
        msgList.append(msg)
        
    #function to create the prompt to post to the api and get the proper response accordingly
    def create_prompt(self, msg, msgList):
        prompt_msg = f'\nHuman: {msg}'
        self.update_list(prompt_msg, msgList)
        prompt = ''.join(msgList)
        return prompt
    
    
    #function to get the proper bot response
    def get_bot_response(self, msg, msgList):
        prompt = self.create_prompt(msg, msgList)
        bot_response = self.get_api_response(prompt)
        
        if bot_response:
            self.update_list(bot_response, msgList)
            
            # this thing basically cuts off the AI part in the response and instead shows you the message
            # I have done this as the api have responses with Human and AI
            pos = bot_response.find('\nAI: ')
            bot_response = bot_response[pos+1:]
            
        else:
            bot_response = "Something went fu*k"
        return bot_response
      
    # function to integrate the stuffs
    def chatIntegrate(self, msg):
                # this is the initial prompt which helps the bot to understand who it is and creates responses accordingly.
        
        self.prompt_list = ['You will pretend to be a gigachad guy who is cool and knows every thing. You are the top G and you will act cool.',
                    '\nHuman: What time is it?',
                    '\nAI: Time is a very important entity in human life and you should not waste your time by asking such stupid questions. By the way it is 12:00']
        
        
        response = self.get_bot_response(msg, self.prompt_list)
        return response


    async def on_message(self, message):       
        print(f'Message from {message.author}: {message.content}')
        if self.user!= message.author:                                 #contition for response only when tagged/mentioned
          if self.user in message.mentions:
          
            channel = message.channel
            messageToSend = self.chatIntegrate(message.content)
            await channel.send(messageToSend)
            
intents = discord.Intents.default()      
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("OPENAI_API_KEY"))                    
