with open ("notes.txt", "r") as file:
    content = file.read()
    words = content.split()
    
    count = {}
    for sentence in words:
        if sentence in count:
            count[sentence] += 1
        else:
            count[sentence] = 1
print(count)        