# -*- coding: utf-8 -*-
"""Tensor_Basics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t_TEIISrYQ4dXq88X38OoXXDajDKndj2

# <font color = dodgerred>**HW1 - 15 Points** </font>
- **You have to submit two files for this part of the HW**
  >(1) ipynb (colab notebook) and<br>
  >(2) pdf file (pdf version of the colab file).**
- **Files should be named as follows**:
>FirstName_LastName_HW_1**
"""

import torch
import time

"""# <font color = dodgerred>**Q1 : Create Tensor (1/2 Point)**
 Create a torch Tensor of shape (5, 3) which is filled with zeros. Modify the tensor to set element (0, 2) to 10 and element (2, 0)  to 100.
"""

#Create a torch Tensor of shape (5, 3) which is filled with zeros.
my_tensor = torch.tensor([
    [0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]
    ])

print(my_tensor)

#Modify the tensor to set element (0, 2) to 10 and element (2, 0) to 100.
my_tensor[0,2] = 10
my_tensor[2,0] = 1000

my_tensor.shape

my_tensor

# Manually set the value at the first row and third column to 10,
# and the value at the third row and first column to 100 in the tensor named "my_tensor".
my_tensor = torch.tensor([
    [0,0,10],[0,0,0],[100,0,0],[0,0,0],[0,0,0]
    ])

my_tensor

"""# <font color = dodgerred>**Q2: Reshape tensor (1/2 Point)**
You have following tensor as input:

```x=torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])```

Using only reshaping functions (like view, reshape, transpose, permute), you need to get at the following tensor as output:

```
tensor([[ 0,  4,  8, 12, 16, 20],
        [ 1,  5,  9, 13, 17, 21],
        [ 2,  6, 10, 14, 18, 22],
        [ 3,  7, 11, 15, 19, 23]])
```


"""

x=torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

x = x.reshape(6,4).transpose(0,1)
x

"""# <font color = dodgerred>**Q3: Slice tensor (1Point)**

- Slice the tensor x to get the following
>- last row of x
>- fourth column of x
>- first three rows and first two columns - the shape of subtensor should be (3,2)
>- odd valued rows and columns
"""

x = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 8, 10], [11, 12, 13, 14, 15]])
x

x.shape

# Student Task: Retrieve the last row of the tensor 'x'
# Hint: Negative indexing can help you select rows or columns counting from the end of the tensor.
# Think about how you can select all columns for the desired row.
last_row = x[-1]
last_row

# Student Task: Retrieve the fourth column of the tensor 'x'
# Hint: Pay attention to the indexing for both rows and columns.
# Remember that indexing in Python starts from zero.
fourth_column = x[ :,3]
fourth_column

# Student Task: Retrieve the first 3 rows and first 2 columns from the tensor 'x'.
# Hint: Use slicing to extract the required subset of rows and columns.
first_3_rows_2_columns = x[:3, :2]
first_3_rows_2_columns

# Student Task: Retrieve the rows and columns with odd-indexed positions from the tensor 'x'.
# Hint: Use stride slicing to extract the required subset of rows and columns with odd indices.
odd_valued_rows_columns = x[::2, ::2]
odd_valued_rows_columns

"""#  <font color = dodgerred>**Q4 -Normalize Function (1/2 Points)**<font>

Write the function that normalizes the columns of a matrix. You have to compute the mean and standard deviation of each column. Then for each element of the column, you subtract the mean and divide by the standard deviation.
"""

# Given Data
x = [[ 3,  60,  100, -100],
     [ 2,  20,  600, -600],
     [-5,  50,  900, -900]]

# Convert to PyTorch Tensor and set to float
X = torch.tensor(x)
X = X.float()

# Print shape and data type for verification
print(X.shape)
print(X.dtype)

# Compute and display the mean and standard deviation of each column for reference
print(X.mean(axis = 0))
print(X.std(axis = 0))

"""- Your task starts here
- Your normalize_matrix function should take a PyTorch tensor x as input.
- It should return a tensor where the columns are normalized.
- After implementing your function, use the code provided to verify if the mean for each column in Z is close to zero and the standard deviation is 1.
"""

