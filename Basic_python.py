##################################
########## Loop questions #######



#########################
## loop saral question ##

#################
### sum print ###

# a=50
# b=0
# while a<60:
#     c=int(input("enter the number:"))
#     b=b+c
#     a+=1
# print(b)


# a=50
# b=0
# while a-60:
#     c=int(input("enter the number:"))
#     b=b+c
#     a+=1
# print(b)


# a=int(input("enter the number: "))
# b=0
# x=0
# while b<a:
#     c=int(input())
#     b+=1
#     x+=c
# print(x)


#######################################
#### sum and average of the element #####

# a=3
# b=1
# c=0
# e=0
# while b<=a:
#     p=int(input())
#     c+=p
#     e=c/a
#     b+=1
# print(c)
# print(e)

#######################
# ### prime number ####

# a=int(input())
# f=0
# b=2
# while b<=a/2:
#     if a%b==0:
#         f=1
#         break
#     b=b+1
# if f==0:
#     print("prime")
# else:
#     print(" not prime number")


# a=int(input(" "))
# b=2
# while b<a:
#     if a%b==0:
#         print("no")
#         break
#     b+=1
# else:
#     print("yes")


# a=20
# while a<=100:
#     print(a)
#     a+=2


# a=7
# while a<100:
#     print(a)
#     a+=7


# a=30
# b=0
# while a<=40:
#     b=a+b
#     a=a+2
# print(b)


# a=12
# b=0
# while a<=420:
#     b=a+b
#     a+=1
# print(b)


# a=30
# b=0
# while a<420:
#     if a%8==0:
#         b=a+b
#         print("a",a)
#     a+=1
# print(b)

#######################
#### average print ####

# a=1
# b=0
# while a<=11:
#     c=int(input())
#     b=b+c
#     d=b/11
#     a+=1
# if d%5==0:
#     print("yes")
# else:
#     print("no")
# print(d)

#################################################
#### odd number pisitive even number negative ####

# a=1
# b=2
# while a<=100:
#     print(a)
#     print(b*(-1))
#     a+=2
#     b+=2

######################
#### gussing game ####

# a=5
# b=1
# c=0
# while b<=3:
#     c=int(input("enter the number: "))
#     b+=1
#     if a==c:
#         print("won")
#         break
#     else:
#         print("try again")
# else:
#     print("you lost the game ")
      

# a=5
# b=1
# c=0
# while b<=3:
#     c=int(input("enter the number: "))
#     b+=1
#     if a==c:
#         print("won")
#         break
#     elif a>c:
#         print("chota hai try again")
#     else:
#         print("bada hai try again")
# else:
#     print("you lost the game ")


# a=1
# b=0
# while a<=50:
#     a,b=b,a
#     c=a+b
#     print(c)
#     a+=1                                                                                                             


# c=0
# d=1
# while c<3:
#     c=c+1
#     d=d*c
#     print(c,d)
# else:
# #     print(c,d)


# i = 0
# while(i<5):
#     j = 0
#     while(j<5): #loop2
#         if (j > 3): 
#             break 
#         else:
#             print ("*") 
#         j = j + 1    
#     print ('')
#     i = i + 1
 

# x = 0
# while(x<7):
#     if (x == 3 or x==5):
#         x = x + 1
#         continue
#     print(x)
#     x = x + 1 


#####################################################
#### 2 number multiply without use multiply sign ####

# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# c=0
# co=0
# while c<b:
#     co=co+a
#     c+=1
# print(co)


################################
#####   Fibonacci  Series  #####

# a=int(input())
# b=0
# c=1
# d=0
# while d<=a:
#     # print(b)
#     e=b+c
#     b=c
#     c=e
#     d+=1
# print(b)


###################################################
##### star pattern difference difference type #####

# a=int(input())
# b=0
# while b<+a:
#     print("  "*(a-2)+"  *"*(a-b))
#     b+=1

# a=int(input())
# b=0
# while b<+a:
#     print("  "*(a+b)+"  *"*(a-b))
#     b+=1

