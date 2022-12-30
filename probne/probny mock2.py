def f2(a1,a2):

    sum1=0
    for i in a1:
        if i>=10 and i<100:
            sum1+=1
   
    sum2=0
    for i in a2:
        if i>=10 and i<100:
             sum2+=1
  
    if sum1==sum2:
        return True
    else:
        return False



print(f2([23,7,16,34],[1,18,79,20,6,111]))

