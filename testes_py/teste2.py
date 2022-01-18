from unittest import TestCase, main


def soma(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y

def par(val):
    return True if val % 2 == 0 else False

class Teste(TestCase):
    # def test_soma(self):
        # self.assertEqual(soma(5, 5), 10)


    # def soma2(self):
        # self.assertEqual(soma(5, 5), 11)

    # def mul2(self):
        # self.assertEqual(mul(5, 5), 25)
    def par(self):
        self.assertEqual(par('str'), True)
        self.assertEqual(par(7), False)


if __name__ == '__main__':
    main()
    
