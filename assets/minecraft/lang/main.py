import os

text_to_add = """
{
    "multiplayer.player.joined": "%s§a has joined the game!",
    "multiplayer.player.joined.renamed": "%s §7(formerly %s§7) §2has joined the game!",
    "multiplayer.player.left": "%s §chas left the game..."
}
"""

current_directory = os.getcwd()

for filename in os.listdir(current_directory):
    if filename.endswith('.json'):
        file_path = os.path.join(current_directory, filename)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_to_add)