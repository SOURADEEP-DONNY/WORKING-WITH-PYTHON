N=int(input())
if N<=500:
    nums=[int(i) for i in input().split()]
    score_list=[]
    
        
    for j in nums:
            
        if j>=100 and j<=999:
            score=0
            j=str(j)
            p=j[0]
            q=j[1]
            r=j[2]
            p=int(p)
            q=int(q)
            r=int(r)
                
            maxi=max(p,q,r)
            mini=min(p,q,r)
                
        score=(maxi*11)+(mini*7)
        score_list.append(score)
    #print(score_list)
    bit_score=[]
    for i in score_list:
        k=i%100
        bit_score.append(k)
    print(bit_score)


    even=[]
    odd=[]
    for i in range(len(bit_score)):
        if i%2 == 0:
            even.append(bit_score[i])
        else:
            odd.append(bit_score[i])
    print('EVEN BIT SCORE',even)
    print('ODD BIT SCORE',odd)




    odd_s=[]
    even_s=[]

    for i in odd:
        k=i//10
        odd_s.append(k)
    print('ODD_S',odd_s)
    for i in even:
        k=i//10
        even_s.append(k)
    
    print('EVEN_S',even_s)

        


    count1=0
    count=0


    for j in range(len(odd_s)):
        p=odd_s.pop()
        for i in odd_s:
            if p==i:
                count=count+1
    for j in range(len(even_s)):
        p=even_s.pop()
        for i in even_s:
            if p==i:
                count1=count1+1    
##    print(count)
##    print(count1)

    if count>2:
        count=2
    if count1>2:
        count=2
    output=count+count1
    print('OUTPUT=',output)
