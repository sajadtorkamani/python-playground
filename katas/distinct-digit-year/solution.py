def distinct_digit_year(year):
    while True:
        year += 1

        num_unique_digits = len(set(str(year)))
        if num_unique_digits == 4:
            return year
