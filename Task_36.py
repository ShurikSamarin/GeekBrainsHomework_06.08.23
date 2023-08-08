def operation_table(operation, num_rows=6, num_columns=6):
    lst = list()
    for i in range (1, num_columns+1):
        for j in range (1, num_rows+1):
            lst.append(eval(operation))
        print(*lst)
        lst = list()
    return
operation_table('i*j')
