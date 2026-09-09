# #1.8
# from math import comb

# n = 10
# k = 5

# a = n ** k
# b = comb(n + k - 1, k)

# print("а) Различные призы:", a)
# print("б) Одинаковые призы:", b)

#1.9
# from math import factorial

# n = 7
# n1, n2, n3 = 3, 2, 2

# result = factorial(n) // (factorial(n1) * factorial(n2) * factorial(n3))

# print("Количество семизначных чисел:", result)

# 1.10
# from math import factorial, perm

# n = 6

# a = 1 / perm(n, 3)
# b = 1 / factorial(n)

# print("а) P(A) = 1 /", perm(n, 3), "=", round(a, 10))
# print("б) P(B) = 1 /", factorial(n), "=", round(b, 10))

#1.11
# from math import factorial

# n = 6
# p3 = factorial(3)
# p2 = factorial(2)
# p6 = factorial(6)

# m = p3 * p2
# result = m / p6

# print("P(B) =", p3, "*", p2, "/", p6, "=", round(result, 10))

# 1.16
# from math import factorial

# n = factorial(10)

# m1 = 2 * factorial(5) ** 2
# a = m1 / n

# m2 = factorial(5) * 2 ** 5
# b = m2 / n

# print("а) P(A) =", m1, "/", n, "=", round(a, 5))
# print("б) P(B) =", m2, "/", n, "=", round(b, 5))

# 1.17
# from math import comb

# n = comb(36, 7)

# m1 = comb(9, 2) * comb(8, 7)
# a = m1 / n

# m2 = comb(9, 7) * 4 ** 7
# b = m2 / n

# m3 = comb(9, 3) * (6 * comb(4, 4) * comb(4, 2) * comb(4, 1) +
#                    3 * comb(4, 3) * comb(4, 3) * comb(4, 1) +
#                    3 * comb(4, 3) * comb(4, 2) * comb(4, 2))
# d = m3 / n

# print("а) P(A) =", m1, "/", n, "=", round(a, 7))
# print("б) P(B) =", m2, "/", n, "=", round(b, 5))
# print("в) P(D) =", m3, "/", n, "=", round(d, 5))