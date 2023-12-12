class Card:
    def __init__(self, contents: str, card_dict: dict) -> None:
        (winners_part, numbers) = contents.split("|")
        self.numbers: list[int] = []
        self.winners: list[int] = []
        self.additional_cards: list[int] = []
        self.name = self.get_name(winners_part)
        self.card_dict = card_dict

        for number in [n for n in numbers.strip().split(" ") if n]:
            n = number.strip()
            self.numbers.append(int(n))

        for winner in [w for w in winners_part.split(":")[1].strip().split(" ") if w]:
            w = winner.strip()
            self.winners.append(int(w))

    def get_value(self):
        winners = [w for w in self.numbers if w in self.winners]

        result = 0
        additional_count = 1

        for _ in range(len(winners)):
            if result == 0 and self.name not in self.card_dict.keys():
                key = self.name
                key = self.name + additional_count
                if key in self.card_dict.keys():
                    self.card_dict[key] += 1
                else:
                    self.card_dict[key] = 1
                additional_count += 1
                result += 1
                continue

            key = self.name + additional_count
            if key in self.card_dict.keys():
                self.card_dict[key] += 1
            else:
                self.card_dict[key] = 1
            additional_count += 1
            result *= 2
        return result

    def get_name(self, value):
        for v in [n for n in value.strip().split(":")[0].strip().split(" ") if n]:
            try:
                return int(v)
            except ValueError:
                pass
        raise Exception("Bad")

