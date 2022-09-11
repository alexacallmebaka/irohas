from nextcord import slash_command, Interaction 
from nextcord.ext import commands
from logging import Logger

#Slash commands live here.
class Admin(commands.Cog):

    def __init__(self, bot: commands.bot, log: Logger, roles: dict) -> None:
        self.bot = bot
        self.log = log
        self.roles = roles

    #Command for self-assginable roles {{{1
    @slash_command(name='grant', description='Self-assign roles.')
    async def play(self, inter: Interaction, role: str) -> None:
            
        if role in self.roles:

            try:
                
                #Grab a role object based on the role's ID.
                to_assign = inter.user.guild.get_role(self.roles[role])

                #Assign the role.
                await inter.user.add_roles(to_assign)
                
                await inter.response.send_message(f'Assigned *{role}*.', ephemeral=True)
            
            except Exception as e:
                await inter.response.send_message(f'An error has occured, please try again.', ephemeral=True)
                self.log.error(str(e))
        else:
            await inter.response.send_message(f'Role *{role}* not assignable.', ephemeral=True) #1}}}
