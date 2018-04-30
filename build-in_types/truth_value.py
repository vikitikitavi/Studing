to_str = "expr: {oper1} {operator} {oper2}\nresult: {res}"


test = (0, None, False, 1, True)

""" The result of equality will be the second operand
    if operands are different"""
for item in test:
    for other_item in test:
        for result in test:
            if item == other_item is result:
                print(to_str.format(
                    oper1=item,
                    operator="==",
                    oper2=other_item,
                    res=result
                ))
