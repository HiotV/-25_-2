# TODO Найдите количество книг, которое можно разместить на дискете
disc = 1.44  # Mbyte
pages = 100
str_ = 50
symbols = 25
symbol_weight = 4  # byte
book_weight = pages * str_ * symbols * symbol_weight / (1024 ** 2)
book_in_disk = int(disc / book_weight)
print("Количество книг, помещающихся на дискету:", book_in_disk)
