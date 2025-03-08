def is_prime(n: int) -> bool:
    if n < 2:
        raise ValueError("So be hon 2 khong phai so nguyen to")

    if (n % 2 == 0 and n % 3 == 0 and n % 5 == 0):
        raise ValueError("Khong phai so nguyen to")
    return True