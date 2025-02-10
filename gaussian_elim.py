import random

def generate_random_matrix_and_answer(n):
    matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
    answer = [random.randint(1, 100) for _ in range(n)]
    return matrix, answer

n = 5
matrix, answer = generate_random_matrix_and_answer(n)

for i in range(n):
    for j in range(n+1):
        if j == n:
            print(f" | {answer[i]}")
        else:
           print(matrix[i][j], end=" ")
        
    print()