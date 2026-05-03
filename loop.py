# movies=[]
# n=int(input("Enter How many movies"))
# for i in range(1,n+1):
#     a=input("enter the movies:")
#     movies.append(a)
# print(movies)

# list1=[1,2,1]
# copy_list=list1.copy()
# copy_list.reverse()
# if(copy_list==list1):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


dict={}
n=int(input("enter the number of students:"))
for i in range(n):
    name=input("Enter the name of student")
    marks=int(input("enter the marks scored:"))
    dict[name]=marks
print(dict)
total=sum(dict.values())
avg=total/n

highest=max(dict.values())
topper=""
for name,marks in dict.items():
    if marks==highest:
        topper=name

count=0
for marks in dict.values():
    if(marks>40):
        count+=1

print(avg)
print(topper)
print(count)