name = input("Enter your name: ")
print("\n\n")
print(f"Hello {name}! Welcome to the Choose_your_own_adventure game.")
print("\n\n")

answer = input("You find yourself at a crossroads in a mysterious forest. The left path is well-worn, and the right one is overgrown. What will you choose [right or left]: ").lower()

if answer == "right":
    print("\n\n")
    print("You have chosen right")
    print("\n\n")
    print("The overgrown path leads you through a dense thicket, with thorns and vines making the journey challenging. As you persevere, you come across an ancient temple hidden deep within the forest. You lost.")
    print("\n\n")
elif answer == "left":
    print("\n\n")
    print("\n\n")
    answer2 = input("Taking the left path leads you to a clearing where friendly forest creatures have gathered. The wise owl offers you a magical amulet. What will you do [accept or decline]: ").lower()

    if answer2 == "accept":
        print("\n\n")
        print("\n\n")
        print("The amulet glows brighter as you accept it. It grants you the ability to communicate with nature. As you move forward, you come across a river.")
        answer3 = input("How will you proceed [ask river or cross alone]: ").lower()

        if answer3 == "ask river":


            answer4 = input("The river advises you to follow a hidden trail to the mountains. As you ascend, you encounter a mystical gate guarded by a riddle-speaking guardian. Solve the riddle or risk being stuck. [RIDDLE or BYPASS]: ").lower()
            print("\n\n")
            if answer4 == "riddle":
                print("\n\n")
                print("\n\n")
                answer5 = input("Solving the riddle allows you to pass through the gate into a magical realm. Here, you encounter a group of beings engaged in a quest to save their land. Will you join them? [JOIN QUEST or GO ALONE]: ").lower()
                print("\n\n")
                print("\n\n")
                if answer5 == "join quest":
                    print("\n\n")
                    print("\n\n")
                    answer6 = input("Your decision to join the quest leads to various challenges and encounters. During a confrontation with a formidable foe, you find a hidden portal leading to a futuristic city. What will you do: [CITY or HELP] ").lower()

                    if answer6 =="help":
                        print("\n \n")
                        print("In the magical realm, you encounter beings engaged in a quest to save their land. Touched by their cause, you decide to stay and offer your assistance. Your involvement in the quest unveils unforeseen challenges and adventures.")
                    elif answer6=="city":
                        print("\n \n")
                        answer7=input("In the city, you discover advanced technology and meet a group of scientists working on a groundbreaking project. They invite you to participate. What's your choice? [PROJECT or EXPLORE]: ").lower()

                        if answer7=="project":
                            answer8=input("Your involvement in the project unveils a time-traveling device. You can use it to revisit any point in your journey. Where and when will you go? [END GAME or CONTINUE]").lower()

                            if answer8=="end game":
                                print("\n \n")
                                print("CONGRATULATIONS YOU REACHED THE END OF THE GAME")
                                quit()
                            elif answer8=="continue":
                                print("\n \n")
                                print("\n \n")
                                print("TO BE CONTINUED")
                                quit()
                            else:
                                print("\n \n")
                                print("\n \n")
                                print("Sorry thats not valid")
                                quit()

                        elif answer7=="explore":
                            print("\n \n")
                            print("\n \n")
                            print("As you traverse through the magical realm, you stumble upon a portal that transports you to a futuristic city. Declining the invitation to join the scientific project, you explore the advanced city filled with towering skyscrapers and futuristic technology.")
                        else:
                            print("\n\n")
                            print("You lost. End of your adventure")
                            quit()
                    else:
                        print("\n\n")
                        print("You lost.")
                        quit()




                    print("\n\n")
                elif answer5 == "go alone":
                    print("\n\n")
                    print("\n\n")
                    print("Avoiding the mystical gate, you choose to continue your journey independently. The path leads you through a magical realm filled with enchanting landscapes and mysterious creatures.")
                    print("\n\n")
                    print("You lost.")
                    quit()

            else:
                print("\n\n")
                print("Wrong choice")
                quit()
        elif answer3 == "cross alone":
            print("\n\n")
            print("\n\n")
            print("Approaching a river on the outskirts of the forest, you attempt to cross it without seeking guidance. The amulet begins to glow, allowing you to communicate with the river. It advises you to follow a hidden trail that leads to the mountains.")
            print("\n\n")
            print("You lost.")
    elif answer2 == "decline":
        print("\n\n")
        print("You decide to politely decline the friendly creatures' offer, choosing to maintain your independence. Your journey takes you deeper into the forest, and you stumble upon a forgotten temple obscured by the foliage.")
        print("\n\n")
        print("You lost.")
    else:
        print("\n\n")
        print("Wrong direction, you lose.")
        quit()
else:
    print("\n\n")
    print("Wrong direction, you lose.")
    quit()
