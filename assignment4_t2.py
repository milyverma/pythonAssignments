user_string = input('Enter text to write to the file:')

file1 = open('output.txt','w')
write_txt = file1.write(user_string)
print('Data successfully written to output.txt.')
file1.close()

additional_txt = input('Enter additional text to append:')
file1 = open('output.txt','a')
append_txt = file1.write('\n'+additional_txt)
print('Data successfully appended.')
file1.close()

file1 = open('output.txt','r')
read_txt = file1.read()
print('Final content of output.txt:')
print(read_txt)








