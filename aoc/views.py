from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from aoc.services.parser_four import Card

from .services.parser import combine_numbers, get_numbers
from .services.parser_two import parse_game
from .services.parser_three import find_gears, find_valid_numbers, get_lines, get_rows

# Create your views here.


def index(request: HttpRequest):
    return render(request, "aoc/index.html", {"pages": range(1, 20)})


def day_one(request: HttpRequest):
    print(request)
    if request.method == "GET":
        return render(request, "aoc/day1.html")

    if request.method == "POST":
        values = [x.strip("\r") for x in request.POST["list"].split("\n")]
        num_values = [get_numbers(x) for x in values]
        combined = 0
        for num in num_values:
            combined += combine_numbers(num)
            print(combined)
        return render(request, "aoc/day1.html", {"result": combined})

    return HttpResponse("day_one")


def day_two(request: HttpRequest):
    print(request)

    if request.method == "GET":
        return render(request, "aoc/day2.html")

    if request.method == "POST":
        print(request.POST)
        red = int(request.POST["red"])
        green = int(request.POST["green"])
        blue = int(request.POST["blue"])
        values = [x.strip("\r") for x in request.POST["list"].split("\n")]

        # games: list[Game] = []
        result = 0
        for value in values:
            print(value)
            g = parse_game(value)
            result += g.get_powers()
            # valid = g.is_valid_game(red, green, blue)
            # print(valid)
            # if valid:
            #     result = result + g.id

        print(result)

        return render(request, "aoc/day2.html", {"result": result})

    return HttpResponse("day_two")


def day_three(request: HttpRequest):
    # print(request)

    if request.method == "GET":
        return render(request, "aoc/day3.html", {"day": 3, "day_url": "day_three"})

    if request.method == "POST":
        print(request.POST)
        values = [x.strip("\r") for x in request.POST["list"]]

        rows = get_rows(get_lines(request.POST["list"]))

        gears = request.POST["gears"]
        if gears == "on":
            values = find_gears(rows)
        else:
            values = find_valid_numbers(rows)

        print(values)

        return render(
            request,
            "aoc/day3.html",
            {"day": 3, "day_url": "day_three", "result": sum(values)},
        )

    return HttpResponse("day_three")


def day_four(request: HttpRequest):
    if request.method == "GET":
        return render(request, "aoc/day4.html", {"day": 4, "day_url": "day_four"})

    if request.method == "POST":
        print(request.POST)

        values = [x.strip("\r") for x in request.POST["list"].split("\n")]
        additional = request.POST.get("additional")

        result: list[int] = []
        card_dict: dict = {}
        additional_result = 0
        for value in values:
            card = Card(value, card_dict)
            if additional:
                if card.name not in card_dict:
                    card_dict[card.name] = 1
                else:
                    card_dict[card.name] += 1
                for _ in range(
                    card_dict[card.name] if card.name in card_dict.keys() else 0
                ):
                    card.get_value()
                if card.name in card_dict.keys():
                    additional_result += card_dict[card.name]
            else:
                result.append(card.get_value())

        return_value = additional_result if additional_result else sum(result)

        if additional:
            print("Additional requested")

        return render(
            request,
            "aoc/day4.html",
            {"day": 4, "day_url": "day_four", "result": return_value},
        )
    return HttpResponse("day_four")


def day_five(request: HttpRequest):
    if request.method == "POST":
        print(request.POST)

        return render(
            request, "aoc/day5.html", {"day": 5, "day_url": "day_five", "result": {}}
        )

    return render(request, "aoc/day5.html", {"day": 5, "day_url": "day_five"})
