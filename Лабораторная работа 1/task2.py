# TODO Найдите количество книг, которое можно разместить на дискете
bytes_on_disk = 1.44 * 1024 * 1024
simv_on_page = 25 * 50
simv_in_book = simv_on_page * 100 * 4
books_on_disk = bytes_on_disk / simv_in_book
print("Количество книг, помещающихся на дискету:", round(books_on_disk))
