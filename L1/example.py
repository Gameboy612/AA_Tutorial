import random

input_dict = {}

if random.randint(0,1):
    input_dict = {
        "success": True,
        "data": "Hi"
    }
else:
    input_dict = {
        "success": False
    }



if "data" in input_dict:
    print(input_dict["data"])
else:
    print("Error")