def normalize_matrix(X):
  # Calculate the mean along each column (think carefully , you will take mean along axis = 0 or 1)
  mean = X.mean(axis = 0)

  # Calculate the standard deviation along each column
  std = X.std(axis = 0)

  # Normalize each element in the columns by subtracting the mean and dividing by the standard deviation
  y = (X - mean) / std

  return y  # Return the normalized matrix

Z = normalize_matrix(X)
Z

print(Z.mean(axis=0))
print(Z.std(axis=0))

"""# <font color = 'dodgerred'>**Q5: In-place vs. Out-of-place Operations (1 Point)**

1. Create a tensor `A` with values `[1, 2, 3]`.
2. Perform an in-place addition (use `add_` method) of `5` to tensor `A`.
3. Then, create another tensor `B` with values `[4, 5, 6]` and perform an out-of-place addition of `5`.

**Print the memory addresses of `A` and `B` before and after the operations to demonstrate the difference in memory usage. Provide explanation**

"""

#use id() function to get memory location of tensor
A = torch.tensor([1, 2, 3])
print('Original memory address of A:', id(A))
A.add_(5)
print('Memory address of A after in-place addition:', id(A))
print('A after in-place addition:', A)

B = torch.tensor([4, 5, 6])
print('Original memory address of B:', id(B))
y = B
torch.cuda.synchronize()
start_memory = torch.cuda.memory_allocated()
B = B + 5
print('Memory address of B after out-of-place addition:', id(B))
print('B after out-of-place addition:', B)

"""**Provide Explanation for above question here : The memory address of tensor A stayed the same because the operation modify the original tensor without creating a new one. On the other hand, out-of-place addition creates a new tensor "B" that has a different memory address than the original. It is not a problem that the new tensor has the same name as the original one because the contents of the original tensor are stored in y. **

# <font color = 'dodgerred'>**Q6: Tensor Broadcasting (1 Point)**

1. Create two tensors `X` with shape `(3, 1)` and `Y` with shape `(1, 3)`. Perform an addition operation on `X` and `Y`.
2. Explain how broadcasting is applied in this operation by describing the shape changes that occur internally.
"""

X = torch.arange(0,3).reshape(3,1)
Y = torch.arange(0,3).reshape(1,3)
print('Original shapes:', X.shape, Y.shape)
result = X + Y
print('Result:', result)
print('Result shape:', result.shape)

"""**Provide Explanation for above question here : A Shape change needs to occur to ensure the two tensors are compatible for addition. The dimension that is smaller is "broadcasted" to match the larger dimension. X & Y are both broadcasted to the dimension of (3,3, which is why the result also has the dimension of (3,3).**

# <font color = 'dodgerred'>**Q7: Linear Algebra Operations (1 Point)**

1. Create two matrices `M1` and `M2` of compatible shapes for matrix multiplication. Perform the multiplication and print the result.
2. Then, create two vectors `V1` and `V2` and compute their dot product.
"""

M1 = torch.randn(3,4)
M2 = torch.randn(4,5)
mat_multiplication =  torch.mm(M1,M2)
print('Matrix multiplication result:', mat_multiplication)

V1 = torch.randn(5)
V2 = torch.randn(5)
dot_product = torch.dot(V1,V2)
print(V1)
print(V2)
print('Dot product:', dot_product)

"""# <font color = 'dodgerred'>**Q8: Manipulating Tensor Shapes (1 Point)**

Given a tensor `T` with shape `(2, 3, 4)`, demonstrate how to
1. reshape it to `(3, 8)` using view,
2. reshape it to `(4, 2, 3` using reshape,
3. transpose the first and last dimensions using permute.
4. explain what is the difference between reshape and view
"""

T = torch.rand(2, 3, 4)
T_view =  T.view(3,8)
print('T_view shape:', T_view.shape)

T_reshape =  T.reshape(4,2,3)
print('T_reshape shape:', T_reshape.shape)

T_permute =  T.permute(2,1,0)
print('T_permute shape:', T_permute.shape)

