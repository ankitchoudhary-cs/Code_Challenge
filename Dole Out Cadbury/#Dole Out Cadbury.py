#Dole Out Cadbury


def NumOfChildren(length, width):
    if length == width:
        return 1
    else:
        left = length - width
        return 1 + NumOfChildren(max(left,width), min(left, width))



if __name__ == "__main__":
    P = int(input())
    Q = int(input())
    R = int(input())
    S = int(input())
    
    
    numOfChildren = 0
    
    for length in range(P,Q + 1):
        for width in range(R, S + 1):
            numOfChildren += NumOfChildren(max(length,width), min(length,width))


    print(numOfChildren)