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