# part 1

contains_range("2-4,2-8")
2-4,6-8 > second_bigger, second_bigger > False
3-7,2-8 > lower=first_bigger, higher=second_bigger > True
2-8,3-7 > lower=second_bigger, higher=first_bigger > True
2-4,2-8 > lower = False, higher = second_bigger > True
2-8,2-4 > lower = False, higher = first_bigger > True
2-4,3-4 > lower=second_bigger, higher = False > True

# part 2

2-6,4-8 > second_bigger, second_bigger > True: this does have overlap
if second_bigger for both:
first item second index minus second item first index
if greater than -1, then they do overlap
and the "how much" is the answer to that subtraction (but we don't need to know that)
4-8,2-6
if first_bigger for both:
second item second index minus first item first index
if greater than -1, then they do overlap
