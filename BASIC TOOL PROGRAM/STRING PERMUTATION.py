def string_permute(input_string):
    l=len(input_string)
    if l==0:
        return [' ']
    inter=string_permute(input_string[1:l])
    final_list=[]
    for i in range(0,len(inter)):
        for j in range(0,l):
            check_strings=inter[i][0:j]+input_string[0]+inter[i][j:l-1]
            if check_strings not in final_list:
                final_list.append(check_strings)
    return final_list

k=input("\nENTER A STRING:-")
print(string_permute(k))
