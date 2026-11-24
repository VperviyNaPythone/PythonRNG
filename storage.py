def load_save():
    try:
        with open("save.txt", "r") as save_file:
            return (
                int(save_file.readline()),
                int(save_file.readline()),
                int(save_file.readline()),
                int(save_file.readline()),
                int(save_file.readline()),
                int(save_file.readline()),
                int(save_file.readline()),
            )
    except FileNotFoundError:
        return (0, 0, 0, 0, 0, 0, 0)


def save_game(balance, mythics, legendaries, ultras, breakthrough, rolls, lucky_glove_buy):
    with open("save.txt", "w") as save_file:
        save_file.write(f"{balance}\n")
        save_file.write(f"{mythics}\n")
        save_file.write(f"{legendaries}\n")
        save_file.write(f"{ultras}\n")
        save_file.write(f"{breakthrough}\n")
        save_file.write(f"{rolls}\n")
        save_file.write(f"{lucky_glove_buy}\n")
