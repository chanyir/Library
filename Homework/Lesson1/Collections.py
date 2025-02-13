
# ex 1
# sum=0
# array=[17,1,12,54,23,9,21]
# for i in array:
#     if i>3 and i<20:
#         sum+=i
# print(sum)

# ex2
# data=[
#       {"id":123, "grates":[88,90,95,98,96,97] },
#       {"id":456, "grates":[100,90,95,98,96,97]},
#       {"id":789,"grates":[88,90,95,99,96,70] }
#     ]
# myMax=0
# idd=int(input("Enter your id"))
# for i in data:
#     if idd==i["id"]:
#       myMax=max(i["grates"])
# print(f"Your high score is:{myMax}")

# ex3
# import statistics
# arr=[4, "Hello" , [ True, "Avi" , [5,1,9,3] ] ]
# arr2=arr[len(arr)-1]
# arr3=arr2[len(arr2)-1]
# sum=0
# average = statistics.mean(arr3)
# print(average)

# ex4
# import statistics
# arr={
# "nums" : [77,95] ,
# "Student" : {
#       "Name" : "Avi",
#       "ID" : 111111,
#       "Grades" : {

# "score" : [89,96,100]

# }
# }
# }

# avgn = statistics.mean(arr["nums"])
# avgs = statistics.mean(arr["Student"]["Grades"]["score"])

# print(max(avgn,avgs))