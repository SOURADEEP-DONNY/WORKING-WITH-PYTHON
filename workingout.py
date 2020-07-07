london_gold=0
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
for i in nested_d.keys():
    if i=='London':
        
        print(nested_d[i])
        for p in nested_d[i].keys():
            if p == 'Great Britain':
                london_gold=nested_d[i][p]
                print(london_gold)
                
