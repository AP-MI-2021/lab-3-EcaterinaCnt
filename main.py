def is_palindrome(n):
    '''
    Determina daca un numar este palindrom
    :param n: numarul introdus
    :return: returneaza valoarea de adevar
    '''

    cifre_n=[]
    while n > 0:
        cifre_n.append(n%10)
        n=n//10
    lungime=len(cifre_n)
    for i in range (0,lungime//2):
        if cifre_n[i]!=cifre_n[lungime-1-i]:
            return False
    return True

def test_is_palindrome():
    '''
    Determina daca un numar este palindrom
    :return: returneaza True daca acesta este palindrom, iar False in caz contrar
    '''

    assert is_palindrome(7557) is True
    assert is_palindrome(15) is False
    assert is_palindrome(1221) is True

def get_palindrom(lst):
    '''
    Determina numerele palindrom dintr o lista
    :param lst: lista de numere intregi
    :return: returneaza o lista cu numere palindrom din lst
    '''

    result = []
    for num in lst:
        if is_palindrome(num):
            result.append(num)
    return result


def toate_nr_sunt_palindrom(l):
    '''
    Determina daca toate numerele dintr o lista sunt prime
    :param l: lista de numere intregi
    :return: returneaza True daca toate numerele din lista sunt palindrom, si False daca nu
    '''

    for x in l:
        if is_palindrome(x) is False:
            return False
    return True

def test_toate_nr_sunt_palindrom():
    '''
    Determina daca toate numerele din lista sunt palindroame
    :return: returneaza True daca toate numerele sunt palindroame, iar False in caz contrat
    '''

    assert toate_nr_sunt_palindrom([1221, 111, 3113]) is True
    assert toate_nr_sunt_palindrom([2332, 545, 1001]) is True
    assert toate_nr_sunt_palindrom([123, 2332, 545]) is False

def div_count(n):
    '''
    Numara numarul de divizori ai unui numar
    :param n: numarul intreg introdus
    :return: returneaza numarul de divizori ai numarului introdus
    '''

    d=0
    for i in range(1,(int)(n ** 0.5) + 1):
        if n%i == 0:
            if n/i == i:
                d=d+1
            else:
                d=d+2
    return d

def show_menu():
    print("1. Citire lista: ")
    print("2. Afisarea numerelor palindrom: ")
    print("3. Cea mai lunga secventa este: ")
    print("x. Exit. ")


def read_list():
    lst = []
    lst_str = input('Dati numere separate prin spatiu: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append((int(num_str)))
    return lst

def numar_inversat(num):
    '''
    Determinam inversul fiecarui numar
    :param num: numarul intreg introdus
    :return: returneaza inversul acestuia
    '''

    invers=0
    while num:
        invers = invers * 10 + num % 10
        num //= 10
    return invers

def test_numar_inversat():
    '''
    Testeaza inversele unor numere citite
    :return: returneaza inversul numarului introdus
    '''

    assert numar_inversat(121) == 121
    assert numar_inversat(1234) == 4321
    assert numar_inversat(111) == 111

def get_longest_same_div_count(lst: list[int]) -> list[int]:
    '''
    Determinacea mai lunga subsecventa de numere care au acelasi numar de divizori
    :param lst: lista de numere intregi
    :return: returneaza cea mai lunga subsecventa de numere care respecta proprietatea
    '''

    n = len(lst)
    result=[]
    for st in range(n):
        for dr in range (st, n):
            d=div_count(lst[st])
            for num in lst[st: dr+1]:
                if div_count(num)!=d:
                    d=-1
                    break
            if (d!=-1):
                if dr-st+1>len(result):
                    result=lst[st: dr+1]
    return result


def test_longest_same_div_count():
    '''
    Determina cea mai lunga subsecventa de numere cu acelasi numar de divizori
    :param lst: lista introdusa
    :return: returneaza subsecventa cea mai lunga care satisface proprietatea
    '''

    assert get_longest_same_div_count([2, 2, 2, 2]) == [2, 2, 2, 2]
    assert get_longest_same_div_count([0]) == [0]
    assert get_longest_same_div_count([1, 4, 9, 3, 5, 7, 9, 11]) == [3, 5, 7]

def get_longest_subarray_nr_palindrom(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa de numere care sunt palindrom
    :param lst: lista de numere intregi
    :return: returneaza cea mai lunga subsecventa de numere care respecta proprietatea
    '''

    n = len(lst)
    result = []
    for st in range (n):
        for dr in range (st, n):
            is_palindrome = True
            for num in lst[st: dr+1]:
                if num != numar_inversat(num):
                    is_palindrome = False
                    break
            if is_palindrome :
                if dr-st+1>len(result):
                    result = lst [st: dr+1]
    return result

def test_longest_subarray_nr_palindrom():
    '''
    Determina cea mai lunga subsecventa de numere care au proprietatea de palindrom
    :return: returneaza cea mai lunga subsecventa cu proprietatea ceruta
    '''
    assert get_longest_subarray_nr_palindrom([121, 122, 1331, 141, 234 ]) == [1331, 141]
    assert get_longest_subarray_nr_palindrom([1, 121, 41]) == [1, 121]
    assert get_longest_subarray_nr_palindrom([121, 1331, 23432, 454, 1551]) == [121, 1331, 23432, 454, 1551]

def main():
    lst = []
    while True:
        show_menu()
        optiune=input("Alege optiunea: ")
        if optiune == "1" :
            lst= read_list()
        elif optiune == "2" :
            palindromes = get_palindrom(lst)
            print('Numere palindrom din lista sunt: ', palindromes)
        elif optiune == "3" :
            print('Cea mai lunga subsecventa de numere palindrom este: ', get_longest_subarray_nr_palindrom(lst))
        elif optiune == "4" :
            print('Cea mai lunga subsecventa de numere cu acelasi numar de divizori este: ' , get_longest_same_div_count(lst))
        elif optiune == "x" :
            break
        else:
            print("Optiune invalida.")


if __name__ == '__main__':
    test_is_palindrome()
    test_longest_same_div_count()
    test_toate_nr_sunt_palindrom()
    test_numar_inversat()
    test_longest_subarray_nr_palindrom()
    main()
