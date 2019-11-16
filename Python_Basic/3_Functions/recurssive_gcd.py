def find_gcd(a, b):
    """
    (int, int) --> int

    A function that accepts two numbers a and b and returns the gcd of them

    """

    gcd = min(a, b)

    # Keep looping until gcd divides both a & b evenly
    while a % gcd != 0 or b % gcd != 0:
        gcd -= 1

    return gcd


print(find_gcd(9,6))
