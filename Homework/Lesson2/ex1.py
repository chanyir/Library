# ex1
# def my_len(str="hello"):
#     return len(str)
# def total(arr):
#     sum=0
#     for i in arr:
#         sum+=my_len(i)
#     return sum
# print(total(["chany","pniny","esty"]))
# -------------------------
# ex2
# from functools import reduce


# def mul(arr):
#    listbet=list(filter(lambda x:x>5 and x<10 , arr ))
#    lst=reduce(lambda x,y:x*y,listbet)
#    return lst

# print(mul([1,5,7,9,12]))
# 

# from functools import reduce


# names=["Yoav", "Ron","Aviva","Ronen","Dan","Galit"]

# bigger=list(filter(lambda x:len(x)>4,names))
# lenght=list(map(lambda x:len(x),bigger))
# total=reduce(lambda x,y:x+y,lenght)
# print(total)

# -----------------------
# ex4
# from functools import reduce


# numbers=[6,2,8,12,4]

# # min_num=reduce(lambda x,y:min(x,y),numbers)
# min_num=reduce(lambda x,y: x if x<y else y, numbers)
# print(min_num)



# def a(f):
#     def ineer_f(str1):
#         f()
#         print("pniny")
#     return ineer_f
# @a
# def b(name):
#     print("chany")

# b("avi")

# ex5
# def check(f):
#     def inner_f(n1,n2):
#         if n2==0:
#             print("Do not divide by zero")
#         else:
#             f(n1,n2)
#     return inner_f

# @check
# def divide(n1,n2):
#     print(f"{n1} / {n2} = {n1/n2}")

# divide(2,0)