def Add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace("\n", ",")

    parts = numbers.split(",")
    for part in parts:
        if part.strip() == "":
            raise ValueError("ValError")
    return sum(int(p) for p in parts)
