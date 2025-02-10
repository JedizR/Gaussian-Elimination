import random

def generate_random_matrix_and_answer(n):
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
    answer = [random.randint(1, 100) for _ in range(n)]
    return matrix, answer

def show_matrix(matrix, answer):
    for i in range(n):
        for j in range(n+1):
            if j == n:
                print(f" | {answer[i]}")
            else:
                print(matrix[i][j], end=" ")
            
        print()
    
def forward(matrix, answer):
    for i in range(n):
        should_print = False
        if matrix[i][i] != 1:
            factor = matrix[i][i]
            for j in range(n):
                matrix[i][j] /= factor
            answer[i] /= factor
            should_print = True
        for j in range(i+1, n):
            factor = -1.0 * matrix[j][i]
            for k in range(n):
                matrix[j][k] += factor * matrix[i][k]
            answer[j] += factor * answer[i] 
        if should_print == True:
            print(f"\nMatrix after forward #{i+1}:")
            show_matrix(matrix, answer)
            
def backward(matrix, answer):
    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
            factor = -1.0 * matrix[j][i]
            for k in range(n):
                matrix[j][k] += factor * matrix[i][k]
            answer[j] += factor * answer[i]
        print(f"\nMatrix after backward #{n-i}:")
        show_matrix(matrix, answer)
            
n = 3
matrix, answer = generate_random_matrix_and_answer(n)
# matrix = [[1, 1, 1], [3, 2, 1], [2, -1, 4]]
# answer = [6, 10, 12]


print("Original Matrix:")
show_matrix(matrix, answer)
forward(matrix, answer)
backward(matrix, answer)