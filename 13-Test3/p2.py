def f(arr):
    x=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != (i+1) * (j+1):
                return False
    return True





def main():
    print(f([[1,2,3],[2,4,6],[3,6,9]])) 
    print(f([[1,2],[2,4]]))
    print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))
    print(f([[1,2],[3,6]]))
    print(f([[1,2,3],[2,4,6]]))
    print(f([[1,2,3],[2,5,6]]))

if __name__=='__main__':
    main()