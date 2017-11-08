print("What is your name?")
name = input().title()

if name == "Andrew":
    print("No way " + name + " is my name too.")
else:
    print(name + "is a pretty cool name.")


print("What is you favorite sport?")
sport = input().title()

if sport == "Basketball":
    print("Did you know Donovan Mitchell is the GOAT?")
elif sport == "Football":
    print("What is your favorite team?")
    team = input().title()

    if team == "Packers":
        print("Mine too! " + team + " are the best team in the NFL.")
    elif team == "Patriots":
        print("Don't be a winner picker.")
    else:
        print(team + "is not my favorite football team.")

        
    print("Aaron Rodgers has the highest QBR of all time.")
elif sport == "Crew":
    print("I do crew too")
else:
    print(sport + " sounds fun.")


print("What is your favorite TV show")
tvshow = input().title()

if tvshow == "Flash" or tvshow == "The Flash" or tvshow == "DC Legend's of Tomorrow":
    print("I love " + tvshow + " too! Who is your favorite character?")
    character == input().title()

    if character == "The Flash" or character == "Kid Flash" or character == "Cisco" or character == "Iris" or character == "Kaitlin" or character == "Barry" or character == "Joe" or character == "Wally" or character == "HR" or character == "Jax" or character == "Professor Stein" or character == "Firestorm" or character == "Sarah" or character == "Ray Palmer" or character == "The Atom" or character == "Heatwave" or character == "Mick" or character == "Rip Hunter" or character == "Gideon":
        print("I like " + character + " too!")
    else:
        print(character + " is not my favorite.")
elif tvshow == "Suite Life of Zack and Cody" or tvshow == "Wiards Of Waverly Place":
    print("I used to watch " + tvshow + " too!")
else:
    print("That " + tvshow + "is bad.")


print("")
