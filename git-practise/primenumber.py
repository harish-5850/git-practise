def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test the function
if __name__ == "__main__":
    try:
        user_input = input("Enter a number: ")
        num = int(user_input)

        # 1. Check if Prime
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")

        # 2. Check if Odd or Even
        # If the remainder when divided by 2 is 0, it's even.
        if num % 2 == 0:
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number")
            
    except ValueError:
        print("That's not a valid number! Please enter an integer (whole number).")