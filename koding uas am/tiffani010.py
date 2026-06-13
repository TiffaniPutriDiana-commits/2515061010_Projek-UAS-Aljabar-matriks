def penjumlahan(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Dimensi kedua vektor harus sama.")
    hasil = []
    for i in range(len(v1)):
        hasil.append(v1[i] + v2[i])
    return hasil


def pengurangan(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Dimensi kedua vektor harus sama.")
    hasil = []
    for i in range(len(v1)):
        hasil.append(v1[i] - v2[i])
    return hasil


def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Dimensi kedua vektor harus sama.")
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total




def acos_manual(x):
    if x >= 1.0:
        return 0.0
    if x <= -1.0:
        return 3.141592653589793
    arcsin = 0.0
    term = x
    for n in range(100):
        arcsin += term
        term *= x * x * (2 * n + 1) * (2 * n + 1) / ((2 * n + 2) * (2 * n + 3))
    return 3.141592653589793 / 2 - arcsin


def sudut(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Dimensi kedua vektor harus sama.")
    dp = dot_product(v1, v2)
    
    panjang_v1 = 0
    for i in range(len(v1)):
        panjang_v1 += v1[i] ** 2
    panjang_v1 = panjang_v1 ** 0.5
 
    # Hitung panjang vektor v2
    panjang_v2 = 0
    for i in range(len(v2)):
        panjang_v2 += v2[i] ** 2
    panjang_v2 = panjang_v2 ** 0.5
 
    if panjang_v1 == 0 or panjang_v2 == 0:
        raise ValueError("Salah satu vektor adalah vektor nol.")
    cos_theta = dp / (panjang_v1 * panjang_v2)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    # Konversi radian ke derajat manual: derajat = radian * (180 / pi)
    return acos_manual(cos_theta) * (180 / 3.141592653589793)