# a=int(input())
# b=0
# while b<+a:
#     print("   "*(a-b)+"*  "*(a-b))
#     b+=1

# a=int(input( ))
# b=1
# while b<=a:
#     print(" "*(a-b)+"* "*b)
#     b+=1
   
# a=int(input())
# b=1
# while b<+a:
#     print(" "*(a-b)+" *"*a)
#     b+=1

# a=int(input())
# b=0
# while b<+a:
#     print("  "*(a-b)+"  *"*(a-b))
#     b+=1

# a=int(input( ))
# b=1
# while b<=a:
#     print(" "*(a-b)+"* "*b)
#     b+=2


##########################################################
### odd number is positive and even number is negative ###

# a=1
# b=2
# while a<=100:
#     print(a,b*(-1))
#     a+=2
#     b+=2


################################
### this code is hppy number ###

# num=int(input())
# n=num
# sum=0
# while sum!= 1 and sum!=4:
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit**2
#         n=n//10
#     n=sum
# if sum==1:
#     print("h")
# else:
#     print("n")


#####################
##### Factiriol #####

# a=int(input())
# b=1
# for i in range (a):
#     b=b*(i+1)
# print(b)


#########################################
#### This code is  String palindrome ####

# x=input(" ")
# b=""
# for i in x:
#     b=i+b
# if x==b:
#     print("y")
# else:
#     print("n")


##########################    
#### R pattern print  ####

# x=4
# y=1
# while y!=5:
#     if y==1:
#         print("* "*x)
#         print("* "," "*2,"*")
#         print("* "*x)
#     else:
#         print("*"," "*(y-2),"*")
#     y+=1
 

#########################
### table print 2*1=2 ###

# a=int(input())
# for i in range (1,11):
#     print(str(a), "*", str(i), "=", str(i*a))

# a= int(input())
# for i in range (1, a+1):
#     for j in range (1,11):
#         print(i*j)
# print()


#########################################
###### odd and even number ##########
# a=1
# while a<=100:
#     a+=1
#     if a%2==0:
#         print(a,"even")
#         if a==100:
#             a-=99
#     else:
#         print(a,"odd")
#     a+=1


##############################################
#### odd even print (first even then odd) ####

# a=2
# while a<=200:
#     if a<=100:
#         if a%2==0:
#             print(a)
#     else:
#         if a%2!=0:
#             print(a-100)
#     a+=1 


########################################################################
#### first  pehle ke three number even then baad ke three number odd ####

# a=int(input())
# f=a
# v=f
# i=0
# while a>0:
#     a-=1
#     if a%2==0:
#         print(a,end=' ')
#         if f-a==5:
#             break
#         elif f-a==6:
#             break
# print()
# while f>0:
#     f+=1
#     if f%2!=0:
#         print(f,end=' ')
#         if f-v==5:
#             break
#         elif f-v==6:
#             break
# print()


########################################
### without use number print 1 to 10 ###

# a=ord("A")
# b=ord("J")
# c=ord("@")
# x = a-c
# while a <= b:
#     print(a-c)
#     a+=x


##################################
####### integer palindrome #######

# x=int(input())
# s = str(x)
# rs = "".join(list(reversed(s)))
# if rs != s:
#     print (False)
# else:
#     print(True)









######################################
########## List  Questions ###########
######################################

######################################
#### prime , even and odd number #####

# l=int(input("How many input do you need :"))
# x=[]
# y=[]
# z=[]
# b=[]
# for p in range (l):
#     t=int(input("Enter the number :"))
#     x.append(t)
# for i in x:
#     if i > 1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             y.append(i)
# for h in x:
#     if h % 2 ==0:
#         z.append(h)
# for k in x:
#     if k % 2 ==1:
#         b.append(k)
# print("This is prime number", y)
# print("This is even number",z)
# print("This is odd number",b)




#### bubble sort #####


# a = [16, 19, 11, 15, 10, 12, 14]
# for j in range(len(a)):
#     b= False
#     i = 0
#     while i<len(a)-1:
#         if a[i]>a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i] 
#             b= True
#         i = i+1
#     if b == False:
#         break 
# print (a)



