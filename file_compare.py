import difflib

def compare(f1, f2):
    with open(f1) as file_1:
        file_1_text = file_1.readlines()
    
    with open(f2) as file_2:
        file_2_text = file_2.readlines()
    
    # Find and print the diff:
    for line in difflib.unified_diff(
            file_1_text, file_2_text, fromfile=f1, 
            tofile=f2, lineterm=''):
        print(line)


# compare('sample_test_set_1/sample_ts1_output.txt','sample_test_set_1/sample_ts1_input.txt.out')

# compare('test_set_1/ts1_output.txt','test_set_1/ts1_input.txt.out')

# compare('test_set_2/ts2_output.txt','test_set_2/ts2_input.txt.out')
compare('./file2.txt', './file1.txt')