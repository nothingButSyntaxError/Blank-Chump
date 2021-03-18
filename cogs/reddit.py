import discord
from discord import user
from discord.ext import commands
import random
import os
const Discord = require('discord.js');
const api = require("imageapi.js");
const client = new Discord.Client();
 
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});
 
client.on('message', async msg => {
  if (msg.content === 'f.meme') {
    let subreddits = [
      "memes"
    ];
    let subreddit = subreddits[Math.floor(Math.random()*(subreddits.length))];
    let img = await api(subreddit)
    const Embed = new Discord.MessageEmbed()
    .setTitle(`A meme from r/PewdiepieSubmissions`)
    .setURL(`https://www.reddit.com/r/PewdiepieSubmissions`)
    .setColor('RANDOM')
    .setImage(img)
    msg.channel.send(Embed)
  }
});
 
client.login('your-token');