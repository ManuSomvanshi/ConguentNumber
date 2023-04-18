import numpy as np
import matplotlib.pyplot as plt
def GCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

def generate_primitives(N):
    m = 1
    primitives = []
    while True:
        n=1
        while n<m:
            if m>n and m%2 != n%2 and GCD(m,n) ==1:
                primitives.append({"x": m**2-n**2, "y": 2*m*n, "z": m**2 + n**2, "area": m*n*(m**2 - n**2)})
            n+=1
        if m == N:
            break
        m+=1
    return primitives

def remove_square(N):
    n = 2
    while True:
        #print(N, " ", n)
        while N%(n**2) == 0:
            N = int(N/n**2)
        if n > np.sqrt(N):
            break
        n+=1
    return int(N)

#a function to generate a list of square free congruent numbers.
def gen_congruent(N, method):
    if method == "brute force":
        S = generate_primitives(N)
        cong_numbers = set()
        for d in S:
            cong_numbers.add(remove_square(d["area"]))
        cong_numbers = list(cong_numbers)
        cong_numbers.sort()
        return cong_numbers

    elif method == "tunnell":
        m = 1
        cong_numbers = set()
        while m <= N:
            n = remove_square(m)
            if n%8 == 5 or n%8 == 6 or n%8 == 7:
                cong_numbers.add(n)
            elif n%2 == 1:
                a = 0
                b = 0
                for x in range(-1*int(np.sqrt(n)), int(np.sqrt(n)) + 1):
                    for y in range(-1*int(np.sqrt(n)), int(np.sqrt(n)) + 1):
                        for z in range(-1*int(np.sqrt(n)), int(np.sqrt(n)) + 1):
                            if 2*x**2 + y**2 + 8*z**2 == n:
                                a+=1
                            if 2*x**2 + y**2 + 32*z**2 == n:
                                b+=1
                if a == 2*b:
                    cong_numbers.add(n)
            elif n%2 == 0:
                a = 0
                b = 0
                for x in range(-1*int(np.sqrt(n)), int(np.sqrt(n)) + 1):
                    for y in range(-1*int(np.sqrt(n)), int(np.sqrt(n)) + 1):
                        for z in range(-1*int(np.sqrt(n)), int(np.sqrt(n)) + 1):
                            if 8*x**2 +2*y**2 + 16*z**2 == n:
                                a+=1
                            if 8*x**2 + 2*y**2 + 64*z**2 == n:
                                b+=1
                if a == 2*b:
                    cong_numbers.add(n)
            m+=1
        cong_numbers = list(cong_numbers)
        return cong_numbers
# a function to generate a list of congruent numbers assuming tunnell's theorem
#print(gen_congruent(1000, method = "tunnell"))

# distribution of congruent numbers

def distribution(N):
    X = list(range(1, N))
    Y = []
    for x in X:
        cong_numbers = gen_congruent(x, "tunnell")
        Y.append(len(cong_numbers)/x)
    plt.plot(X, Y, "b-")
    plt.xlabel(r"$x$")
    plt.ylabel(r"Ratio of congruent numbers less than $x$")
    plt.show()

#distribution(300)
