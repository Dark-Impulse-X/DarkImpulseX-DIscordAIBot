<div align="center">

<h1>● DarkImpulseX-DiscordAIBot</h1>
</br>
  
<p align="center">
  <img src="https://readme-typing-svg.demolab.com/?lines=The,+Ultimate!;+Discord Companion&font=Fira%20Code&center=true&width=380&height=50&duration=4000&pause=1000" alt="Example Usage - README Typing SVG">
</p>
  
  <img alt="Discord" src="https://img.shields.io/discord/1171866074338299974?style=for-the-badge">
  
  <img alt="GitHub contributors" src="https://img.shields.io/github/contributors-anon/Dark-Impulse-X/DarkImpulseX-DIscordAIBot?style=for-the-badge">
  
  <a href="https://github.com/Dark-Impulse-X/DarkImpulseX-DiscordAIBot"><img src="https://img.shields.io/badge/Language-python-green.svg?style=for-the-badge" alt="Language"></a>
  <a href="https://www.codefactor.io/repository/github/dark-impulse-x/darkimpulsex-discordaibot/overview/master"><img src="https://www.codefactor.io/repository/github/dark-impulse-x/darkimpulsex-discordaibot/badge/master?style=for-the-badge" alt="CodeFactor" /></a>
  
</div>
</br>
<div align="center">

<img src="https://github.com/Dark-Impulse-X/DarkImpulseX-DIscordAIBot/assets/145888668/ea46a340-2b23-4aef-8537-b4b6b6aaea8f" width="230" height="230">

</div>

</br></br>

<h2 align="center"> Maintainers </h2>
<div align="center">
  <a href="https://github.com/the-coder-boy">the-coder-boy</a>          
  
  <a href="https://github.com/SadharanLadkaIsBack">SadharanLadkaIsBack</a>
  </div>

</br>

<h2>About </h2>
<div align="center">
  DarkImpulseX-DiscordAIBot is the all in one discord bot that you need. This is an AI Bot which integrates with openai as well as trains itself with new datasets.
  Manage your discord with this ultimate discord companion which can handle different things from playing music, chatting with people, making ready made templates and many more.
</br> We are continuously developing to fit with the modern and developing world!
</div>

</br></br>

## Documentation
DarkImpulseX-DiscordAIBot is a versatile discord bot. 
It is end-to-end trained to work in your server. It uses our language model as well as openai. Also it can use NLP to understand the language with which users are interacting.

- **Features**
  - [x] Responds to users query using openai 😎
  - [x] Greets if anyone joins your discord channel with a *joke* 😂
  - [x] Joins and leaves voice channel 📣
  - [ ] Play, stop, resume, previous and next music playing
  - [ ] Image generation
  - [ ] List commands
  - [ ] Discord Management
  - [ ] and more.......

### Libraries Used 
- openai
- discord.py
- discord.py[voice] *pip install discord.py[voice]*
- requests

### Code Explanation
- **Prompt Engineering**
 is very essential part to make a good AI chat application

While using the OpenAI API, we have used a very cool prompt so to give our bot a particular behaviour. See the code example below where we have told hpw the bot would behave and how it should give answers- 

![Snippet](https://github.com/Dark-Impulse-X/DarkImpulseX-DIscordAIBot/assets/133076612/0cd59bc0-a886-4f01-a7de-7d61fc6e824e)


- **Greeting User**
The bot checks the default text channel using the below code
```
guild.text_channels[0]
```
*a "member" represents a user within the context of a specific server (guild)*
*A "guild" is Discord's term for a server. It represents a collection of channels, roles, and members on Discord.*

The bot greets the user by making requests to [jokeapi](https://v2.jokeapi.dev/) - we appreciate it a lot.

- **Joins and leaves voice channel** 
*uses python discord.py[voice]*
  - command to join - *join*
  We get the voice channel that user has joined with this code :- 
  ```
  channel = message.author.voice.channel
  ```
  and stores the channel in `self.voiceChannel`.

  - command to leave - *leave*
  Leaves the channel on user command by using the same code above to get the channel

  - leaves automatically
  checks the number of users using the code
  ```
  len(self.voiceChannel.channel.members) == 1
  ```
  then, disconnects after waiting for *1 minute*



We have developed our bot such that it takes into consideration those chats which **mentions** the bot while chatting.


### Installation
All you need is python installed in your computer.

- [Add](https://tinyurl.com/darkimpulsex) the bot to your server


- Clone the repo
  
``` shell
git clone https://github.com/Dark-Impulse-X/DarkImpulseX-DIscordAIBot.git
```

- Install the libraries
```
pip install requirements.txt
```

- Extra installation
```
pip install discord.py[voice]
```

### How To Run?

- Collect all the tokens and openai keys.

- Make a .env file and make two variables TOKEN and OPENAI_API_KEY and store the value in it.
  
- Run the **main.py** file from the src to run locally.
  ```
  python src/main.py
  ```

- Invite the bot [here](https://tinyurl.com/darkimpulsex)

- Enjoy your bot!


**THE BOT WILL BE ONLINE UNTILL YOU CLOSE main.py ON YOUR PC!!!**

**How to make use of the bot?**

- Mention the bot whilist your message to get responses


## Contributions
Contributions are accepted. Read the contribution guidelines before contributing and follow the rules properly.

## License
DarkImpulseX-DiscordAIBot is licensed under the MIT License. You are permitted to use, copy, modify, distribute, sublicense, and sell copies of the software.
