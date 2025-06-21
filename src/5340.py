answer = [0] * 6

for i in range(6):
    message = input().strip(" ")
    answer[i] = len(message)

print(f"Latitude {answer[0]}:{answer[1]}:{answer[2]}")
print(f"Longitude {answer[3]}:{answer[4]}:{answer[5]}")