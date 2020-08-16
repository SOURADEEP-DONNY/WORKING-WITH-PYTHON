list1=[int(i) for i in input().split()]
stages=int(input())

def list_rot():
    #input_list=[int(i) for i in input().split()]
    input_list=list1
    input_list_length=len(input_list)
    output_list=[0] * input_list_length
    stage=stages
    #stage=int(input("Number of stages:-"))
    for i in range(input_list_length):
        if i+stage<len(input_list):
            output_list[i+stage]=input_list[i]
        else:
            new_index=(i+stage)%input_list_length
            output_list[new_index]=input_list[i]
    return output_list


print(list_rot())
