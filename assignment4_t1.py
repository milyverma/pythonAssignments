try:
    file1 = open('sample.txt','r')
    i = 1
    print('Reading file content:')
    while True:
        read_line = file1.readline()
        if not read_line:
            break
        else:
            print(f'Line {i}: '+read_line)
            i+=1
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
