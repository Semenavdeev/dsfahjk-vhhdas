elif message.content.startwith('$genpas'):
        await message.channel.send(gen_pass())