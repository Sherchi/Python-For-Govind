totalMark = 0
amount = 0
avg = 0

score = input();

while (score != "stop"):
    amount += 1;
    totalMark += int(score)
    avg = totalMark/amount
    print(avg)
    score = input()

    
