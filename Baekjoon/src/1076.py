resistance = ["black", "brown", "red", "orange","yellow", "green", "blue", "violet", "grey", "white"]

first_color = input()
second_color = input()
third_color = input()

first_index = resistance.index(first_color)
second_index = resistance.index(second_color)
third_index = resistance.index(third_color)

print((first_index * 10 + second_index) * pow(10, third_index))