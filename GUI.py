import os
import time
import random

def get_terminal_size():
    """Gets the current terminal window size."""
    try:
        rows, cols = os.get_terminal_size()
        return rows, cols
    except OSError:
        return 24, 80

def display_player_info(name, rating, wins, losses, hp, max_hp, row):
    """Displays player information at the specified row."""
    rows, cols = get_terminal_size()
    info = f"{name} (Rating: {rating}) [W:{wins}/L:{losses}] HP: {hp}/{max_hp}"
    hp_bar_length = 20
    filled_length = int(hp_bar_length * hp / max_hp)
    bar = '█' * filled_length + '-' * (hp_bar_length - filled_length)
    hp_display = f"[{bar}]"
    output = f"{info} {hp_display}"

    if row == 1:
        print(output.ljust(cols // 2), end=f"\r\033[{row};0H")  # Top left
    elif row == 2:
        print(output.rjust(cols // 2), end=f"\r\033[{row};0H")  # Top right

def display_fight_log(log_messages, start_row):
    """Displays the scrolling fight log starting at the specified row."""
    rows, cols = get_terminal_size()
    log_height = rows - start_row - 1 # Leave space for player info and potentially a bottom prompt

    # Clear the log area
    for i in range(start_row, start_row + log_height):
        print(" " * cols, end=f"\r\033[{i};0H")

    # Display the latest log messages
    start_index = max(0, len(log_messages) - log_height)
    for i, message in enumerate(log_messages[start_index:]):
        line_number = start_row + i
        print(message.center(cols), end=f"\r\033[{line_number};0H")

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    player1_name = "Hero"
    player1_rating = 1200
    player1_wins = 5
    player1_losses = 2
    player1_hp = 80
    player1_max_hp = 100

    player2_name = "Goblin"
    player2_rating = 900
    player2_wins = 1
    player2_losses = 3
    player2_hp = 50
    player2_max_hp = 75

    fight_log = []
    log_start_row = 3  # Start the log display from the third row

    clear_screen()

    while player1_hp > 0 and player2_hp > 0:
        display_player_info(player1_name, player1_rating, player1_wins, player1_losses, player1_hp, player1_max_hp, 1)
        display_player_info(player2_name, player2_rating, player2_wins, player2_losses, player2_hp, player2_max_hp, 2)

        attacker = random.choice([player1_name, player2_name])
        damage = random.randint(5, 15)

        if attacker == player1_name:
            player2_hp -= damage
            fight_log.append(f"{player1_name} attacks {player2_name} for {damage} damage!")
        else:
            player1_hp -= damage
            fight_log.append(f"{player2_name} attacks {player1_name} for {damage} damage!")

        display_fight_log(fight_log, log_start_row)
        time.sleep(0.5)

    if player1_hp <= 0:
        fight_log.append(f"{player2_name} wins!")
    else:
        fight_log.append(f"{player1_name} wins!")

    display_fight_log(fight_log, log_start_row)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()