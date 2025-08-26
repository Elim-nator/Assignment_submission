#Q6. Write a program to perform matrix multiplication.

r1 = int(input("Rows of Matrix A: "))
c1 = int(input("Cols of Matrix A: "))
r2 = int(input("Rows of Matrix B: "))
c2 = int(input("Cols of Matrix B: "))

if c1 != r2:
    print("Matrix multiplication not possible (A_cols must equal B_rows).")
else:
    print("Enter Matrix A elements row-wise:")
    A = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)

    print("Enter Matrix B elements row-wise:")
    B = []
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input(f"B[{i}][{j}]: ")))
        B.append(row)

    C = []
    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            k = 0
            while k < c1:
                total += A[i][k] * B[k][j]
                k += 1
            row.append(total)
        C.append(row)

    print("Resultant Matrix C = A x B:")
    for row in C:
        print(" ".join(str(x) for x in row))
