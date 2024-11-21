import numpy as np
def strassen(a, b):
    n = len(a)
    if n == 1:
        return a * b

    k = n // 2
    a11, a12, a21, a22 = a[:k, :k], a[:k, k:], a[k:, :k], a[k:, k:]
    b11, b12, b21, b22 = b[:k, :k], b[:k, k:], b[k:, :k], b[k:, k:]

    m1 = strassen(a11 + a22, b11 + b22)
    m2 = strassen(a21 + a22, b11)
    m3 = strassen(a11, b12 - b22)
    m4 = strassen(a22, b21 - b11)
    m5 = strassen(a11 + a12, b22)
    m6 = strassen(a21 - a11, b11 + b12)
    m7 = strassen(a12 - a22, b21 + b22)

    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 - m2 + m3 + m6

    c = np.zeros((n, n), dtype=int)
    c[:k, :k
