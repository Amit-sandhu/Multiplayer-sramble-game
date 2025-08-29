# MULTIPLAYER SCRAMBLE WORD GAME

import random                                                        # imports random module to select words randomly

# List of words to choose from in the game
words = ["apple", "river", "mountain", "freedom", "galaxy", "ocean", "candle",
         "shadow", "blanket", "forest", "whisper", "journey", "thunder", "mirror",
         "diamond", "puzzle", "horizon", "notebook", "melody", "spark", "butterfly",
         "castle", "dream", "lantern", "feather", "rhythm", "planet", "secret",
         "lighthouse", "sunflower", "window", "firefly", "comet", "treasure",
         "meadow", "storm", "echo", "ivy", "breeze", "sapphire", "velvet", "pebble",
         "twilight", "ember"]

# Print game rules for the user
print("\n\n                   MULTIPLAYER SCRAMBLED WORD GAME                        ")
print("\n\n                        RULES FOR THE GAME                              ")
print("\n1) Read each instruction carefully")
print("2) There will be a scrambled word on the screen")
print("3) Take guesses and try to unscramble the word")
print("4) Type 'quit' anytime during guessing to give up")
print("\n                      Enjoy!")

# Main game loop to allow starting a new game
while True:
    start = input("\nStart a new game? yes/no: ").strip().lower()  # asks user to start the game
    if start == "yes":
        players = []                                               # list to store player names
        result = []                                                # list to store number of guesses each player took to guess the word

        # Loop to add multiple players
        while True:
            add_player = input("\nAdd new player? yes/no: ").strip().lower()                    # ask if a new player should be added
            
            if add_player == "yes":
                # Get valid player name
                while True:
                    name = input("Enter player name: ").strip()                                 # asks for player name
                    if name:
                        break
                    else:
                        print("Player name cannot be empty.")
                players.append(name)                                                            # add the player name to the players list

                guess_number = 1                                                                # counter for number of guesses for this player
                word = random.choice(words)                                                     # randomly choose a word from the list

                # Scramble the word
                scrambled_word = list(word)                                                     # convert word into a list of letters
                while True:
                    random.shuffle(scrambled_word)                                              # shuffle the letters
                    if "".join(scrambled_word) != word:                                         # ensure the scrambled word is not same as original
                        break
                print("\nScrambled word: ", " ".join(scrambled_word))                           # print scrambled letters

                # Loop to get guesses from the player
                while True:
                    guess = input("Enter your guess (or type 'quit' to give up): ").strip()
                    
                    # Handle empty input
                    if not guess:
                        print("Guess cannot be empty.")
                        continue
                    
                    # Handle quitting
                    if guess.lower() == "quit":
                        print(f"{name} gave up! The word was '{word}'.")
                        guess_number = float('inf')                                 # mark as did not finish so cannot win
                        break
                    
                    # Check if guess is correct
                    if guess.lower() == word.lower():
                        print(f"Congrats {name}! You got it right.")                # if correct, exit loop
                        break
                    else:
                        print(f"Your guess was wrong! Try again")                   # if incorrect, increment guesses
                        guess_number += 1

                result.append(guess_number)                                         # store the total guesses for this player

            elif add_player == "no":                                                # if no more players to add, determine winner
                if players:

                    # Filter out players who gave up (infinity guesses)
                    valid_results = [(i, g) for i, g in enumerate(result) if g != float('inf')]
                    if valid_results:

                        # Find minimum number of guesses

                        min_guesses = min(g for i, g in valid_results)
                        # Find all players who have minimum guesses (handle tie)

                        winners = [players[i] for i, g in valid_results if g == min_guesses]
                        if len(winners) == 1:
                            print(f"\nWinner: {winners[0]} with {min_guesses} guesses!")
                        else:
                            print(f"\nIt's a tie! Winners: {', '.join(winners)} with {min_guesses} guesses each!")
                    else:
                        print("No one guessed the word. No winners this round.")
                else:
                    print("No players played the game.")
                break                                                                # exit player-adding loop

            else:                                                                    # handle invalid input for adding a player
                print("Invalid input! Please enter yes or no.")

    elif start == "no":                                                              # user does not want to start a new game
        print("Have a nice day!")
        break                                                                        # exit main game loop

    else:                                                                            # handle invalid input for starting game
        print("Invalid input! Please enter yes or no.")



