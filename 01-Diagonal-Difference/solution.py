import math

def diagonalDifference(arr):
    primary_sum = 0
    secondary_sum = 0
    matrix_size = len(arr)
    
    for i in range(matrix_size):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][matrix_size - 1 - i]
        
    return abs(primary_sum - secondary_sum)

if __name__ == '__main__':
    # Sample test matrix
    sample_arr = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    
    result = diagonalDifference(sample_arr)
    print("Diagonal Difference Result:", result)