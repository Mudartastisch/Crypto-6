#!/usr/bin/env python3

# ----------------------------------------------------------
import sys
import gmpy2
from gmpy2 import mpz, fmod, powmod, mul

def main():
    if not (sys.argv[1] == "-i"):
        print("Invalid usage! rsa_mitm_attack_117516.py -i <filename>")
        quit()
    print("reading in values")
    lines = [line.rstrip('\n') for line in open(sys.argv[2])]
    n = mpz(lines[2])
    e = int(lines[4])
    C = mpz(lines[6])
    b = int(lines[8])
    S = int(b) 
    T = int(b)
    print("starting dict creation")
    found = False
    dict = {}

    if (S * T) < b:
        print("S * T is too small")
        print(S * T)
        quit()
    for s in range(1, S, 1):
        Cs = fmod(mul(C, (powmod(powmod(s, e, n), -1, n))), n)
        dict[Cs] = s
    print("finished dict creation")
    print("starting comparision")
    for t in range(1, T, 1):
        key = powmod(t, e, n)
        if key in dict:
            print("Found collision at s = " + str(dict[key]) + " and t = " + str(t) + ", both equal " + str(key))
            print("X = " + str(s * t))
            found = True

    if not found:
        print("No collision found")


# ----------------------------------------------------------

if __name__ == "__main__":
    main()



