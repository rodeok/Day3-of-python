# # CLASSWORK
# # CHECK WHETHER 10 IS GREATER OR LESS THAN 1
# # USING CONDITION

# z = input("subject name: ")
# m = input("book name:  ")

# # z = int(z)
# # m = int(m)

# if z > m:
#     print ("z is greater than m!")
#     if z >= 10:
#         print("z is negative1")
#     else:
#         print("z is positive!")
# if z < m:
#     print("z is less than m!")
#     if z < 10:
#         print("z is less than 10")
# else:
#     print("z is equal to m")

# from PIL import Image,ImageFilter
# befo = Image.open("shark.png")
# aft = befo.filter(ImageFilter.BoxBlur(110))
# aft.save("out.png")

# from PIL import Image
# with Image.open("shark.png") as im:
#     im.rotate(45).show()

import json

# some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["city"])



# some JSON:
# s =  '{"name": "age":30, "city":"new york"}'

# # parse s:
# s = json.loads(s)

# # the result is a python dictionary:
# print(s["name")




myanimals = ("dog" "cat", "goat")
myanimals = tuple(myanimals)

print(next(myanimals))
print(next(myanimals))
print(next(myanimals))