##### palindrome using list #####

# a=list(input())
# b=[]
# for i in a[::-1]:
#     b.append(i)
# if a==b:
#     print("yes")
# else:
#     print("no")



### find which numbers are not present in the second array ###

# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7] 
# for i in list2 :
#     for j in list1 :
#         if i == j :
#             list1.remove(j)
# print(list1)    


#### sum of nested list ####

#marks = [ [78, 76, 94, 86, 88], [91, 71, 98, 65, 76],[95, 45, 78, 52, 49] ] 
#b=0
#for i in marks:
#	for j in i:
#		b=j+b
#print(b)


###### sum of the list and average the list ######

# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ] 
# for i in marks:
#     sum=0
#     for j in i:
#         sum=sum+j
#     av=sum/len(i)
#     print(sum)
#     print(round(av,2))




######## sum of odd number and sum of even ########

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# d=0
# e=0
# for i in elements:
#     if i % 2 == 1:
#         d+=i
#     else:
#         e+=i
# print("sum of odd number :",d)
# print("sum of even number :",e)


#### Total sum 30 ####

# number = 30
# a = [10, 11, 12, 13, 14, 17, 18, 19] 
# c=[]
# for i in a:
#     sum = 0
#     for j in a :
#         sum = i +j
#         if number == sum:
#             c.append([i,j])
#             a.remove(i)
#             a.remove(j)
# print(c)



#### find odd even number and sum of odd even number ####
#### and average of odd even number ####

# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
# b=[]
# c=[]
# d=0
# e=0
# for i in elements:
#     if i % 2 == 1 :
#         b.append(i)
#         d+=i        
#     else:
#         c.append(i)
#         e+=i
# print("odd number is :",len(b),b)
# print("even number is :",len(c),c)
# print("sum of odd number :",d)
# print("sum of even number :",e)
# r=d/len(b)
# s=e/len(c)
# print("average of odd number :",round (r,2))
# print("average of even number :",round (s,2))





####sum same indexing ka same indexing ke sath ####

# a=[23,45,67,87,98,90]
# b=[24,45,5,78,12,34]
# c=[]
# for i in a:
#     sum=0
#     for j in b:
#         sum= i+j  
#         b.remove(b[0]) 
#         break
#     c.append(sum)
# print(c)



#### Bubble short ####

# a=[23,45,56,12,21,13,14,54]
# b=[]
# for i in range(len(a)):
#     v=min(a)
#     a.remove(v)
#     b.append(v)
# print(b)



####  Write a Python program to multiplies all the items in a list. ####

# a=int(input())
# c=[]
# b=1
# for i in range (a) :
#     d=int(input())
#     c.append(d)
#     b=b*d
# print(b)


#### Write a Python program to get the largest number from a list. ####

# a=int(input())
# b=[]
# c=0
# for i in range (a):
#     d=int(input())
#     b.append(d)
# print(b) 
# for j in b:
#     if j > c:
#         c=j
# print(c)




#### Write a Python program to get the minium number from a list ####

# a=int(input())
# b=[]
# for i in range(a):
#     d= int(input())
#     b.append(d)
# print(b)
# c=b[0]
# for  j in b:
#     if j < c:
#         c=j
# print(c)



#### Write a Python program to count the number of ####
#### strings where the string length is 2 or more and the ####
#### first and last character are same from a given list of strings. ####

# a=int(input())
# b=[]
# for i in range (a):
#     c=input()
#     b.append(c)
# print(b)
# e=0
# for j in b:
#     if len(b)>2 and j[0]==j[-1]:
#         e+=1
# print(e)


##### remove duplicate items from list #####

# a=int(input())
# b=[]
# for i in range (a):
#     c=input()
#     b.append(c)
# d=[]
# for j in b:
#     if j not in d:
#         d.append(j)
# print(d)


##### print whose element not in the list end of the lenth #####

