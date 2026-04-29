# Using a single 'with' statement to open multiple files safely;
# both files are automatically closed after the block

with (open('file1.txt') as f1,open('file2.txt') as f2):
    data1 = f1.read()
    data2 = f2.read()
    print(data1, data2)
#  Process files