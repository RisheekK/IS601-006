a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result

    for i in arr:
        if type(i) == int:                              #to check if the value is integer
            print(abs(i), end=' ')
        elif type(i) == float:                          #to check if the value is float
            print(abs(i), end=' ')
        elif type(i) == str:                            #to check if the value is String
            i = f"{abs(int(i))}"                        #to make sure the ouput is also string
            print((i), end=' ')
    
    print(type(i))                                      #to mention the data type of the output




print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)