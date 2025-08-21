N = int(input())
paper_num = []
for _ in range(N):
    paper = input()
    # 마지막 원소까지 검사하기 위해 임의의 문자 "x"를 넣었음
    paper += "x"
    word = ""
    for i in range(len(paper)):
        if paper[i].isdigit():
            word += paper[i]
        else:
            if i > 0 and paper[i-1].isdigit():
                paper_num.append(int(word))
                word = ""
paper_num.sort()
for num in paper_num:
    print(num)