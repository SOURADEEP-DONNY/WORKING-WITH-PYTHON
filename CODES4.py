olympics=('Beijing','London','Rio','Tokyo')
print(olympics)

olymp = ('Rio', 'Brazil', 2016)
city=olymp[0]
country=olymp[1]
year=olymp[2]


country=[]
t=()
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
for i in tuples_lst:
    t=i[1]
    print(t)
    country.append(t)
print(country)

def info(name,gender,age,bday_month,hometown):
    t=(name,gender,age,bday_month,hometown)
    name,gender,age,bday_month,hometown=t
    return t
print(info('SOURADEEP','M',21,'NOVEMBER','KOLKATA'))

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals=[]
for i in gold.items():
    num_medals.append(i)
print(num_medals)

