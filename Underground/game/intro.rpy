# The script of the game goes in this file.
# Player stats

default player_hp = 40
default player_max_hp = 100 

# Opponent stats 
default opponent_hp = 60 
default opponent_max_hp = 100


# Player's companion 

default player_creature = ""
default friendship = 5

# Character

define m = Character("Me", color="#e9e641")
define c = Character("[player_creature]", color="#564b93")

# Battle Screen

screen battle_screen():
    modal True 
    tag battle_screen

    # Display opponent
    add "opponent.png" xalign 0.85 yalign 0.1

    # Display creature
    if player_creature == "Captain Cringe": 
        add "CaptainCringe.png" xalign 0.1 yalign 0.6
    elif player_creature == "Caffine Crusader":
            add "CaffineCrusader.png" xalign 0.1 yalign 0.6
    elif player_creature == "Raving Ravenge":
        add "RavingRavenge.png" xalign 0.1 yalign 0.6

    # Display hit bars 
    #opponent
    frame: 
        xalign 0.95
        yalign 0.05
        background "#0009"
        padding (10, 10, 10, 10)
        vbox: 
            text "The Shadow" color "#fff" size 20
            bar value opponent_hp range opponent_max_hp
            xalign 0.0 yalign 0.1 xmaximum 200
    #player
    frame:
        xalign 0.05
        yalign 0.75
        background "#0009"
        padding (10, 10, 10, 10)
        vbox: 
            text "[player_creature]" color "#fff" size 20
            bar value player_hp range player_max_hp 
            xalign 0.0 yalign 0.1 xmaximum 200

    # Display battle menu
    frame: 
        xalign 0.5
        yalign 0.55
        background "#0009"
        padding (10, 10, 10, 10)
        hbox spacing 20: 
            textbutton "Fight" action Return("fight") text_color "#ff0000"
            textbutton "Fly" action Return("fly") text_color "#c97ee9"
            textbutton "Talk" action Return("talk") text_color "#00fff2"
            textbutton "Run" action Return("run") text_color "#eeff00" 

#Character Selection

screen creature_selection():
    modal True
    tag selection 
    frame:
        xalign 0.5
        yalign 0.5
        background "#0009"
        vbox:
            spacing 30
            text "Chose your sidekick:" color "#d6b476" size 30
            textbutton "CaptianCringe" action [SetVariable
            ("player_creature", "CaptianCringe"), Jump("battle_intro")] text_color "#7e3636" text_size 35
            textbutton "CaffeneCrusader" action [SetVariable
            ("player_creature", "CaffeneCrusader"), Jump("battle_intro")] text_color "#32774a" text_size 35
            textbutton "RavingRavenge" action [SetVariable
            ("player_creature", "RavingRevenge"), Jump("battle_intro")] text_color "#ce6fdf" text_size 35

# The game starts here.

label start:
    scene intro with dissolve
    
    "Welcome to 2054"
    "Four years ago, people with superpowers were discovered."
    "And they don't have your typical invisability or telepathy super powers."
    "They have unique super powers to make their lives, and the lives of others around them, better...or worse."
    "Lately, there have been warnings of a shadow haunting your city."
    "You haven't run into it yet, luckily."
    call screen creature_selection

label battle_intro: 
    scene alleyway with fade
    "While walking down the streets of New York City, you see a shadow in the alleyway."
    "Luckily you have your superhero sidekcik [player_creature] by your side."
    "You run down the alleyway hoping to run into the shadow and take it down. You want to be the hero that saves your city."
    jump battle_sequence

label battle_sequence:
    "The shadow is there and it spins around and faces you."
    show screen battle_screen
    $ result= ui.interact()

    if result == "fight":
        hide screen battle_screen
        "You launch an attack with [player_creature]!"
        "The shadow fights back."
        $ opponent_hp -= 10
        if opponent_hp <= 0:
            "The shadow is no match for your powers. The shadow is defeated."
            jump victory
        else: 
            "The shadow takes a hit, but is still standing."
            jump battle_sequence
    elif result == "talk":
        hide screen battle_screen
        "The shadow plays along and chats with you."
        "The shadow starts to laugh."
        $ player_hp += 10
        if player_hp >= player_max_hp:
            "You, and [player_creature] become friends with the shadow. You decide to join forces to protect the city."
            jump friendship
        else: 
            "The shadow talks but soon you all remember why you are there."
            jump battle_sequence  
    elif result == "Fly":
        hide screen battle_screen
        "You decide to attack from the sky."
        "You and your [player_creature] zoom up above and attack."
        $ player_hp += 20
        if player_hp >= player_max_hp:
            "You are victorious and the shadow is defeated."
            jump victory
        else: 
            "The shadow hits back and you fall to the ground."
            jump battle_sequence    
    elif result == "Run":
        hide screen battle_screen
        "You try to escape, but the shadow blocks your path."
        jump battle_sequence  

label victory: 
    "Victory is yours! The shadow was overcome but [player_creature]'s epic powers."
    "Thanks to [player_creature] New York City is safe...for now..."
    $ friendship -= 1
    jump companion_backstory 

label friendship: 
    "Who knew this would result in a friendship"
    "You continue to keep the city safe with [player_creature] and the shadow, each going in your different directions."
    $ friendship += 1
    jump companion_backstory 



    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
