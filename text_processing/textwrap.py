import textwrap


text = " There is a long text \
      \twith a lot of tabs\t,\n \
      not  single    spaces\n and very \
      long lines that are bigger than 50 characters.\n \
      The purpose of this dummy long text is to demonstrate \
      the POWER in prettifying with wonderfull textwrap module. \
      "

print("Here are how the text looks like without textwrap: \n{}".format(
    text
    ))
