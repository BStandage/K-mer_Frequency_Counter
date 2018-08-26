from collections import Counter

def count_kmers(str, k):
    kmers = []

    for i in range(len(str) - k + 1):
        kmers.append(str[i: i + k])

    return kmers


if __name__ == '__main__':
    str = input('Enter a string of k-mers: ')
    k = int(input(' Enter a value for k: '))
    print(Counter(count_kmers(str, k)))