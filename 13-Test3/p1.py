def f(n):
    # res=""
    # for i in range(n):
    #     if n<=0:
    #         return res
    #     if i!=0 and i%5==0:
    #         res+="-"
    #         res+="/"
    #     else:
    #         res+="/"
    # return(res)

    x=''
    for i in range(n):
        if (i%5)!=0 or i==0 :
            x+=('/')        
        elif (i%5)==0 and i!=0:
            x+=('-')
            x+='/'
    return(x)

def main():
    print(f(-7),'1')
    print(f(0),'2')
    print(f(5))
    print(f(7))
    print(f(6),'6')
    print(f(10))
    print(f(11))



if __name__=='__main__':
    main()