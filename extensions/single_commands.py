import hikari, lightbulb
from dotenv import load_dotenv
from os import getenv
from variables import *
from secrets import randbelow

load_dotenv()

def rand(min: int, max: int) -> int:
    return min + randbelow((max - min) + 1)

plugin = lightbulb.Plugin("single_commands")

# About command
@plugin.command
@lightbulb.command('apropos', 'À propos de Swagbot')
@lightbulb.implements(lightbulb.SlashCommand)
async def apropos(ctx) -> None:
    embed = (
        hikari.Embed(title=f"Swagbot (v{botversion})", description="Le bot le plus **swag** de la Terre !", color=embedcolor)
        .add_field("Mais qui es-tu ?", "Je suis un bot multifonction conçu par DarkblooM#8472 pour la communauté de MamanSwag.")
        .add_field("Qu'est-ce que tu peux faire ?", "Je possède une variété de commandes utilitaires, ainsi qu'une fonction pour acceuillir les nouveaux membres du serveur.\nJ'ai également été consulter mon confrère WizeBot pour me procurer les commandes personnalisées disponibles sur Twitch. Si vous avez une commande de ce genre qui contient du texte, vous pouvez la lancer avec le préfix habituel `!`.")
        .add_field("Où puis-je trouver tes commandes ?", "Simplement en entrant un `/` dans la barre de chat, un menu contextuel s'ouvre contenant toutes les commandes disponibles sur ce serveur. Vous pouvez trouver les miennes en cliquant sur mon icône dans la liste verticale à gauche.")
        .set_footer("Pour toute question non-répondue ou toute demande à propos de Swagbot, merci de contacter DarkblooM#8472.")
    )
    await ctx.respond(embed)
    return

# Patch note command
@plugin.command
@lightbulb.command('patchnote', 'Informations sur le dernier patch')
@lightbulb.implements(lightbulb.SlashCommand)
async def patchnote(ctx) -> None:
    embed = hikari.Embed(title="Patch note", color=embedcolor)
    embed.add_field("Version", botversion)
    if "beta" in botversion:
        embed.add_field("Disclaimer", "Je suis encore en beta ! Il se peut que je ne fonctionne pas toujours corrèctement, alors soyez patients avec moi.")
    embed.add_field("Contenu", patchnote)
    await ctx.respond(embed)
    return

# Social command
@plugin.command
@lightbulb.command('social', 'Les liens utiles')
@lightbulb.implements(lightbulb.SlashCommand)
async def social(ctx) -> None:
    await ctx.respond("""Suis MamanSwag partout !
**__Twitch__ :** <https://twitch.tv/mamanswag>
**__YouTube__ :** <https://youtube.com/c/MamanSwag>
**__Twitter__ :** <https://twitter.com/SwagMaman>
**__TikTokk__ :** <https://www.tiktok.com/@mamanswag>

Visite aussi le site web !
<https://mamanswag.tv/>""")
    return

# Dixper command
@plugin.command
@lightbulb.command("dixper", "Inscris-toi sur Dixper !")
@lightbulb.implements(lightbulb.SlashCommand)
async def dixper(ctx) -> None:
    await ctx.respond("""INSCRIS-TOI maintenant sur <https://dixper.gg/MamanSwag>
Pourquoi ? Car tu vas donner un tout autre sens à mes lives !! :wink:""")
    return

# Epic code command
@plugin.command
@lightbulb.command("epic", "Code créateur Epic Games")
@lightbulb.implements(lightbulb.SlashCommand)
async def epic(ctx) -> None:
    await ctx.respond("""CODE CRÉATEUR : mamanswag
Merci pour ton soutien :heartpulse: :hugging:""")
    return

# Stream schedule command
@plugin.command
@lightbulb.command("prog", "Ne manque plus aucun live !")
@lightbulb.implements(lightbulb.SlashCommand)
async def prog(ctx) -> None:
    await ctx.respond(":arrow_forward: Maman streame tous les soirs de 22h à 00h | :pause_button: le mardi | Restez à l'affut pour des streams sauvages certains aprems :upside_down:")
    return

# Feedback command
@plugin.command
@lightbulb.command("feedback", "Ton avis m'intéresse !")
@lightbulb.implements(lightbulb.SlashCommand)
async def feedback(ctx) -> None:
    embed = (
        hikari.Embed(title="Ton avis m'intéresse !", description="Une question ? Une proposition ? Ou tout simplement un avis à donner ? Ça se passe sur Github :\nhttps://github.com/DarkblooM-SR/swagbot/issues", color=embedcolor)
        .add_field(name="Pour les développeurs", value="Une idée de commande ou de fonctionnalité ? Tu peux créer un plugin Lightbulb et faire une demande de pull, je reviendrai vers toi si je suis intéressé :\n**__Pull requests__ :** https://github.com/DarkblooM-SR/swagbot/pulls\n**__Documentation Lightbulb__ :** https://hikari-lightbulb.readthedocs.io/en/latest/")
    )
    await ctx.respond(embed)
    return

# Random password command
@plugin.command
@lightbulb.command("mdp", "Génère un mot de passe aléatoire")
@lightbulb.implements(lightbulb.SlashCommand)
async def mdp(ctx) -> None:
    output = ""
    for n in range(16):
        i = rand(33, 126)
        if i != 96:
            output = output+chr(i)
    await ctx.author.send(f"```\n{output}\n```")
    await ctx.respond("Check tes messages privés !")
    return

def load(bot) -> None:
    bot.add_plugin(plugin)

def unload(bot) -> None:
    bot.remove_plugin(plugin)
