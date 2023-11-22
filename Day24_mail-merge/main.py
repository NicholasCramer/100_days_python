import os

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

names = []

with open("Input/Names/invited_names.txt") as list_names:
    invited_names = list_names.readlines()
    for name in invited_names:
        names.append(name.strip())

with open("Input/Letters/starting_letter.txt") as starting_letter:
    contents = starting_letter.read()


def create_letter_contents(person):
    new_contents = contents.replace("[name]", person)
    return new_contents


def compose_letter(person):
    content = str(create_letter_contents(person))
    filepath = os.path.join("Output/ReadyToSend", f"letter_for_{person}.txt")
    with open(filepath, "w") as final_letter:
        final_letter.write(content)


for name in range(len(names)):
    recipient = names[name]
    compose_letter(recipient)
