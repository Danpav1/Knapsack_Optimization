# @author Daniel Pavenko
# @date 03/07/24
# A python program that generates 270 text files (90 - 10,000 nums, 90, - 100,000 nums,
# 90 - 1,000,000 nums) which are filled with random numbers in range 0 <= x <= 9,999.

import os
import random
import time
from multiprocessing import Process

# Main method
def main():
    runGenerator()

# Starts the process(es) and runs generateFiles with appropriate inputs in parallel
def runGenerator():
    # Inputs used for generateFiles
    sizes = [("small", 10000), ("medium", 100000), ("large", 1000000)]
    # Queue of parallel processes
    processes = []

    # Start a new process for each entry in sizes, uses the tuple in sizes as input for generateFiles, adds
    # process to the queue "processes"
    for size, count in sizes:
        p = Process(target = generateFiles, args = (size, count))
        p.start()
        processes.append(p)

    # Waits for each process in queue to finish
    for p in processes:
        p.join()

# Generates files based on the size (small, medium, large) and count (number of integers in file) given to it
def generateFiles(size, count):
    baseDir = f"dataset/{size}"
    makeDirectory(baseDir)

    # Creates folder heirarchy
    unsortedDir = os.path.join(baseDir, "unsorted")
    sortedDir = os.path.join(baseDir, "sorted")
    reverseSortedDir = os.path.join(baseDir, "reverse_sorted")
    makeDirectory(unsortedDir)
    makeDirectory(sortedDir)
    makeDirectory(reverseSortedDir)

    # Creates the files and fills them with appropriate data
    for i in range(1, 31):
        # Unsorted
        nums = [str(random.randint(0, 9999)) for _ in range(count)]
        filePath = os.path.join(unsortedDir, f"{size}_unsorted_{i}.txt")
        writeNumbersToFile(filePath, nums)

        # Sorted (Low to High)
        sortedNums = sorted(nums, key = int)
        sortedFilePath = os.path.join(sortedDir, f"{size}_sorted_{i}.txt")
        writeNumbersToFile(sortedFilePath, sortedNums)

        # Reverse sorted (High to Low)
        reverseSortedNums = sorted(nums, key = int, reverse=True)
        reverseSortedFilePath = os.path.join(reverseSortedDir, f"{size}_reverse_sorted_{i}.txt")
        writeNumbersToFile(reverseSortedFilePath, reverseSortedNums)

    print(f"\t{size.capitalize()} files done.")

# Helper method that checks if a directory exists and if not, creates the directory
def makeDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Helper method that writes a list of numbers to a file
def writeNumbersToFile(filePath, numbers):
    with open(filePath, 'w') as file:
        file.write(" ".join(numbers))

# Check if script is getting run directly or imported
if __name__ == "__main__":
    startTime = time.perf_counter()
    print("Generating...")
    main()
    print("All files done.")
    endTime = time.perf_counter()
    runTimeS = (endTime - startTime)
    runTimeMin = runTimeS / 60
    runTimeMS = runTimeS * 1000
    print(f"Execution time: {runTimeMS:.2f} ms or {runTimeS:.2f} sec or {runTimeMin:.2f} min")
