# Progamming assignment 2:

## Introduction

This project is the second programming assignment for the Design and Analysis of Algorithms course. In this project we generate small, medium and large "knapsacks"
and optimize them in a way in which we get the most amount of value in a knapsack while still being within the knapsacks weight constraints.

## Usage

Step by step process on how to run this program.

###### Change directory to the desired repository location:
	cd desired-dir-here

###### Clone the repository:
	git clone https://github.com/Danpav1/Knapsack_Optimization.git

 ###### Change directory to be inside the newly cloned repository:
	cd project-dir-here

###### Create virtual environment and activate it:
	# For macOS and Linux
 	python3 -m venv .venv
	source .venv/bin/activate
###### 
	# For Windows
	python -m venv .venv
	.\.venv\Scripts\activate

###### Generate the dataset:
	python3 ./knapsackGenerator.py

This will create and fill the dataset folder heirarchy with the knapsacks.

The dataset folder can be found at: Knapsack_Optimization/dataset. The datasets are sorted in size (small, medium, large).

NOTE: Everytime you generate a new dataset, the old dataset is overwritten.

###### Then optimize the files and find the max value that can be fit in each knapsack:
	python3 ./optimizeKnapsacks.py

This will create and fill the results folder heirarchy with the results of the knapsack optimization.

The results folder can be found at: Knapsack_Optimization/results. The results are sorted in dataset input size (small, medium, large).

All of the run time data for each test as well as the overall run time mean and standard deviation is stored at the end of any given results file.

NOTE: Everytime you generate a new dataset and run optimizeKnapsacks, the old results are overwritten.

