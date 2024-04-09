# @author Daniel Pavenko
# @date 04/09/24
# Programming assignment 2 for Design and Analysis of Algorithms. This program handles the knapsack creation

import os
import time
import statistics
from multiprocessing import Process

# Main method
def main():
  createResultsDirectories()
  processTextFiles()

# Creates the results directory hierarchy
def createResultsDirectories():
    print("\tCreating result directories.")
    baseDir = "results"
    sizes = ["small", "medium", "large"]
    types = ["unsorted", "sorted", "reverse_sorted"]
  
    for size in sizes:
        for sortType in types:
            dirPath = os.path.join(baseDir, size, sortType)
            os.makedirs(dirPath, exist_ok=True)

# Creates a process for small, medium and large files
def processTextFiles():
    sizes = ["small", "medium", "large"]
    processes = []

    for size in sizes:
        p = Process(target=processFilesWorker, args=(size,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

# Processes text files by sorting them, measuring their efficiency, and writing that measurment to a results file
def processFilesWorker(size):
    print(f"\tProcessing and sorting text files for size: {size}")
    readDir = "dataset"
    writeDir = "results"
    types = ["unsorted", "sorted", "reverse_sorted"]
    sortFunctions = {'quickSort': quickSort, 'mergeSort': mergeSort, 'heapSort': heapSort}

    for sortType in types:
        runTimes = {sortName: [] for sortName in sortFunctions.keys()}
        resultContent = []

        for i in range(1, 31):
            fileName = f"{size}_{sortType}_{i}.txt"
            readFilePath = os.path.join(readDir, size, sortType, fileName)
            with open(readFilePath, 'r') as file:
                integers = [int(num) for num in file.read().split()]

            for sortName, sortFunc in sortFunctions.items():
                runTimeMS = sortAndMeasure(list(integers), sortFunc)
                runTimes[sortName].append(runTimeMS)
                resultContent.append(f"{sortName} - {fileName} - {runTimeMS:.4f} ms\n")
            resultContent.append("\n")

        for sortName, times in runTimes.items():
            mean = statistics.mean(times)
            stdev = statistics.stdev(times)
            resultContent.append(f"{sortName} mean: {mean:.4f} ms, standard deviation: {stdev:.4f}\n")

        writeFilePath = os.path.join(writeDir, size, sortType, f"{size}_{sortType}_results.txt")
        with open(writeFilePath, 'w') as file:
            file.writelines(resultContent)
     
# Calls appropriate sort and measures execution time of said sort
def sortAndMeasure(integers, sortFunc):
    startTime = time.perf_counter()
    sortFunc(integers)
    endTime = time.perf_counter()
    return (endTime - startTime) * 1000

# Sorts a list of integers using quicksort
def quickSort(integers):
    if len(integers) <= 1: # len of 0 or 1 don't need to be sorted
        return integers
    
    first = integers[0]
    middle = integers[len(integers) // 2]
    last = integers[len(integers) - 1]
    
    # Sorting and picking middle element to find median of three
    medianOfThree = sorted([first, middle, last])[1]
    
    # Using the median of three as the pivot
    pivot = medianOfThree
    
    left = [x for x in integers if x < pivot]
    middle = [x for x in integers if x == pivot]
    right = [x for x in integers if x > pivot]
    
    return quickSort(left) + middle + quickSort(right)

# Sorts a list of integers using mergesort
def mergeSort(integers):
    if len(integers) > 1: # Stop the recursive call once we've split down to single elements
      mid = len(integers) // 2  # Finding the mid of the array
      L = integers[:mid]  # Dividing the array elements into 2 halves
      R = integers[mid:]

      mergeSort(L)  # Sorting the first half
      mergeSort(R)  # Sorting the second half

      i = j = k = 0

      # Copy data to temp arrays L[] and R[]
      while i < len(L) and j < len(R):
          if L[i] < R[j]:
              integers[k] = L[i]
              i += 1
          else:
              integers[k] = R[j]
              j += 1
          k += 1

      # Checking if any element was left
      while i < len(L):
          integers[k] = L[i]
          i += 1
          k += 1

      while j < len(R):
          integers[k] = R[j]
          j += 1
          k += 1

# Helper function for heapSort
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2 * i + 1
    r = 2 * i + 2  # right = 2 * i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # See if right child of root exists and is greater than the largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# Sorts a list of integers using heapsort
def heapSort(integers):
    n = len(integers)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(integers, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        integers[i], integers[0] = integers[0], integers[i]  # swap
        heapify(integers, i, 0)

# Check if being run directly or imported
if __name__ == "__main__":
    startTime = time.perf_counter()
    print("Custom sort started...")
    main()
    endTime = time.perf_counter()
    runTimeS = (endTime - startTime)
    runTimeMin = runTimeS / 60
    runTimeMS = runTimeS * 1000
    print(f"Execution time: {runTimeMS:.2f} ms or {runTimeS:.2f} sec or {runTimeMin:.2f} min")