# a=[1,7,9,12]
# c=[]
# b=0
# while b < a[-1]:
#     if b not in a :
#         c.append(b)
#     b+=1
# print(c)



######## find maximum or second maximum number from list ##########

# a=[34,56738905,2234,3]
# b = a[0]
# c = a[0]
# for j in range (len(a)):
#     if a[j] > b:
#         c = b
#         b = a[j]
#     elif a[j] > c and a[j] < b:
#         c = a[j]
# print("maximum :", b,"\nsecond maximum :",c)




#### implement string ####

# def string(a,b):
#     for i in a:
    #         if b not in a:
    #             print(-1)
    #             break
    #     else:
    #         print(len(b))
    # a=input()
    # b=input()
    # string(a,b)






#### perfect number ####

# a=int(input())
# sum1=0
# c=[]
# for i in range (1,a):
#     if a%i==0:
#         sum1+=i
#         c.append(i)
# print(c)
# if a==sum1:
#     print("perfect number")
# else:
#     print("not perfect")


#### convert binary to decimal ####

# d=int(input())
# a=[]
# for j in range (d):
#     e=int(input())
#     a.append(e)
# c=0
# b=0
# for i in range(-1,-len(a)-1,-1):
#     c=a[i]*2**b+c
#     b+=1
# print(c)


############ find maximum and second maximum in the list #######

# a=[73,432345678905,2234,3,35,5789024,9,9,99999999,234,9]
# b = a[0]
# c = a[0]
# for j in range (len(a)):
#     if a[j] > b:
#         c = b
#         b = a[j]
#     elif a[j] > c and a[j] < b:
#         c = a[j]
# print("maximum :", b,"\nsecond maximum :",c)






#########################################
###### saral dictionary question ########
##############################
#### Dictionary Questions ####
##############################

# dict1={1:10, 2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# dict1.update(dic2)
# dict1.update(dic3)
# print(dict1)

##############################

# a=input("Enter the keys :")
# dict1={"name":"Raju", "marks":56}
# if a in dict1:
#     print("Key already exist in the dictionary :")
# else:
#     print("Key not exist in the dictionary :")

##############################

# my_dict = {
#     'data1':100,
#     'data2': -54,
#     'data3': 247
#     } 
# c=0
# for i in my_dict.values():
#     c+=i
# print(c)

##############################

# Dic= {
#     1: 'NAVGURUKUL',
#     2: 'IN',  
#     3:{    
#             'A' : 'WELCOME',
#             'B' : 'To',
#             'C' : 'DHARAMSALA'
#         }
#     }
# del Dic[3]['A']
# print(Dic)

###############################

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5]
# a={}
# for i in range (len(list1)):
#     a[list1[i]]=list2[i]
# print(a)

###############################

# dic={
#     "ball":"red",
#     "bat":4,
#     "wickets":8,
#     "ball":"green",
#     "bat":3
#     }
# print(dic)

################################

# a=[
#      {"first":"1"}, 
#      {"second": "2"}, 
#      {"third": "1"}, 
#      {"four": "5"}, 
#      {"five":"5"}, 
#      {"six":"9"},
#      {"seven":"7"}
# ]
# b=[]
# for i in a:
#     for j in i.values():
#         if j not in b:
#             b.append(j)
# print(b)

##################################

# a=int(input("Enter the students name and values :"))
# b={}
# for i in range (a):
#     c=input("Enter the name :")
#     d=int(input("Enter the students marks :"))
#     b[c]=(d)
# print(b)

####################################

# a="MISSISSIPPI"
# b={}
# for i in a:
#     d=a.count(i)
#     b[i]=(d)
# print(b)

######################################

# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# b=0
# for i in dict1.values():
#     for j in i:
#         b+=1
# print("Total count = ",b)

######################################

# my_dict = {
#     'a':500, 
#     'b':58, 
#     'c':560,
#     'd':40, 
#     'e':100, 
#     'f':20
#     }
# a=[]
# for i in my_dict.values():
#     a.append(i)
#     a.sort()
# print(a[3:])

########################################

