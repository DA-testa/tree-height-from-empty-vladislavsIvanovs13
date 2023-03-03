# python3

import sys
import threading
import numpy
import time


def compute_height(n, parents):
    max_height = 0
    for i in numpy.arange(n):
        counter = 1
        number = int(parents[i])
        while not (number == -1):
            counter += 1
            number = int(parents[number])
        max_height = max(max_height, counter)
    return max_height


def main():
    start = time.time()
    command = input()
    if "F" in command:
        file_name = input()
        path = "test/" + file_name
        if not "a" in file_name:
            contents = open(path, "r")
            text = contents.read()
            contents.close()
            partitioned = text.partition("\n")
            n = int(partitioned[0])
            arr = partitioned[2].split(" ")
            arr = numpy.array(arr)
            print(compute_height(n, arr))
            print(time.time() - start)
        
        
    elif "I" in command:
        n = int(input())
        parents = input()
        arr = parents.split(" ")
        arr = numpy.array(arr)
        print(compute_height(n, arr))
        
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
