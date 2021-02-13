arr = []
strArr = []

y = open('input.txt','r');

for line in y:
    ### removes '\n'
    ### line = "1;2;3;4;5"
    templine = line.strip().split(';')
    ### templine = ['1','2','3','4','5']
    strArr.append(templine);
    ##  strArr = [['1','2','3','4','5'],...]
    tempArr = []
    for i in templine:
        temp = int(i)
        tempArr.append(temp);

    ### tempArr = [1,2,3,4,5]
    arr.append(tempArr)


f = open('output.txt','w')


for x in range(len(arr)):
    total = 0;
    for n in arr[x]:
        total += n;
    value = ';'.join(strArr[x][0:5])
    f.write(value + "=" + str(total) + "\n")


f.close()
        
