# python3

import numpy

def compute_height(n, parents):
    possible_heights = [0 for i in range(n)]
    max_height = 0
    for i in numpy.arange(n):
        height = 0
        j = i
        while not (int(parents[j]) == -1):
            if (possible_heights[j] != 0):
                height += possible_heights[j] 
                break
            height += 1
            j = int(parents[j])
        possible_heights[i] = height
        max_height = max(max_height, possible_heights[i])
    return max_height + 1

def main():
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
        
        
    elif "I" in command:
        n = int(input())
        parents = input()
        arr = parents.split(" ")
        arr = numpy.array(arr)
        print(compute_height(n, arr))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()
main()
