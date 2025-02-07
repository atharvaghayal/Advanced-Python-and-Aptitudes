#find the next larger element in list using loop in pyhton
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
next_larger = []
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[j] > numbers[i]:
            next_larger.append(numbers[j])
            break;           
    
next_larger.append(-1)
print(next_larger)