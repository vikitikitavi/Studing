"""Text prettifying  with textwrap"""

import textwrap


text = """\
There is a long text\
\twith a lot of tabs\t,\
single\tspaces\n and very\
long lines that are bigger than 50 characters.\n\
The purpose of this dummy long text is to demonstrate\
the POWER in prettifying with wonderfull textwrap module.\
"""

print("Here are how the text looks like without textwrap: \n\n{}\n".format(
    text
    ))
text = textwrap.dedent(text)
lines = textwrap.wrap(
    text,
    width=50,
    expand_tabs=False,
    replace_whitespace=True,
    drop_whitespace=True,
    subsequent_indent="   ",
    initial_indent='',
    max_lines=4
    )
print("Here are how the text looks like with textwrap: \n\n{}\n".format(
    "\n".join(lines)
))
