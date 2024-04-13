# Read input
n = int(input())
scores = map(int, input().split(","))

# Convert the list into a set to remove duplicates
unique_scores = set(scores)

# Convert the set back to a list and sort it in descending order
sorted_scores = sorted(unique_scores, reverse=True)

# Check if there are at least two scores
if len(sorted_scores) >= 2:
    # Print the runner-up score
    print(sorted_scores[1])
else:
    print("There are not enough unique scores to determine the runner-up.")
