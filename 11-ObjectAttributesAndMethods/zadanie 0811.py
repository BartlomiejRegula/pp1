class Arrays():
    @staticmethod
    def method_name(number_of_array_elements, value_of_array_elements):
        a=[]
        for i in range(number_of_array_elements):
            a.append(value_of_array_elements)
        return a

    @staticmethod
    def method_name2(number_of_array_elements, value_from, value_to):
        import random
        b=[]
        for j in range(number_of_array_elements):
            x=random.randrange(value_from,value_to)
            b.append[x]
        return b

    # def method_name3(array, value_from, value_to):





m=Arrays.method_name(4,1)
m2=Arrays.method_name2(4,2,5)
print(m)
print(m2)
