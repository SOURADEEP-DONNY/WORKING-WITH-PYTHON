with open("salary1.txt","r") as rd:
    with open("output.txt","a") as wd:
        for i in rd.readlines():
            name,salary=i.split(',')
            wd.write(f'{name}\'s salary is{salary}')
