class Player:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        p1_choice = self.player1.choice
        p2_choice = self.player2.choice

        # Rocks
        if p1_choice == "rock" and p2_choice == "rock":
            return "It's a tie"
        elif p1_choice == "rock" and p2_choice == "paper":
            return f"paper beats rock, {self.player2.name} wins"
        elif p1_choice == "rock" and p2_choice == "scissors":
            return f"rock beats scissors, {self.player1.name} wins"
        # paper
        elif p1_choice == "paper" and p2_choice == "rock":
            return f"paper beats rock, {self.player1.name} wins"
        elif p1_choice == "paper" and p2_choice == "paper":
            return "It's a tie"
        elif p1_choice == "paper" and p2_choice == "scissors":
            return f"scissors beats paper, {self.player2.name} wins"
        # scissors
        elif p1_choice == "scissors" and p2_choice == "rock":
            return f"rock beats scissors, {self.player2.name} wins"
        elif p1_choice == "scissors" and p2_choice == "paper":
            return f"scissors beats paper, {self.player1.name} wins"
        elif p1_choice == "scissors" and p2_choice == "scissors":
            return "It's a tie"
