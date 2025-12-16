n, X = [int(i) for i in input().split()]
boxes = [int(i) for i in input().split()]

remainder_count = dict()
current_sum = 0
count = 0

remainder_count[0] = 1

for num in boxes:
    current_sum = (current_sum + num) % X
    
    if current_sum in remainder_count:
        count += remainder_count[current_sum]
    
    remainder_count[current_sum] = remainder_count.get(current_sum, 0) + 1


print(count)
