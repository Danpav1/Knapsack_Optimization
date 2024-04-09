# @author Daniel Pavenko
# @date 04/09/24
# Programming assignment 2 for Design and Analysis of Algorithms. This program handles the knapsack generation

import os
import time
import statistics

# Main method
def main():
    sizes = ["small", "medium", "large"]
    for size in sizes:
        processKnapsacks(size)

# Function to process knapsack files
def processKnapsacks(size):
    print(f"Finding knapsack max val for size: {size}")
    readDir = "dataset"
    writeDir = "results"
    resultFilePath = os.path.join(writeDir, f"{size}_results.txt")

    os.makedirs(writeDir, exist_ok=True)
    resultContent = []

    runtimes_top_down = []
    runtimes_bottom_up = []

    for i in range(1, 31):
        fileName = f"{size}_knapsack_{i}.txt"
        readFilePath = os.path.join(readDir, size, fileName)
        with open(readFilePath, 'r') as file:
            lines = file.readlines()
            W = int(lines[0])
            w = []
            v = []
            for line in lines[1:]:
                weight, value = map(int, line.split())
                w.append(weight)
                v.append(value)

        # Top-Down dynamic programming algo.
        top_down = [[-1 for _ in range(W+1)] for _ in range(len(w)+1)]
        startTime = time.perf_counter()
        maxValuetop_down = knapsack_top_down(w, v, W, len(w), top_down)
        endTime = time.perf_counter()
        runTimetop_downMS = (endTime - startTime) * 1000
        runtimes_top_down.append(runTimetop_downMS)

        # Bottom-Up dynamic programming algo.
        startTime = time.perf_counter()
        maxValuebottom_up = knapsack_bottom_up(w, v, W, len(w))
        endTime = time.perf_counter()
        runTimebottom_upMS = (endTime - startTime) * 1000
        runtimes_bottom_up.append(runTimebottom_upMS)

        resultContent.append(f"Knapsack {i} - Top-down: {maxValuetop_down} - {runTimetop_downMS:.4f} ms\n")
        resultContent.append(f"Knapsack {i} - Bottom-up: {maxValuebottom_up} - {runTimebottom_upMS:.4f} ms\n")
        resultContent.append("\n")

    mean_top_down = statistics.mean(runtimes_top_down)
    sd_top_down = statistics.stdev(runtimes_top_down)
    mean_bottom_up = statistics.mean(runtimes_bottom_up)
    sd_bottom_up = statistics.stdev(runtimes_bottom_up)

    resultContent.append(f"Top-Down Mean Runtime: {mean_top_down:.4f} ms, SD: {sd_top_down:.4f}\n")
    resultContent.append(f"Bottom-Up Mean Runtime: {mean_bottom_up:.4f} ms, SD: {sd_bottom_up:.4f}\n")

    with open(resultFilePath, 'w') as file:
        file.writelines(resultContent)
    print(f"Finished finding knapsack max val for size: {size}")

# Top-Down dynamic programming approach
def knapsack_top_down(w, v, W, n, top_down):
    if n == 0 or W == 0:
        return 0
    if top_down[n][W] != -1:
        return top_down[n][W]
    if w[n-1] > W:
        top_down[n][W] = knapsack_top_down(w, v, W, n-1, top_down)
    else:
        top_down[n][W] = max(v[n-1] + knapsack_top_down(w, v, W-w[n-1], n-1, top_down), knapsack_top_down(w, v, W, n-1, top_down))
    return top_down[n][W]

# Bottom-Up dynamic programming approach
def knapsack_bottom_up(w, v, W, n):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if w[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

# Check if being run directly or imported
if __name__ == "__main__":
    startTime = time.perf_counter()
    main()
    endTime = time.perf_counter()
    runTimeS = (endTime - startTime)
    runTimeMin = runTimeS / 60
    runTimeMS = runTimeS * 1000
    print(f"Total execution time: {runTimeMS:.2f} ms or {runTimeS:.2f} sec or {runTimeMin:.2f} min")