#def print_formatted(number):
#        for i in range(0,number):
#        x = "{0:d} {0:o} {0:X} {0:b}".format(i)
#        print(n)

#if __name__ == '__main__':
#    n = int(input())
#    print_formatted(n)

def print_formatted(number):
    x = "{0:b}".format(number)
    for i in range(1,number+1):
        dec = "{0:d}".format(i)
        dec = "{:>{space}}".format(dec, space=len(x))
        oct = "{0:o}".format(i)
        oct = "{:>{space}}".format(oct, space=len(x))
        hex = "{0:X}".format(i)
        hex = "{:>{space}}".format(hex, space=len(x))
        bin = "{0:b}".format(i)
        bin = "{:>{space}}".format(bin, space=len(x))
        n = dec + ' ' + oct + ' ' + hex + ' ' + bin
        print(n)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)