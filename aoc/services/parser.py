from typing import List

num_map = [[ "one", "1" ],
           [ "two", "2" ],
           [ "three", "3" ],
           [ "four", "4" ],
           [ "five", "5" ],
           [ "six", "6" ],
           [ "seven", "7" ],
           [ "eight", "8" ],
           [ "nine", "9" ]]


def get_numbers(value: str) -> List[int]:
    result: List[int] = []
    result.append(get_number(value))
    result.append(get_number(value, True))
    # mapped = map_numbers(value)
    # for char in mapped:
    #     if char.isdigit():
    #         result.append(int(char))

    # print(result)
    return result

def combine_numbers(nums: list) -> int:
    result = 0
    if len(nums) == 0:
        result = 0
    elif len(nums) == 1:
        result = nums[0] * 10 + nums[0]
    else:
        result = nums[0] * 10 + nums[-1]

    # print(nums)
    # print(result)
    return result

def map_numbers(value: str) -> str:
    result = value
    temp = ""
    for c in value:
        temp = temp + c
        for map in num_map:
            result = temp.replace(map[0], map[1])
            temp = temp.replace(map[0], map[1])

    return result

def get_number(value: str, last: bool = False) -> int:
    temp = ""
    for i in range(len(value)):
        index = i if not last else (i + 1) * -1
        if value[index].isdigit():
            return int(value[index])
        temp = temp + value[index]
        for map in num_map:
            if (temp if not last else temp [::-1]).__contains__(map[0]):
                return int(map[1])
    return 0