# a=int(input("Enter the number :"))
# b={}
# for i in range (a):
#     c=int(input())
#     b[c]=(c*c)
# print(b)

################################

# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }
# print(details["name"])
# print(details["email"])
# print(details["age"])

#################################

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+i
# print(sum) 

#################################

# c=dict()
# for i in range(1,16):
#     c[i]=i*i
# print(c)


###################################

# my_dict = {
#     'a':50, 
#     'b':58,
#     'c': 56,
#     'd':40,
#     'e':100, 
#     'f':20
#     } 
# b=sorted(my_dict.values())
# s=b[-3:]
# s.reverse() 
# print(s)
# a=[]
# for i in s:
#     for j, k in zip(my_dict.values(),my_dict.keys()):
#         if i == j :
#             a.append(k)                      
# print(a)

##################################

# a={'bijender':45,'deepak':60,"param":20,"anjili":30,"roshini":50}
# d={}
# for i,j in zip(a.values(),a.keys()):
#     d[i]=j
# list1=[]
# for i in d:
#     list1.append(i)
# list1.sort()
# a=[]
# d2={}
# for j in list1:
#     for i,k in zip(d.values(),d.keys()):
#         if j==k:
#             d2[i]=j
# print("Assending order :",d2)
# a={'bijender':45,'deepak':60,"param":20,"anjili":30,"roshini":50}
# d={}
# for i,j in zip(a.values(),a.keys()):
#     d[i]=j
# list1=[]
# for i in d:
#     list1.append(i)
# list1.sort(reverse=True)
# a=[]
# d2={}
# for j in list1:
#     for i,k in zip(d.values(),d.keys()):
#         if j==k:
#             d2[i]=j
# print("Dessending order :",d2)




# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'b': 3, 'a': 2}
# d2 = {}
# list1=[]
# list2=[]
# for key,value in d1.items():
#     print(value)
#     if key not in list1:
#         list1.append(key)
#     if value not in list2:
#         list2.append(value)
# list2.insert(0,1)
# print(list1)
# print(list2)
# for i in range (len(list1)):
#     d2[list1[i]]=list2[i]
# print(d2)


###########################################
#### w3recourse dictionary questions ######
###############################
#### add sum of all values ####

# a=int(input())
# b=0
# c={}
# for i in range (a):
#     e=input()
#     d=int(input())
#     c[e]=d
# for j in c.values():
#     b+=j
# print(b)

#################################
#### multiples of all values ####

# a=int(input())
# b=1
# c={}
# for i in range (a):
#     e=input()
#     d=int(input())
#     c[e]=d
# for j in c.values():
#     b*=j
# print(b)

########################################
#### remove the key from dictionary ####

# a={"tus":56,"dh":67,"k":3}
# print(a)
# a.pop("tus")
# print(a)

#########################################################
#### find minimum and maximum value from dictionary #####

# a={"a":45,"f":34,"e":35,"b":2}
# b=[]
# for i in a.values():
#     b.append(i)
#     b.sort()
# print("minimum value of dictionary : ",b[0])
# print("maximum value of dictionary : ",b[-1])

##############################################################
#### combine two dictionary adding values for common keys.####

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# D3 ={}
# for i,j in zip(d1,d2):
#     if i == j:
#         D3[i] = d1[i]+d2[j]
#     else:
#         D3[i] = d1[i]
#         D3[j] = d2[j]
# print(D3)

##############################################
#### find 3 highest value from dictionary ####

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# b=0
# c=[]
# l = []
# for i in my_dict.values():
#     c.append(i)
# for j in c:
#     l.append(max(c))
#     c.remove(max(c))
# print(l)

###############################################
#### remove the spaces from the dictionary ####

# a= {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# c={}
# for i in a:
#     b=i.replace(' ','')
#     for j in a.values():
#         c[b]=j
# print(c)

##############################
#### find 3 maximum value ####

# a= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# b=0
# c=[]
# l = []
# for i in a.values():
#     c.append(i)
# for j in c:
#     l.append(max(c))
#     c.remove(max(c))
# print(l)

