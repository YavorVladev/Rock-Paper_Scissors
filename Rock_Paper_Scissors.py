def play(player1_choice, player2_choice, p1_name, p2_name):
    if player2_choice == loses_to[player1_choice]:
        return f"{p1_name} wins by picking {player1_choice}! {p2_name} picked {player2_choice}"
    if player1_choice == loses_to[player2_choice]:
        return f"{p2_name} wins by picking {player2_choice}! {p1_name} picked {player1_choice}"
    if player1_choice == player2_choice:
        return "tie"


loses_to = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}
player1_name = input("First player name: ")
player2_name = input("Second player name: ")
player1 = input(f"{player1_name} choose between: rock, paper or scissors ").lower()
player2 = input(f"{player2_name} choose between: rock, paper or scissors ").lower()
print(play(player1, player2, player1_name, player2_name))
