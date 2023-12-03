from openai import OpenAI  
import os
from dotenv import load_dotenv
import requests

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")     

class DiscordLangModel:
    openClient = OpenAI(api_key = openai_api_key)
    jokesAPI = "https://v2.jokeapi.dev/joke/Any"
    
    prompt = [
        "You are a helpful assistant and you are cool and a gigachad guy who knows everything..",
        "\nHuman: What time is it?",
        "\nAI: The time is 12:00. But you should not waste your time just asking these type stupid questions",
        "\nHuman: Hey there!",
        "\nAI: Hey there, How can I assist you for your non-important work..."
    ]
    
    def __init__(self) -> None:
        print("The part of the bot interacting with the response and questions of the users enabled...")
    
    async def getApiResponse(self):   
        apiResponse: str| None = None

        try:
            response = self.openClient.completions.create(model='text-davinci-003', #used the text-davinci-003 ai model as it is far best in GPT 3.5 model
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
            botResponse = "Something went fu*k"   # only if token validity expires or something awkward happens
        return botResponse

    async def ChatResponse(self, msg):
        question = msg[5:]
        response = await self.getBotResponse(question)
        return response
    
    #getting jokes
    async def getJokes(self):
        response = requests.get(self.jokesAPI)
        joke = response.json()
        
        if joke['type'] == 'twopart':
            return f"{joke['setup']} {joke['delivery']}"
        else:
            return joke['joke']
        
    
    # generating welcome sentence if someone enters
    async def WelcomeMessage(self, member):
        joke = await self.getJokes()
        msg = f"Welcome to the server, {member}! Feel free to ask me anything.\nJoke for you :- \n{joke}\n😂😂"
        
        return msg