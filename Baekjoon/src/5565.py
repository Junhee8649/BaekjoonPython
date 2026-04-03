book_sum = int(input())
books = []
for _ in range(9):
    book = int(input())
    books.append(book)
print(book_sum - sum(books))