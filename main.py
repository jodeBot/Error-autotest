## catching different error messages

def otaluku():
    luku = input('Anna lukuarvo:\t')
    return luku

def main():
    luku1 = otaluku()
    luku2 = otaluku()
    try:
        tulos = int(luku1) /int(luku2)
    except ZeroDivisionError:
        print('Nollalla ei voi jakaa.')

    except (TypeError, ValueError):
        print('Kirjaimilla ei voi laskea.')
    else:
        print('Tulos on ', tulos)

if __name__ == '__main__':
    main()