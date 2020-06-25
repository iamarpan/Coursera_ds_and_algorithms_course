# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    ratio = list(map(lambda x:(x[1]/x[0]),zip(weights,values)))
    sortedRatio,weights = [list(t) for t in zip(*sorted(zip(ratio,weights),reverse=True))]
    for weight,ratio in zip(weights,sortedRatio):
        if(capacity==0):
            break
        if(int(weight)<=capacity):
            capacity -= weight
            value += weight*ratio
        else:
            value+=capacity*ratio
            capacity=0


    return value


if __name__ == "__main__":
    number,capacity = map(int,input().split())
    weights = []
    values = []
    for a in range(number):
        value,weight = map(int,input().split())
        values.append(value)
        weights.append(weight)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
