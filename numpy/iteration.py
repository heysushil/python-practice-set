# numpy 

'''
npiter
    EXAMPLE:
        import numpy as np

        arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

        # range(star,end,diff)
        # np.nditer(start:end, ::number postion)
        # if(2 <= 3) = IN nditer 1ST ARGUMENT 0 SHOWING STARING POINT AND 2 SHOWING N-1 SAME AS RANGE [0,2] = HERE 2 IS EXCULUDED FROM RANGE
        # ::2 NOT DIFFRENCE IT'S ARRAY VALUE POSTION LIKE AS [1,2,3,4,5]. RESULT 1,3,5
        for x in np.nditer(arr[0:2, ::2]):
            print(x)

Iterating SUBMETHODS:
    nditer() = NORAMAL ITERATE SAME LIKE NESTED FOR LOOP
    op_dtypes() = IT CHANGE THE DATA TYPE OF ARRAY TO OTHER. LIKE op_dtypes('S') => array => stirng
    ndenumerate() = GIVES INDEX AND VALUE BOTH

JOINING:
    concatenate() - USE SUB METHOD concatenate() LIKE concatenate((ARR1,ARR2), axis=1)
    
MATRIX:
    stack() - 
            - EXAMPLE = stack(arr1,arr2): SHOW NORAML MATRIX SIDE BY SIDE
            - EXAMPLE = stack((arr1,arr2), axis=1): CONCATENATE ARR1 AND ARR2 WITH USE OF AXIS=1
    EXAMPLE: 
        1ST MARTIX = [1 2 3] = [00 01 02] (2*3) = (3*2)
        2ND MARTIX = [4 5 6]   [10 11 12] (2*3) = (3*2)

        OUTPUT: 
            [1 4]
            [2 5]
            [3 6]
    hstack() - horizontal line or FOR ROW - np.hstack((arr1, arr2))

    vstack() - vertical line or FOR COLUMN - np.vstack((arr1, arr2))

    dstack() - DIRECT CONCATENATE 2 MATRIXES NO NEED OF AXIS
             - EXAMPLE: arr = np.dstack((arr1, arr2))

SPLIT:
    array_split(): 
        EXAMPLE: newarr = np.array_split(arr, 3) : SPLIT 3 ARRAYS OF 2'S EACH
                 newarr = np.array_split(arr, 3, axix=1): CONCATENATE ARRYS

                newarr = np.hsplit(arr, 3): DIRECT CONCATENATE ARRAYS
                OUTPUT: 
                    [1 4 7 10 13 16]
                    [2 5 8 11 14 17]
                    [3 6 9 12 15 18]

'''