# # Login test data --BEFORE
#
# USERNAME = "standard_user"
# PASSWORD = "secret_sauce"

#AFTER using parametrize
LOGIN_DATA = [
    ("standard_user", "secret_sauce","success"),
    ("standard_user", "wrong_password","failure"),
    ("wrong_user", "secret_sauce","failure")]   #Each test data row now contains username + password + expected result.