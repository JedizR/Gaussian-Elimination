import random
import numpy as np
import time
import copy

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
    global TIME_USED
    time_start = time.time()
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
    time_end = time.time()
    TIME_USED += time_end - time_start
            
def backward(matrix, answer):
    global TIME_USED
    time_start = time.time()
    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
            factor = -1.0 * matrix[j][i]
            for k in range(n):
                matrix[j][k] += factor * matrix[i][k]
            answer[j] += factor * answer[i]
        print(f"\nMatrix after backward #{n-i}:")
        show_matrix(matrix, answer)
    time_end = time.time()
    TIME_USED += time_end - time_start
    
def compare_error(normal_error, Hilbert_error):
    print("    Error from Normal    |   Error from Hilbert    |   difference")
    for i in range(n):
        print_text_numpy = " " + str(normal_error[i])
        while len(print_text_numpy) < 25:
            print_text_numpy = print_text_numpy + " "
        print(f"{print_text_numpy}",end="|")
        print_text_manual = " " + str(Hilbert_error[i])
        while len(print_text_manual) < 25:
            print_text_manual = print_text_manual + " "
        print(f"{print_text_manual}",end='|')
        difference_text = " " + str(abs(normal_error[i] - Hilbert_error[i]))
        print(f"{difference_text}")
        
def generate_error_vector(A, x, b):
    error_vector = []
    for i in range(n):
        error = -1*b[i]
        for j in range(n):
            error += A[i][j] * x[j]
        error_vector.append(float(error))
    return error_vector

def Hilbert_matrix_generator(n):
    H = np.zeros((n, n))
    answer = [random.randint(1, 100) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            H[i][j] = 1 / (i + j + 1)
    return H, answer

n = 20
# Normal Matrix
TIME_USED = 0
matrix, answer = generate_random_matrix_and_answer(n)
# matrix = [[1, 1, 1], [3, 2, 1], [2, -1, 4]]
# answer = [6, 10, 12]
original_matrix = copy.deepcopy(matrix)
original_answer = copy.deepcopy(answer)
print("Original Matrix:")
show_matrix(matrix, answer)
forward(matrix, answer)
backward(matrix, answer)
error_vector = generate_error_vector(original_matrix, answer, original_answer)
print(f"\nError Vector:{error_vector}")
normal_time = TIME_USED

# Hilbert Matrix
TIME_USED = 0
H, H_answer = Hilbert_matrix_generator(n)
original_H = copy.deepcopy(H)
original_H_answer = copy.deepcopy(H_answer)
print(f"\nHilbert Matrix of order {n}:")
print(H)
forward(H, H_answer)
backward(H, H_answer)
H_error_vector = generate_error_vector(original_H, H_answer, original_H_answer)
print(f"\nError Vector for Hilbert Matrix:{H_error_vector}")
hilbert_time = TIME_USED
print(f"Normal Time:{normal_time}")
print(f"Hilbert Time:{hilbert_time}")

# Comparison
compare_error(error_vector, H_error_vector)