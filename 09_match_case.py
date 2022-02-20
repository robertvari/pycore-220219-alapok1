status = 204

# if status == 200:
#     print("OK")
# elif status == 204:
#     print("No Content")
# elif status == 404:
#     print("Bad Request")
# elif status == 500:
#     print("Internal Server Error")
# else:
#     print("Something went wrong... :(")

match status:
    case 200:
        print("OK")
    case 204:
        print("No Content")
    case 404:
        print("Bad Request")
    case 500:
        print("Internal Server Error")
    case _:
        print("Something went wrong... :(")
