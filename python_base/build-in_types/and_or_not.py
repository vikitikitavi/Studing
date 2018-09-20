""" and, or, not operators"""

to_str = "expr: {oper1} {operator} {oper2}\nresult: {res}\nnote: {note}"


"""1. or is a short-circuit operator,
so it only evaluates the second argument if the first one is false. """

# should raise the TypeError exception when the second operand is processed.
print(to_str.format(
    oper1=1,
    operator="or",
    oper2="abs(\"skdjskd\")",
    res=eval("1 or abs(\"skdjskd\")"),
    note="raise the TypeError exception when the second operand is processed."
))

""" 2. and is a short-circuit operator,
    so it only evaluates the second argument if the first one is true."""

# should raise the TypeError exception when the second operand is processed.
print(to_str.format(
    oper1=0,
    operator="and",
    oper2="abs(\"skdjskd\")",
    res=eval("0 and abs(\"skdjskd\")"),
    note="raise the TypeError exception when the second operand is processed."
))
