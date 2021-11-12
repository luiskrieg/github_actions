from classes.Addition import Addition
from classes.Test_addition import Test_addition

object_addition = Addition(1,1)
#print(object_addition.execution())
object_test_addition = Test_addition(1, object_addition.execution(), 1)
print(object_test_addition.execution())

object_addition = Addition(1,1)
#print(object_addition.execution())
object_test_addition = Test_addition(2, object_addition.execution(), 2)
print(object_test_addition.execution())

object_addition = Addition(3,3)
object_test_addition = Test_addition(3, object_addition.execution(), 6)
print(object_test_addition.execution())

object_addition = Addition(1.5,1)
print(object_addition.execution())
object_test_addition = Test_addition(4, object_addition.execution(), 2.5)
print(object_test_addition.execution())

