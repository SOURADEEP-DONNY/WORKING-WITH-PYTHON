with open("salary1.txt","r") as rd:
    with open("output.txt","a") as wd:
        for i in rd.readlines():
            name=i.split(' ')
            wd.write(str(name))
            ##wd.write(salary)
