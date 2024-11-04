# def is_palindrome(s):
#     return s == s[::-1]
#
# print(is_palindrome("radar"))  # True
# print(is_palindrome("hello"))   # False
#
#
#
# def reverse_string(s):
#     return s[::-1]
#
# print(reverse_string("Hello"))  # "olleH"
#
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# print(factorial(5))  # 120
#
#
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
# fibonacci(10)
#
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# print(is_prime(11))  # True
# print(is_prime(4))   # False
#
# def check_even_odd(number):
#     if number % 2 == 0:
#         print(f"{number} is even.")
#     else:
#         print(f"{number} is odd.")
#
# check_even_odd(7)
#
#
# def pyramid(n):
#     for i in range(n):
#         print(' ' * (n - i - 1) + '*' * (2 * i + 1))
#
# pyramid(5)
#
#
# # Step 1: Define the functions
# def A(x, y):
#     return x + y  # Addition function
#
#
# def B(x, y):
#     return x - y  # Subtraction function
#
#
# # Step 2: Call the functions using variable C
# def C(operation, x, y):
#     if operation == 'A':
#         return A(x, y)  # Call addition
#     elif operation == 'B':
#         return B(x, y)  # Call subtraction
#     else:
#         raise ValueError("Invalid operation")


# # Step 1: Define the functions
# def A(x, y):
#     return x + y  # Addition function
#
#
# def B(x, y):
#     return x - y  # Subtraction function
#
#
# # Step 2: Call the functions using variable C
# def C(operation, x, y):
#     if operation == 'A':
#         return A(x, y)  # Call addition
#     elif operation == 'B':
#         return B(x, y)  # Call subtraction
#     else:
#         raise ValueError("Invalid operation")
#
#
# # Step 3: Test the functions
# def test_operations():
#     # Test addition
#     assert C('A', 3, 2) == 5, "Test failed: 3 + 2 should be 5"
#     assert C('A', -1, 1) == 0, "Test failed: -1 + 1 should be 0"
#
#     # Test subtraction
#     assert C('B', 3, 2) == 1, "Test failed: 3 - 2 should be 1"
#     assert C('B', 2, 3) == -1, "Test failed: 2 - 3 should be -1"
#
#     print("All tests passed!")
#
#
# # Run the tests
# test_operations()
#
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b
#
# def combine_operations(a, b):
#     result_add = add(a, b)
#     result_multiply = multiply(a, b)
#     return result_add, result_multiply
#
# # Test Cases
# def run_tests():
#     # Test Case 1: Addition (Passed)
#     result = add(3, 5)
#     print(f"add(3, 5) = {result}, Expected: 8, Test Passed: {result == 8}")
#
#     # Test Case 2: Addition (Failed)
#     result = add(2, 2)
#     print(f"add(2, 2) = {result}, Expected: 5, Test Passed: {result == 5}")
#
#     # Test Case 3: Multiplication (Passed)
#     result = multiply(3, 5)
#     print(f"multiply(3, 5) = {result}, Expected: 15, Test Passed: {result == 15}")
#
#     # Test Case 4: Multiplication (Failed)
#     result = multiply(2, 3)
#     print(f"multiply(2, 3) = {result}, Expected: 7, Test Passed: {result == 7}")
#
#     # Test Case 5: Combine Operations (Passed)
#     result_add, result_multiply = combine_operations(3, 5)
#     print(f"combine_operations(3, 5) = ({result_add}, {result_multiply}), Expected: (8, 15), Test Passed: {result_add == 8 and result_multiply == 15}")
#
#     # Test Case 6: Combine Operations (Failed)
#     result_add, result_multiply = combine_operations(2, 3)
#     print(f"combine_operations(2, 3) = ({result_add}, {result_multiply}), Expected: (5, 8), Test Passed: {result_add == 5 and result_multiply == 8}")
#
# # Run the tests
# run_tests()
# Step 1: Define the functions
def A(x, y):
    return x + y  # Addition function


def B(x, y):
    return x - y  # Subtraction function


# Step 2: Call the functions using variable C
def C(operation, x, y):
    if operation == 'A':
        return A(x, y)  # Call addition
    elif operation == 'B':
        return B(x, y)  # Call subtraction
    else:
        raise ValueError("Invalid operation")


# Step 3: Test the functions
def test_operations():
    # Test addition
    try:
        assert C('A', 3, 2) == 5, "Test failed: 3 + 2 should be 5"
        print("Test passed: 3 + 2 == 5")
    except AssertionError as e:
        print(e)

    try:
        assert C('A', -1, 1) == 0, "Test failed: -1 + 1 should be 0"
        print("Test passed: -1 + 1 == 0")
    except AssertionError as e:
        print(e)

    # Test subtraction
    try:
        assert C('B', 3, 2) == 1, "Test failed: 3 - 2 should be 1"
        print("Test passed: 3 - 2 == 1")
    except AssertionError as e:
        print(e)

    try:
        assert C('B', 2, 3) == -1, "Test failed: 2 - 3 should be -1"
        print("Test passed: 2 - 3 == -1")
    except AssertionError as e:
        print(e)

    # Intentionally failing test
    try:
        assert C('A', 2, 2) == 5, "Test failed: 2 + 2 should be 4"  # This will fail
        print("Test passed: 2 + 2 == 5")
    except AssertionError as e:
        print(e)

    # Another intentionally failing test
    try:
        assert C('B', 5, 3) == 3, "Test failed: 5 - 3 should be 2"  # This will also fail
        print("Test passed: 5 - 3 == 3")
    except AssertionError as e:
        print(e)

    print("Testing complete!")


# Run the tests
test_operations()
