class Round:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue


    def __eq__(self, other) -> bool:
        return self.red == other.red and self.green == other.green and self.blue == other.blue

class Game:
    def __init__(self, id: int):
        self.id = id
        self.rounds: list[Round] = []
        self.reds = 0
        self.greens = 0
        self.blues = 0

    def add_round(self, red: int, green: int, blue: int):
        self.rounds.append(Round(red, green, blue))
        self.reds += red
        self.greens += green
        self.blues += blue

    def is_valid_game(self, max_red: int, max_green: int, max_blue: int) -> bool:
        rounds: list[Round] = []

        for round in self.rounds:
            if round.red <= max_red \
                    and round.green <= max_green \
                    and round.blue <= max_blue:
                rounds.append(round)
            else:
                print("Failed", round.red, round.green, round.blue)

        return len(rounds) == len(self.rounds)

    def get_powers(self) -> int:
        red_max = 0
        green_max = 0
        blue_max = 0
        for round in self.rounds:
            red_max = max(red_max, round.red)
            green_max = max(green_max, round.green)
            blue_max = max(blue_max, round.blue)

        return red_max * green_max * blue_max

    def __eq__(self, other) -> bool:
        if self.id != other.id:
            return False

        for round in other.rounds:
            if not self.rounds.__contains__(round):
                return False

        return True


def parse_game(row: str) -> Game:
    (game_id, details) = row.split(":")
    id = game_id.split(" ")[1]

    game = Game(int(id))
    for detail in details.split(";"):
        (red, green, blue) = parse_details(detail)
        game.add_round(red, green, blue)

    return game


def parse_details(details: str) -> tuple[int, int, int]:
    parts = details.split(",")
    red = 0
    green = 0
    blue = 0

    for color in parts:
        (value, name) = color.strip().split(" ")
        if name.strip().lower() == "red":
            red = int(value)
        elif name.strip().lower() == "green":
            green = int(value)
        elif name.strip().lower() == "blue":
            blue = int(value)
        else:
            print("Unknown color", name)

    return (red, green, blue)
