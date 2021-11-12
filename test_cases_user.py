from classes.User import User
from classes.Test_user import Test_user

object_user = User(1,"Luis Guerra", "luis@git.com", "3312724816")
#print(object_user.execution())
object_test_user = Test_user(1, object_user.get_id(), 1)
print(object_test_user.test_id())
