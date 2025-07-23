word = input()
max_len = len(word)
word_list = []

for i in range(max_len-2):
    for j in range(i+1,max_len-1):
        for k in range(j+1,max_len):
            word_a = word[:j][::-1]
            word_b = word[j:k][::-1]
            word_c = word[k:][::-1]
            word_list.append(word_a + word_b + word_c)
        
print(min(word_list))