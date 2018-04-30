from string import Template

class_template = """
class $class_name:
    def __init__(self, arg):
        self.$name = arg 
"""

class_a = Template(class_template).substitute(
    class_name="Aclass",
    name="my_arg"
)

exec(class_a)
print(Aclass("Petya").my_arg)