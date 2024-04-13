user_input = input("Enter a sentence or para :").split()
count_words = 0
for word in user_input:
    count_words = count_words + 1
print(f"words count : {count_words}.")
