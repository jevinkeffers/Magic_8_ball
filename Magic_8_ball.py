import random

eightball_choices = {
"1": "Ask again later.",
"2": "As I see it, yes.",
"3": "Better not tell you now.",
"4": "Cannot predict now",
"5": "Concentrate and ask again.",
"6": "Don’t count on it.",
"7": "It is certain.",
"8": "It is decidedly so.",
"9": "Most likely.",
"10": "My reply is no.",
"11": "My sources say no.",
"12": "Outlook not so good.",
"13": "Outlook good.",
"14": "Reply hazy, try again.",
"15": "Signs point to yes.",
"16": "Very doubtful.",
"17": "Without a doubt.",
"18": "Yes.",
"19": "Yes, definitely.",
"20": "You may rely on it.",
"Play_again": "Y"
}

def magic_eightball():
    random_selection = eightball_choices[str(random.randint(1,20))]
    user = input("Shake that 8 Ball (Hit ENTER/RETURN) ")
    print(random_selection)

while eightball_choices["Play_again"] == "Y":
    magic_eightball()
    eightball_choices["Play_again"] = input("Try again? (Y/N) ").upper()