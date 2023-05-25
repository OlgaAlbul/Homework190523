def print_operation_table(operation, num_rows=6, num_columns=6):
    r_num = num_rows
    c_num = num_columns
    list_rows = [x for x in range(1,r_num+1)]
    list_columns =[x for x in range(1, c_num+1)]
    for i in range(0,r_num):
        if i==0:
            for x in list_columns:
                print("{:6d}".format(x), end='')
        else: 
            print("{:6d}".format(list_rows[i]), ' ', end='') 
            for j in range(1,c_num): 
                if type(calk_1(list_rows[i], list_columns[j])) != int:
                    print("{:5.1f}".format(calk_1(list_columns[j],list_rows[i])), end='')   
                else:        
                    print("{:6d}".format(calk_1(list_columns[j],list_rows[i])), end='')          

        print()
        
calk_1 = lambda x,y: x*y

print_operation_table(calk_1, 6, 6)