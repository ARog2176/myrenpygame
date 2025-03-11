label companion_backstory:
    scene background with dissolve
    "You walk on for awhile."
    m "Now that we're past that fight, who exactly are you?"
    if player_creature == "CaptianCringe":
        jump CaptainCringe_dialouge
    elif player_creature == "CaffeneCrusader":
        jump CaffeneCrusader_dialouge
    elif player_creature == "RavingRevenge":
        jump RavingRavenge_dialouge

label CaptainCringe_dialouge: 
        show CaptainCringe: 
            xalign 0.1
            yalign 0.6
        if friendship >= 5:
            c "I just make others cringge so hard and I simply win like that."
        else:
            c "I don't really like to talk about myself. Sorry."
        m "Okay then. What else do you do when you're not fighting crime?"
        c "I love to take walks in the city."
        m "Want to continue walking?"
        c "Sure!"
        m "Why is that dog looking at you strangely?"
        c "Uhh, it's probably nothing..."
        m "My hero signal is going off. There is an enemy on this path"
        c "My thing isnt going off."
        m "Oh my gosh. It's you, isn't it?"
        c "Yes. But you'll never catch me. I'm going underground."
        return

label CaffeneCrusader_dialouge: 
        show CaffeneCrusader: 
            xalign 0.1
            yalign 0.6
        if friendship >= 5:
            c "I constantly have caffene coursing through my veins."
            c "It makes me so hyper that I'm able to run fast and always be awake to fight crime."
        else:
            c "I don't really like to talk about myself. Sorry."
        m "I love to take walks in the city."
        m "Want to continue walking?"
        c "Sure!"
        m "Why is that dog looking at you strangely?"
        c "Uhh, it's probably nothing..."
        m "My hero signal is going off. There is an enemy on this path"
        c "My thing isnt going off."
        m "Oh my gosh. It's you, isn't it?"
        c "Yes. But you'll never catch me. I'm going underground."
        return

label RavingRavenge_dialouge: 
        show RavingRavenge: 
            xalign 0.1
            yalign 0.6
        if friendship >= 5:
            c "My goal is to get revenge. I don't care what happens, as long as I get revenge."
        else:
            c "I don't really like to talk about myself. But I get the job done."
        m "What else do you do when you're not fighting crime?"
        c "I love to take walks in the city."
        m "Want to continue walking?"
        c "Sure!"
        m "Why is that dog looking at you strangely?"
        c "Uhh, it's probably nothing..."
        m "My hero signal is going off. There is an enemy on this path"
        c "My thing isnt going off."
        m "Oh my gosh. It's you, isn't it?"
        c "Yes. But you'll never catch me. I'm going underground."

        return