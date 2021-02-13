letters = {}
y = open('input.txt','r');


for x in range(26):
    letters[chr(65 + x)] = 0;
for x in range(26):
    letters[chr(97 + x)] = 0;

for line in y:
    for char in line:
        if char in letters:
            letters[char] += 1

for key in letters:
    print("Letter " + key + " Appears " + str(letters[key]) +  " times")
