def addition(number_one, number_two):
    result = number_one + number_two
    return result

def test_addition(addition_result, test_result):
    if addition_result is test_result:
        return "Test case approved"
    else:
        return "Test case NOT approved"

print("Test case 1: ")
print(test_addition(addition(1,1), 2))
print("Test case 2: ")
print(test_addition(addition(1,1), 3))