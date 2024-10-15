import random
import statistics  

class Player:
    def __init__(self, name):
        self.name = name  # Name of the player
        self.score = 0    # Total score of the player
        self.turn_total = 0  # Score for the current turn
        self.roll_count = 0  # Count of rolls in the current game
        self.sixes_count = 0  # Count of consecutive sixes

    def roll_die(self, die):
        roll = die.roll()  # Roll the die
        self.roll_count += 1  # Increment roll count

        if roll == 1:
            print(f"{self.name} rolled a 1! No points this turn.")
            self.turn_total = 0  # End turn if rolling a 1
            self.sixes_count = 0  # Reset sixes count
        elif roll == 6:
            self.turn_total += roll  # Add roll to turn total
            self.sixes_count += 1  # Increment consecutive sixes count
            print(f"{self.name} rolled a {roll}. Turn total: {self.turn_total}")
            if self.sixes_count == 6:
                print(f"{self.name} rolled six sixes in a row! {self.name} wins!")  # Fun feature
                return True  # Win condition
        else:
            self.turn_total += roll  # Add roll to turn total
            self.sixes_count = 0  # Reset sixes count
            print(f"{self.name} rolled a {roll}. Turn total: {self.turn_total}")

        return False  # No win condition

    def hold(self):
        self.score += self.turn_total  # Add turn total to overall score
        print(f"{self.name} holds. Total score: {self.score}")
        self.turn_total = 0  # Reset turn total for next turn

    def reset_turn(self):
        self.turn_total = 0  # Reset the turn total at the start of each turn

class Die:
    def __init__(self, sides=6):
        self.sides = sides  # Number of sides on the die

    def roll(self):
        return random.randint(1, self.sides)  #rolling the die

class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]  # Create two players
        self.die = Die()  # Create a die
        self.current_player = 0  #Track whose turn it is
        self.total_rolls = 0  # Track total rolls for the d20 this is purely because I'm a dnd nerd

    def play(self):
        while True:
            player = self.players[self.current_player]  # Get the current player
            player.reset_turn()  # Reset turn total
            print(f"{player.name}'s turn:")
            while True:
                # Roll a d20 every 100 rolls for fun
                if self.total_rolls % 100 == 0 and self.total_rolls > 0:
                    d20_roll = random.randint(1, 20)  # Roll a d20
                    print(f"Bonus roll! You rolled a d20: {d20_roll}")  # a fighting chance

                choice = input("Roll (r) or Hold (h)? ")
                if choice == 'r':
                    if player.roll_die(self.die):  # Player rolls the die
                        return  # End the game if they win
                    self.total_rolls += 1  # Increment total rolls
                    if player.turn_total == 0:
                        break  # End turn if rolled a 1
                elif choice == 'h':
                    player.hold()  # Player holds their turn
                    break
            if player.score >= 100:
                print(f"{player.name} wins!")  # Check for a winner
                break
            self.switch_turn()  # Switch to the next player

    def switch_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)  # Change turn

# Main program
if __name__ == "__main__":
    random.seed(0)  # Set the seed for reproducibility
    game = Game()  # Create a new game instance
    game.play()  # Start the game
