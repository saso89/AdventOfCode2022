from copy import deepcopy

def compare_lists(first, second):
    #print('compare lists')
    while len(first) > 0 and len(second) > 0:
        left = first.pop(0)
        right = second.pop(0)
        #print(f"{left=}, {right=}")
        if type(left) == int and type(right) == int:
            if left < right:
                return 1
            elif left > right:
                return -1
        if type(left) == list and type(right) == list:
            sub_comparison = compare_lists(left, right)
            if sub_comparison != 0:
                return sub_comparison
        if type(left) == int and type(right) == list:
            sub_comparison = compare_lists(list([left]), right)
            if sub_comparison != 0:
                return sub_comparison
        if type(left) == list and type(right) == int:
            sub_comparison = compare_lists(left, list([right]))
            if sub_comparison != 0:
                return sub_comparison
    #print('compare lengths', f"{first=}, {second=}")
    if len(first) < len(second):
        return 1
    elif len(first) > len(second):
        return -1
    else:
         return 0

def solve1(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    index = 1
    indices = []
    pairs = []
    while len(lines) > 0:
        list_a = eval(lines.pop(0))
        list_b = eval(lines.pop(0))
        if len(lines) > 0:
            lines.pop(0)

        #print(f"{index=}")
        #print(f"{list_a=}, {list_b=}")
        comparison = compare_lists(list_a, list_b)
        if comparison == 1:
            indices.append(index)
        index += 1
        #print("-----")
    print(indices)
    print(sum(indices))

solve1('day_13.txt')



def solve2(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    smaller_than_2 = 0
    smaller_than_6 = 0
    while len(lines) > 0:
        line = lines.pop(0)
        if len(line) == 0:
            continue
        list_from_file = eval(line)
        
        if compare_lists(deepcopy(list_from_file), [[2]]) == 1:
            smaller_than_2 += 1
        if compare_lists(deepcopy(list_from_file), [[6]]) == 1:
            smaller_than_6 += 1
        
    position_of_2 = smaller_than_2 + 1
    position_of_6 = smaller_than_6 + 2
    print(f"{position_of_2=}, {position_of_6=}")
    print(position_of_2 * position_of_6)

solve2('day_13.txt')



