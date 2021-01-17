# Wiretapping-Bot

## An experimental Discord bot that allows you to pay... special attention to users in your server.

---

## Introduction:
Once upon a time, I was watching [that Snowden movie](https://en.wikipedia.org/wiki/Snowden_(film)) (solid 9/10 would recommend) and was transfixed by the way they explained the [FISA Court](https://en.wikipedia.org/wiki/United_States_Foreign_Intelligence_Surveillance_Court). Imagine you want to do surveillance on someone living inside the USA, but you obviously can't apply for a warrant because that runs the risk of tipping them off. Instead, you go the FISA Court and apply for a warrant. which is strictly classified at all steps in the process. Now you have a warrant to spy on people using [whatever methods you see fit](https://en.wikipedia.org/wiki/XKeyscore).

I wondered if I could bring PRISM\XKeyscore's functionality into Discord, where a moderation team might be able to covertly monitior all the messages of a potentially problematic user in their server, regardless of where the message was sent, when the message was sent, and if it was deleted or not. The goal was to have all these messages collected in a channel exclusive to each wiretapped user.

## How it Works:

When you choose to wiretap a user, their unique user ID (herein referred to as UUID) is added to an array in the cog. The cog then scans *every* sent message, and checks to see if it originated from a user on its wiretap list. If the UUID of a list member is recognized, the cog plucks that message, along with where it was sent, and puts it in a channel created in a special "FISA Court" category. The channel name is the UUID of the tracked user.

## How to use it:
The main deployment of this is intended to be a cog in an existing bot. This makes it *far* less conspicuous than if it was its own bot. If you really do want it to be an independent bot, then there are some steps you'll have to take.

1. Create a new Discord application at the [Discord Developer Portal](https://discord.com/developers/applications).
2. Make a bot user for the application. Name it whatever you want, give it a profile picture, go nuts. My own testing bot is literally called the National Security Agency.
3. Copy the bot token from the menu. **A bot token is what grants a program access to your bot and all of its permissions. it is imperative you keep this safe.**
4. Create a new file inside of wherever you cloned the repo to, call it `config.json`.
5. The body of this new file needs to be:
```json
{"token": "your bot token here, the one we copied from the dev portal"}
```
6. It is important you keep the quotes, so that it is correctly interpreted as a string.
7. You can now launch your bot, and verify it works correctly.
8. To invite your bot to your server, we're going to need to something else from the Developer Portal, your application's Client ID (found under General Information).
9. You can then go to [this site](https://discordapi.com/permissions.html) and insert your Client ID. You're going to need to give this bot `Administrator` permissions in order to make sure it can see every channel in the server.
10. Use the link the site generates to add the bot to any server you want, and you're ready to violate your users' right to privacy!

## Python Dependencies (packages installed with pip):
* discord (obviously)
* jthon (lets the bot interact with the config file)