"""**Provide Explanation for above question here : View performs the same task as reshape, however, it will not create a copy and will instead share data with the original tensor. On the other hand reshape returns a tensor that is a copy of the input. Additionally, reshape can be used on contigious and non-contiguous tensors whereas view can only be used on contiguous tensors. These are tensors that are stored as an unbroken block of memory.**

# <font color = 'dodgerred'>**Q9: Tensor Concatenation and Stacking (1 Point)**

Create tensors `C1` and `C2` both with shape (2, 3).
1. Concatenate them along dimension 0 and then along dimension 1. Print the shape of the resulting tensor.
2. Afterwards, stack the same tensors alomng dimension 0  and print the shape of the resulting tensor.
3. What is the difference between stacking and concatinating.
"""

C1 = torch.rand(2, 3)
C2 = torch.rand(2, 3)
concatenated_dim0 =  torch.cat((C1,C2), dim=0)
print('Concatenated along dimension 0:', concatenated_dim0.shape)

concatenated_dim1 = torch.cat((C1,C2), dim=1)
print('Concatenated along dimension 1:', concatenated_dim1.shape)

stacked =  torch.stack((C1,C2), dim=0)
print('Stacked tensor shape:', stacked.shape)

"""**Explain the diffrence between concatinating and stacking here:Concatinating combines the tensors along a dimension, and both must be the same size in that dimension. The new tensor's specified dimension will be changed, and the other dimension will be the same. Stacking instead creates a new dimension with tensors of the same shape. The new tensor has one additional dimension in stacking where the number of dimensions stay the same in concatinating. **

# <font color = 'dodgerred'>**Q10: Advanced Indexing and Slicing (1 Point)**

1. Given a tensor `D` with shape (6, 6), extract elements that are greater than 0.5.
2. Then, extract the second and fourth rows from `D`.
3. Finally, extract a sub-tensor from the top-left 3x3 block.
"""

D = torch.rand(6, 6)
print(D)
D_greater = D[D > 0.5]
print('Elements greater than 0.5:\n', D_greater)

second_fourth_rows = D[[1,3],:]
print('\nSecond and fourth rows:\n', second_fourth_rows)

top_left_3x3 =  D[:3, :3]
print('\nTop-left 3x3 block:\n ', top_left_3x3)

"""# <font color = 'dodgerred'>**Q11: Tensor Mathematical Operations (1 Point)**

1. Create a tensor `G` with values from 0 to π in steps of π/4.
2. Compute and print the sine, cosine, and tangent logarithm and the exponential of `G`.
"""

G = torch.arange(0, torch.pi, (torch.pi / 4))
print('G:', G)
print('Sine of G:',  torch.sin(G))
print('Cosine of G:',  torch.cos(G))
print('Tangent of G:',  torch.cos(G))
print('Natural logarithm of G:', torch.log(G))
print('Exponential of G:',  torch.exp(G))

"""# <font color = 'dodgerred'>Q12: **Tensor Reduction Operations (1 Point)**

1. Create a 3x2 tensor `H`.
2. Compute the sum of `H`. Print the result and shape after taking sun.
3. Then, perform the same operations along dimension 0 and dimension 1, printing the results and shapes.
4. What do you observe? How the shape changes?
"""

H = torch.rand(3, 2)
print('H:', H, end = "\n\n")
print('Shape of original Tensor H', H.shape, end = "\n\n")

sum_H = H.sum()
print('Sum of H:', sum_H)
print('Shape after Sum of H:',  sum_H.shape,  end = "\n\n")

sum_H0 = H.sum(axis=0, keepdim=True)
print('Sum of H along dimension 0:', sum_H0)
print('Shape after sum of H along dimension 0:', sum_H0.shape,  end = "\n\n")

sum_H1 = H.sum(axis=1, keepdim=True)
print('Sum of H along dimension 1:', sum_H1)
print('Shape after sum of H along dimension 1:', sum_H1.shape)