######################################################
#### find the key, value and item in a dictionary.####

# a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# b=0
# print("key","value","count")
# for i,j in zip(a.keys(),a.values()):
#     b+=1
#     print(i,"  ",j,"  ",b)

##################################################################
#### Write a Python program to print a dictionary line by line.####

# a={'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for i in a:
#     print(i)
#     for j in a[i]:
#         print(j,':',a[i][j])

####################################################################
#### count number of items in a dictionary value that is a list.####

# dic =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# c=0
# for i in dic.values():
#     for j in range (len(i)):
#         c+=1
# print(c)

########################################################
##### replace dictionary values with their average.#####

# def average(a):
#     for d in a:
#         n1 = d.pop('V')
#         n2 = d.pop('VI')
#         d['V+VI'] = (n1 + n2)/2
#     return a
# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# print(average(student_details))

##############################################
#### match key values in two dictionaries.####

# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}
# for i,j in zip(x,y):
#     if i==j:
#         if x[i]==y[j]:
#             print(i,':',x[i],"is present in both x and y")

###############################################################
#### Access the fifth value of each key from the dictionary.####

# a={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#  'y':   [21, 22, 23, 24, 25, 26, 27, 28, 29],
#  'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# print(a)
# for i in a.values():
#     if 15 in i:
#         print(15)
#     elif 25 in i :
#         print(25)  
#     elif 35 in i :
#         print(35) 
# for j in a.values():
#     print(j)
        
#########################################################
#### filter a dictionary based on values.marks > 170 ####

# a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# b={}
# for i,j in zip (a.keys(),a.values()):
#     if j>170:
#         b[i]=j
# print(b)
        
#########################################################
#### convert a given dictionary into a list of lists ####

# a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# b=[]
# for i,j in zip (a.keys(),a.values()):
#     b.append([i,j])
# print(b)

# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b=[]
# for i,j in zip (a.keys(),a.values()):
#     b.append([i,j])
# print(b)

########################################################################################
##### get the total length of all values of a given dictionary with string values. #####

# a={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# b=0
# for i in a.values():
#     for j in i:
#         b+=1
# print(b)

################################################################
#### create a key-value list pairings in a given dictionary.####

# a={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# b={}
# for i,j in zip(a.keys(),a.values()):
#     for k in j:
#         b[i]=k
# print([b])

                









############################
#### Function Questions ####
############################

### 1 to 100 count print ###

# def ask_question():
#     a=1
#     while a<=100:
#         print(a)
#         a+=1
# ask_question()   



### odd even code using function ###

# def vishal(v):
#     a=1
#     b=2
#     while a<=v:
#         print(a,b)
#         a+=2
#         b+=2
# vishal(50)



#### sum of list use function ####

# def sum():
#     a=int(input())
#     b=[]
#     c=0
#     for i in range (a) :
#         d=int(input())
#         b.append(d)
#     print(b)
#     for j in b:
#         c+=j
#     print(c)
# sum()



#### sum of lenth list use of function ####

# def len():
#     a=int(input("how many element do you need in list : "))
#     b=[]
#     c=0
#     for i in range (a) :
#         d=int(input("add element in the list : "))
#         b.append(d)
#     print(b)
#     for j in b:
#         c+=1
#     print("sum of lenth list ", c)
# len()



### list sum ####

# def sum_list(b):
#     a=0
#     for i in b:
#         a+=i
#     print(a)
# a=[23,45,76,78,98,6]
# sum_list(a)




#### find min number from list use min function  ####
# def list1(a):
#     print(min(a))
# a= [8, 6, 4, 8, 4, 50, 2, 7]
# list1(a)



# def tushar(a,b):
#     for i in  (a):
#         c=0
#         for j in (b):
#             c=i*j
#             b.remove(j)
#             break
#         print(c)
# c=[2,3,5,6]
# d=[4,6,9,8]
# tushar(c,d)



#####  perfect number 1 to input #####

