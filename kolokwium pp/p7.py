class C:
    @staticmethod
    def m(n):
        x=''
        for i in str(n):
            if int(i)%2==0:
                x+=str(i)
        return x

    