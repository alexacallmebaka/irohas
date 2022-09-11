import nextcord
from nextcord.ext import commands
import json
import logging
from admin import Admin

def main() -> None:
    
    #Set up logging.
    log = logging.getLogger('irohas')
    
    stderr = logging.StreamHandler()
    stderr.setFormatter(logging.Formatter('%(name)s:%(asctime)s:%(levelname)s:%(message)s'))

    log.addHandler(stderr)

    #Create bot.
    bot = commands.Bot()
   
    #Add commands.
    with open('creds/roles.json') as rolefile:
        bot.add_cog(Admin(bot, log, json.load(rolefile)))
   
    #Read the bot token in from external JSON.
    with open('creds/creds.json') as credfile:
        creds = json.load(credfile)
        bot.run(creds["token"])

main()