# def perfect(a):
#     b=[]
#     for i in range (1,a+1):
#         sum=0
#         for j in range (1,i):
#             if i % j ==0:
#                 sum+=j
#         if i==sum:
#             b.append(sum)
#     print(b)
# v=int(input())
# perfect(v)
        


#### sum and average of the element ####

# def sum_average(e):
#     b=0
#     c=0
#     for i in range (e):
#         d=int(input())
#         b+=d
#         c=b/a
#     print("sum of the number", b)
#     print("average of the number", c)
# a=int(input())
# sum_average(a)



#### jo number 3 or 5 ke multiple and dono ke mulntiple unka sum ####

# def sum1(limit):
#     sum= 0
#     for i in range (1, limit+1):
#         if i % 3 == 0:
#             sum+=i
#         if i % 5 ==0:
#             sum+=i
#     print(sum)
# x=int(input())
# sum1(x)



#### speed limit #####

# def drivers(speed):
#     d=0
#     sum=0
#     for i in range (1,speed+1):
#         if a < 70 :
#             print("Okay")
#             break
#         elif i > 70:
#             d+=1
#             if d%5==0:
#                 sum+=1
#     print(sum)
#     if sum > 12:
#         print("your licence have suspended")
# a=int(input())
# drivers(a) 



##### Check String Lenght ###### 

# def lenth(c):
#     s=0
#     sum=0
#     for i in range (c):
#         if len(a)==len(b):
#             print("len(a)\nlen(b)")
#             break
#         elif len(a)>len(b):
#             sum+=i
#             print(a)
#             break
#         else:
#             print("sum of len(b)",s)
#             s+=i
#             break
# a=input()
# b=input()
# lenth(b)



#### check prime number or not ####

# def primeorNot(num):     
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#         else:
#            print(num,"is a prime number")
# d=int(input("Enter the number :"))
# primeorNot(d)



# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum
# a=int(input("Enter the number :"))
# print(sumofdigits(a))
 


#### food menu ####

# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner"    :
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))











##############################################
########## Recursion Extra questions #########   
############## Sum of the number ############# 

# def sum1(n):
#     if n == 1:
#         return 1 
#     else:
#         return n + sum1(n-1)
# a = int(input("Enter the number :"))
# print(sum1(a))


#############################################
####### check the power of the number #######

# def pow(a,b):
#     if b==0:
#         return 1
#     else:
#         return a * pow(a,b-1)
# a=int(input("Enter the number :"))
# b=int(input("Enter the power :"))
# print(pow(a,b))

#################################
####### count the collum ########

# def se(n,m):
#     if n==1 or m==1:
#         return 1
#     else:
#         return se(n,m-1)+ se(m,n-1)
# a=int(input("Enter the number :"))
# b=int(input("Enter the number :"))
# print(se(a,b))

################################
###### ## table  print ## ######

# def table(a,b):
#     if b > 10:
#         return
#     print(a*b)
#     return table(a, b + 1)
# c=int(input("Enter the number which table do you want to print :"))
# table(c,1)


###################################
########### sum of list ###########

# def list1(a):
#     if len(a) == 1:
#         return a[0]
#     return a[0] + list1(a[1:])
# print(list1([21,464,43,342,45]))



##########################
## this type of pattern ##

# def pattern (b):
#     if b > 31:
#         return 
#     print(b)
#     return pattern(b+3)
# pattern(1)


##############################
######### factorial ##########

# def factorial(number):
#     if number < 1:
#         return 1
#     print(number)
#     return number * factorial(number - 1)
# print(factorial(5))



##########################################
########### Fibonaci Sereies  ############
 
# def getFibNumber(number):
#     if number < 1:
#         return 0
#     elif number < 2:
#         return 1
#     else:
#         return getFibNumber(number-1) + getFibNumber(number-2)
# for i in range(15+1):
#     print(getFibNumber(i))


##################################
####### Triangular Series ########

# def triangular(a):
#     b=0
#     for i in range (1,a+1):
#         b=b+i
#         print(b,end=" ")
# a=int(input("Enter the number :"))
# triangular(a)


