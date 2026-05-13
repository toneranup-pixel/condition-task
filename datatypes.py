
# a={'ram':44,'shyam':55}
# for i in a:
#     print(i)
# for i in a.key:
#     print(i)
# for i in a.value:
#     print(i)
# for i in a.item:
#     print(i)
# #seperate for key and seperate for value not in tuple
# for i,j in a.item:
#     print(i,j)
# 1
# items=[3,5,7,9,11,13]
# r_item=items.pop(4)
# items.insert(2,r_item)
# items.append(r_item)
# print(items)

# 3
# first_set={27,43,34}
# second_set={34,93,22,27,43,53,48}
# common_element=first_set.issubset(second_set)
# if common_element:
#     print(first_set.clear())
# else:
#     print("no subset")

# 4
# month={'jan':47,'feb':52,'march':47,'april':44,'may':52,'june':53,'july':54,'august':44,'sept':54}
# print(list(set(month.values)))

# sample_list=[87,45,41,65,94,41,99,94]
# remove=tuple(set(sample_list))
# print(max(remove),min(remove))

# 2
# first_set={23,42,65,57,78,83,29}
# second_set={57,83,29,67,73,43,48}
# common_element=first_set.intersection(second_set)
# if common_element:
#     a=first_set.difference(second_set)
#     print(a)
# else:
#     print("no common element found")

# 6
# club_a={"ram","hari","shyam"}
# club_b={"ram","gita","hari"}
# common_element=club_a.intersection(club_b)
# if common_element:
#     print(f'{common_element} exit')
# else:
#     print("no overlapping members found between groups")

# 7
# required_task={'email','report','meeting'}
# completed_task={'email','report'}
# a=required_task.issubset(completed_task)
# if a:
#     print("all task done")
# else:
#     print("some task pending")

# 8
# student_email={'ram':'ram@gmail.com','hari':'hari@gmail.com','shyam':'shyam@gmail.com'}
# stdnt_name=input("enter a student name:")
# result=student_email.get(stdnt_name,'user not found')
# print(result)




    


    