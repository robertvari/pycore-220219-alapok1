username = "rober"
password = "testpas12"

#           True                   True
if username == "robert" and password == "testpas123":
    print("Wellcome robert you are logged in")
else:
    print("username or password was not correct")

#          True                   False
if username == "robert" or password == "testpas123":
    print("Wellcome robert you are logged in")