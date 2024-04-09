# @author Daniel Pavenko
# @date 04/09/24
# Programming assignment 2 for Design and Analysis of Algorithms. This program handles the knapsack creation

import os
import random
import time

# Main method
def main():
    runGenerator()

# Starts the process(es) and runs generateKnapsacks with appropriate inputs
def runGenerator():
    # Inputs used for generateKnapsacks (size, max_weight_range, num_items_range, item_weight_range, item_value_range)
    sizes = [
        ("small", (2, 10), (3, 8), (1, 7), (1, 5)),
        ("medium", (11, 30), (9, 15), (1, 20), (1, 10)),
        ("large", (31, 60), (16, 35), (1, 25), (1, 20))
    ]

    # Uses the tuples in sizes as input for generateFiles
    for size, weight_range, items_range, w_range, v_range in sizes:
        generateKnapsacks(size, weight_range, items_range, w_range, v_range)

# Generates knapsack files based on the parameters given to it
def generateKnapsacks(size, weight_range, items_range, w_range, v_range):
    baseDir = f"dataset/{size}"
    makeDirectory(baseDir)

    # Make the 30 knapsacks
    for i in range(1, 31):
        max_weight = random.randint(*weight_range)
        num_items = random.randint(*items_range)
        filePath = os.path.join(baseDir, f"{size}_knapsack_{i}.txt")

        # Ensure at least one item can fit into the knapsack
        guaranteed_item_weight = random.randint(1, max_weight)
        guaranteed_item_value = random.randint(*v_range)

        items = [(guaranteed_item_weight, guaranteed_item_value)]
        for _ in range(num_items - 1):
            w = random.randint(*w_range)
            v = random.randint(*v_range)
            items.append((w, v))

        # Write the knapsack data
        with open(filePath, 'w') as file:
            file.write(f"{max_weight}\n")
            for w, v in items:
                file.write(f"{w} {v}\n")

    print(f"\t{size.capitalize()} knapsack files done.")

# Helper method that checks if a directory exists and if not, creates the directory
def makeDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Check if script is getting run directly or imported
if __name__ == "__main__":
    startTime = time.perf_counter()
    print("Generating knapsacks...")
    main()
    print("All knapsacks done.")
    endTime = time.perf_counter()
    runTimeS = (endTime - startTime)
    runTimeMin = runTimeS / 60
    runTimeMS = runTimeS * 1000
    print(f"Execution time: {runTimeMS:.2f} ms or {runTimeS:.2f} sec or {runTimeMin:.2f} min")
