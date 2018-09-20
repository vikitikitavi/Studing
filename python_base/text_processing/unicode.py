""" Working with unicode characters """


import unicodedata


c_cedilla = unicodedata.lookup("LATIN CAPITAL LETTER C WITH CEDILLA")
c_compose_cedilla = unicodedata.normalize("NFD", c_cedilla)

print("всмa" == "всма")

print_mess = "C cedilla: {} and C combining cedilla: {} are same?\n{}\n" \
             "Their normalistion are same ?\n{}"

normalized_equality = unicodedata.normalize(
    "NFKD", "a") == unicodedata.normalize("NFKD", "а")

print(print_mess.format(
    c_cedilla,
    c_compose_cedilla,
    c_cedilla == c_compose_cedilla,
    normalized_equality
    )
)
