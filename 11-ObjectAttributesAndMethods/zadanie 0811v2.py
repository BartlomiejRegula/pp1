class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def row(array):
        for i in array:
            if i!=array[-1]:
                print(i,end=',')
            else:
                print(i,end='')
        print()
            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)
Arrays.row(my_array)
print(my_array)