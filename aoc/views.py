from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .services.parser import combine_numbers, get_numbers
from .services.parser_two import Game, parse_game

# Create your views here.

def day_one(request: HttpRequest):
    print(request)
    if request.method == "GET":
        return render(request, "aoc/day1.html")

    if request.method == "POST":
        values = [x.strip("\r") for x in request.POST["list"].split("\n")]
        num_values = [ get_numbers(x) for x in values ]
        combined = 0
        for num in num_values:
            combined += combine_numbers(num)
            print(combined)
        return render(request, "aoc/day1.html", { "result": combined }) 

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

        return render(request, "aoc/day2.html", { "result": result })

    return HttpResponse("day_two")

def day_three(request: HttpRequest):
    print(request)

    if request.method == "GET":
        return render(request, "aoc/day3.html")

    if request.method == "POST":
        print(request.POST)
        values = [x.strip("\r") for x in request.POST["list"]]
