import discord

from python_aternos import Client

bot_id = 1033058024450965546

user = "ProsteMC_1"
pswd = "?ProsteMC?"


try:
    aternos = Client.restore_session(user,pswd)
except:
    aternos = Client.from_credentials(user, pswd)


servers = aternos.list_servers()
print(servers)

server = servers[0]
server.start()





intents = discord.Intents()
intents.members = True
intents.presences = True
intents.messages = True

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is running')


@client.event
async def on_message(message):

    if message.author == client.user:
        return
  
    msg = str(message.content).replace(str(f'<@{bot_id}> '), '')

    #print(message.content, msg, client.user, sep=' , ')

    await message.channel.send('Received message: ' + msg)


client.run('MTAzMzA1ODAyNDQ1MDk2NTU0Ng.GmlTDQ.-5io7BNBx3OtTYd8cdBaRXgq31zSA_mD65WJqs')