"""**Provide your observations on shape changes here: the H.sum() function takes the sum of the entire tensor which produces only 1 number. This is a scalar output which is represented by the torch.Size([]). It is empty since it is only 1 number. Computing the sum along dimension 0 means we are computing the sum along the rows. It has the size of [1,2] since there are 2 columns in the tensor. When we sum along axis 1, we sum along the columns, which is why the tensor has the size of [3,1], since there are 3 rows in the tensor. These are 2 dimensional tensors since keepdim=True.**

# <font color = 'dodgerred'>**Q13: Working with Tensor Data Types (1 Point)**

1. Create a tensor `I` of data type float with values `[1.0, 2.0, 3.0]`.
2. Convert `I` to data type int and print the result.
3. Explain in which scenarios it's necessary to be cautious about the data type of tensors.
"""

# Solution for Q16
I =  torch.tensor([1.0,2.0,3.0], dtype = torch.float32)
print('I:', I)
I_int =  I.to(dtype=torch.int32)
print('I converted to int:', I_int)

"""**Your explanations here: It is necessary to be catious about the data type of tensors when there is a concern about precision, compatibility, and loss of information. Float datatypes tend to be more precise, but that precision can result in unnecessary memory usage or computational efficiency if that precision doesn't offer any value. Converting from a Float to Integer datatype can result in loss of information if the precision was necessary. It is also important to consider when combining tensors**

# <font color = 'dodgerred'>**Q14. Speedtest for vectorization 1.5 Points** </font>

Your goal is to measure the speed of linear algebra operations for different levels of vectorization.

1. Construct two matrices $A$ and $B$ with Gaussian random entries of size $1024 \times 1024$.
1. Compute $C = A B$ using matrix-matrix operations and report the time. (Hint: Use torch.mm)
1. Compute $C = A B$, treating $A$ as a matrix but computing the result for each column of $B$ one at a time. Report the time. (hint use torch.mv inside a for loop)
1. Compute $C = A B$, treating $A$ and $B$ as collections of vectors. Report the time. (Hint: use torch.dot inside nested for loop)
"""

## Solution 1
torch.manual_seed(42) # do not change this
A = torch.randn(1024, 1024)
B = torch.randn(1024, 1024)

## Solution 2
start = time.time()
C_mm = torch.mm(A, B)

print("Matrix by matrix: " + str(time.time()-start) + " seconds")

## Solution 3
C_mv = torch.empty(1024,1024)
start = time.time()
for i in range(B.shape[1]):
    C_mv[:, i] = torch.mv(A, B[:, i])

print("Matrix by vector: " + str(time.time()-start) + " seconds")

## Solution 4
C_dot = torch.empty(1024,1024)
start = time.time()
for i in range(A.shape[1]):
    for j in range(B.shape[1]):
        C_dot[i, j] = torch.dot(A[:, i], B[:, j])

print("vector by vector: " + str(time.time()-start) + " seconds")

"""# <font color = 'dodgerred'>**Q15 : Redo Question 14 by using GPU - 1.5 Points**

<font size = 4, color = 'dodgerred'> **Using GPUs**

How to use GPUs in Google Colab<br>
In Google Colab -- Go to Runtime Tab at top -- select change runtime type -- for hardware accelartor choose GPU
"""

# Check if GPU is availaible
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)

## Solution 1
torch.manual_seed(42)
A= torch.randn((1024, 1024),device=device)
B= torch.randn((1024, 1024),device=device)

## Solution 2
start=time.time()

C_mm = torch.mm(A, B)
C_mm_cpu = C_mm.to("cpu")

print("Matrix by matrix: " + str(time.time()-start) + " seconds")

## Solution 3
C= torch.empty(1024,1024, device = device)
start = time.time()

for i in range(B.shape[1]):
    C_mv[:, i] = torch.mv(A, B[:, i])
C_mv_cpu = C_mv.to("cpu")

print("Matrix by vector: " + str(time.time()-start) + " seconds")

## Solution 4
C = torch.empty(1024,1024, device = device)
start = time.time()

for i in range(A.shape[1]):
    for j in range(B.shape[1]):
        C[i, j] = torch.dot(A[:, i], B[:, j])
C_vv_cpu = C.to("cpu")

print("vector by vector: " + str(time.time()-start) + " seconds")