B = 'ZBBACAA'
A = 'ABCBCYA'
# answ = PSIIP
# len(A) == len(B)
# P = 0
# S = 1
# I = 2
C = {}

for i in range(len(B)):
    if B[i] == A[i]:
        C[i] = 'P'
    else:
        for j in range(len(A)):
            if not j in C:
                if B[i] == A[j]:
                    C[i] = 'S'
                    C[j] = 'I'
        if not i in C:
            C[i] = 'I'

# print(C)
C = dict(sorted(C.items()))
print(C)
print(''.join(list(C.values())))









# ch_dict = {}
# td = dict(zip(B, A))
# for i, v in enumerate(td.items()):
#     ch_dict[i] = v

# # Отсортировал по plagiarism
# for i, v in ch_dict.items():
#     if v[0] == v[1]:
#         ch_dict[i] = 0

# for i, v in ch_dict.items():
#     if isinstance(v, tuple):
#         check = v[0]
#         second_chrs = []


# print(ch_dict)