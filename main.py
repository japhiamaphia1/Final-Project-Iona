
def start_adventure():
    """Start the text-based adventure game"""
    print("               Welcome to the AI/Machine Learning Game!")
    print()
    print("Hey there! I'm AIA, your AI assistant! Today I will be helping you learn about how AI can help with Climate Change and the Medical Field!")
    print()
    print("Which game would you like to play?")
    print()
   

    # Present the first choice to the player
    print("1. How AI can help with Climate Change.")
    print("2. How AI can help in the Medical Field.")
    print()

    # Get the player's choice
    choice1 = input("Which game would you like to play? (1 or 2): ")
    print("_________________________________________________________")

    # Branching story based on the first choice
    if choice1 == '1':
        print()
        print("Welcome to the AI Climate Change Game!")

        name = input("What is your name? ")
        print("Hello " + name + "! Let's start our adventure together! 😊")
        print()

        print("Welcome to Skyrift! Right now the name of the city sounds futuristic, but the city isn't in its best shape.")
        print("The city is struggling with climate change with leads to the air quality becoming terrible.")
        player_idea = input("What ideas do you have to make Skyrift a better city? ")
        print("That's amazing! Your idea to " + player_idea + " is a great one!")
        print()

        print("As an AI bot, some actions I can do are analyzing data for the city and predicting weather updates!")
        print("Robots can help many cities in multiple ways. Some of the ways include making self-driving taxis operated by AI recognition.")
        print("Going back to the topic of climate change, robots and AI can make technology that plants trees all around Skyrift!")
        print()

        print("Do you know why planting trees all around Skyrift can help the city?")
        print("1. Trees can help make the air quality better.")
        print("2. Trees can help make the city warmer.")
        print()

        choice_tree = input("What do you think? (1 or 2): ")
        print()

        if choice_tree == '1':
            print("That's right! Trees can help make air quality better and they recycle oxygen!")
        elif choice_tree == '2':
            print("That's unfortunately wrong! Trees can help make air quality better and they recycle oxygen!")
        else:
            print("Invalid choice, trees can help make air quality better and they recycle oxygen!")

       
        print("___________________________________________________")
        print()
        print("AI can do many things to help Skyrift and other cites suffering with climate change!") 
        print("We can help predict weather updates and make sure the city is prepared for any weather changes!")
        print("In the future, AI can help make cities better and help the world with climate change!")
        print("As of right now, AI is still being developed and we can't do everything, but we can do many things in the future!")
        print("___________________________________________________")
        print()
        choice2 = input("Did you learn anything new from this game? (Yes or No): ")
        print()

        if choice2 == 'Yes':
            print("Thank you for playing the AI Climate Change Game! I'm happy to know you learned something new!")
        elif choice2 == 'No':
            print("Sorry to hear that, but thank you for playing the AI Climate Change Game!")
        else:
            print("Sorry to hear that, but thank you for playing the AI Climate Change Game!")
        print()
        print("Thank you for playing the AI Climate Change Game!")

    

    
    
    
    
    
    
    elif choice1 == '2':
        print()
        print("Welcome to the AI Medical Field Game!")
        print("As an AI myself, we can help doctors and nurses in many ways.")
        print("_________________________________________________________")
        print()
        print("AI can help doctors in and out of sugrey!")
        print("We enhance the ability of doctors to diagnose and treat patients more accurately and efficiently.")
        print()
        print("AI can help doctors in surgery by providing real-time data and analysis during operations.")
        print("During surgrey, we can give real life assessments of the patient's health and give the doctor the best possible directions to proceed.")
        print()
        print("The prblem with AI in the medical field is that it ")

        print("You have two AI-powered tools to choose from:")
        print("1. AI system that plants trees automatically.")
        print("2. AI model that predicts air quality and pollution hotspots.")
        print()
        
        print("Do you know why AI can help in surgrey?")
        print("1. It can make surgery more successful.")
        print("2. It can help the doctors in times where the need help.")
        print("3. Both of these are helpful.")
        print()

        choice_tree = input("What do you think? (1 or 2): ")
        print()

        choice3 = input("Which AI tool would you like to deploy? (1 or 2): ")
        print()
        if choice3 == '1':
            print("Great choice! This answer is correct but so it the other one!")
        elif choice3 == '2':
            print("Great choice! This answer is correct but so it the other one!")
        elif choice3 == '3':
            print("That's right both of these answer can make surgrey more successful!")

        print("While people may think that AI can't help in the medical field, it can help in many ways!")

        print("___________________________________________________")
        print()
        choice4 = input("Did you learn anything new from this game? (Yes or No): ")
        print()

        if choice4 == 'Yes':
            print("Thank you for playing the AI Medical Game! I'm happy to know you learned something new!")
        elif choice4 == 'No':
            print("Sorry to hear that, but thank you for playing the AI Medical Game!")
        else:
            print("Sorry to hear that, but thank you for playing the AI Medical Game!")
        print()
        print("Thank you for playing the AI Medical Game!")
        
if __name__ == "__main__":
    start_adventure()


