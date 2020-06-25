# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    result1 = -1
    result2 = -1
    for index in range(n):
        if(numbers[index]>result1):
            max1index = index
            result1 = numbers[index]
    del numbers[max1index]
    for index in range(len(numbers)):
        if(numbers[index]>result2):
            result2 = numbers[index]
    return result2*result1


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
