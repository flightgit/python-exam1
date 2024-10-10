count_numbers = 0
sum_positive = 0
count_equal_pairs = 0

while True:
    x = int(input("הכנס מספר שלם ראשון:"))
    y = int(input("הכנס מספר שלם שני:"))

    count_numbers += 2

    if x == -y:
        break

    if x > 0:
        sum_positive += x

    if y > 0:
        sum_positive += y

    if x == y:
        count_equal_pairs += 1

print(f"{count_numbers}")
print(f"sum p{sum_positive}")
print(f"equal{count_equal_pairs}")