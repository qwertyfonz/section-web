def filter(ls, f):
    new_ls = []
    for elt in ls:
        if f(elt):
            new_ls.append(elt)
    return new_ls


if __name__ == "__main__":
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # Filtering some lists
    evens = filter(ls, lambda x: x % 2 == 0)
    odds = filter(ls, lambda x: x % 2 != 0)
    large = filter(ls, lambda x: x > 5)

    ls2 = ["apple", "hello", "baby"]

    def has_a(st):
        return "a" in st

    print(f"Words with A: {filter(ls2, has_a)}")

    print(f"Evens: {evens}")
    print(f"Odds: {odds}")
    print(f"Greater than 5: {large}")



