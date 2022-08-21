import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","-","_"]
out_file = open("outputFile.txt","w")

print(f"Starting brute force on {len(alphabet)} characters")
startTime = time.time()
for let1 in range(0,len(alphabet)):
    out_file.write(alphabet[let1] + "\n")

oneCharacterEnd = time.time()

twoCharacterStart = time.time()
for let1 in range(0,len(alphabet)):
    let1 = alphabet[let1]
    for let2 in range(0,len(alphabet)):
        let2 = alphabet[let2]
        word = let1 + let2
        out_file.write(word + '\n')

twoCharacterEnd = time.time()

threeCharacterStart = time.time()
for let1 in range(0,len(alphabet)):
    let1 = alphabet[let1]
    for let2 in range(0,len(alphabet)):
        let2 = alphabet[let2]
        for let3 in range(0,len(alphabet)):
            let3 = alphabet[let3]
            word = let1 + let2 + let3
            out_file.write(word + '\n')

threeCharacterEnd = time.time()

fourCharacterStart = time.time()
for let1 in range(0,len(alphabet)):
    let1 = alphabet[let1]
    for let2 in range(0,len(alphabet)):
        let2 = alphabet[let2]
        for let3 in range(0,len(alphabet)):
            let3 = alphabet[let3]
            for let4 in range(0,len(alphabet)):
                let4 = alphabet[let4]
                word = let1 + let2 + let3 + let4 
                out_file.write(word + '\n')

fourCharacterEnd = time.time()

fiveCharacterStart = time.time()
for let1 in range(0,len(alphabet)):
    let1 = alphabet[let1]
    for let2 in range(0,len(alphabet)):
        let2 = alphabet[let2]
        for let3 in range(0,len(alphabet)):
            let3 = alphabet[let3]
            for let4 in range(0,len(alphabet)):
                let4 = alphabet[let4]
                for let5 in range(0,len(alphabet)):
                    let5 = alphabet[let5]
                    word = let1 + let2 + let3 + let4 + let5
                    out_file.write(word + '\n')

fiveCharacterEnd = time.time()

out_file.close()

print(f"Execution to complete all 1 characters: {oneCharacterEnd - startTime} seconds")
print(f"Execution to complete all 2 characters: {twoCharacterEnd - twoCharacterStart} seconds")
print(f"Execution to complete all 3 characters: {threeCharacterEnd - threeCharacterStart} seconds")
print(f"Execution to complete all 4 characters: {fourCharacterEnd - fourCharacterStart} seconds")
print(f"Execution to complete all 5 characters: {fiveCharacterEnd - fiveCharacterStart} seconds")
print(f"Total time to brute force everything: {fiveCharacterEnd - startTime} seconds")