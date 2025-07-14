import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

class مهمةView(View):
    def __init__(self, الطالب, المهمة):
        super().__init__()
        self.الطالب = الطالب
        self.المهمة = المهمة
        self.المنفذ = None

    @discord.ui.button(label="📄 أخذ المهمة", style=discord.ButtonStyle.primary)
    async def اخذ(self, interaction: discord.Interaction, button: Button):
        if self.المنفذ is None:
            self.المنفذ = interaction.user.name
            await interaction.response.edit_message(embed=discord.Embed(
                title="📜 المهمة قيد التنفيذ",
                description=f"""**📝 التفاصيل:** {self.المهمة}
**📄 ينفذها:** {self.المنفذ}

**----------𝟭𝗦𝗧-----------**""",
                color=discord.Color.orange()
            ), view=self)
        else:
            await interaction.response.send_message("المهمة مأخوذة بالفعل.", ephemeral=True)

    @discord.ui.button(label="✅ تم التنفيذ", style=discord.ButtonStyle.success)
    async def تم(self, interaction: discord.Interaction, button: Button):
        if self.المنفذ == interaction.user.name:
            await interaction.response.edit_message(embed=discord.Embed(
                title="✅ المهمة مكتملة",
                description=f"""**📝 التفاصيل:** {self.المهمة}
**✅ أتمها:** {self.المنفذ}

**----------𝟭𝗦𝗧-----------**""",
                color=discord.Color.green()
            ), view=None)
        else:
            await interaction.response.send_message("أنت ما أخذت المهمة.", ephemeral=True)

@bot.command()
async def طلب(ctx, *, المهمة: str):
    view = مهمةView(ctx.author.name, المهمة)
    await ctx.send(embed=discord.Embed(
        title="📜 مهمة جديدة",
        description=f"""**👤 صاحب الطلب:** {ctx.author.name}
**📝 التفاصيل:** {المهمة}

**----------𝟭𝗦𝗧-----------**""",
        color=discord.Color.blue()
    ), view=view)

bot.run("MTM5NDMzMDk5ODAxNTAwNDY5Mg.GN5LE6.CyfV3v_yrIcLMCpBCYcZXh4lyfaZGqkmWG1-OM")
