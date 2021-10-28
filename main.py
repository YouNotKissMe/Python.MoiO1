from math import e, pi, sqrt
import sys
from tabulate import tabulate

sys.setrecursionlimit(1500)

class dichotomy:
    def __init__(self, start, end, epsilan, const):
        self.start = start
        self.end = end
        self.epsilan = epsilan
        self.const = const
        self.n = 1

    def startiteration(self):
        betta = None
        alfa = None
        if (self.end - self.start) <= self.epsilan:
            peremen = (self.start + self.end) / 2
            BabaZina = 2 * peremen ** 2 - e ** peremen
            print(f'МЕТОД ПОЛОВИННОГО ДЕЛЕНИЯ\n'
                  f'{peremen}'
                  f'[{self.start};{self.end}]'
                  f'На поиск решения было потраченно: {self.n} итераци\n'
                  f'Окончательный ответ f(x*)={BabaZina}')
        else:
            alfa = (self.start + self.end) / 2 - self.const
            betta = (self.start + self.end) / 2 + self.const
            if (2 * alfa ** 2 - e ** alfa) < \
                    (2 * betta ** 2 - e ** betta):
                self.end = betta
                self.n += 1

                dichotomy.startiteration(self)
            else:
                self.start = alfa
                self.n += 1

                dichotomy.startiteration(self)


class gold():
    def __init__(self, start, end, epsilan):
        self.start = start
        self.end = end
        self.epsilan = epsilan
        self.n = 1
        self.l = (sqrt(5) - 1) / 2
        self.alfa = self.start + (1 - self.l) * (self.end - self.start)
        self.betta = self.start + self.l * (self.end - self.start)

    def goldenratio(self):

        if (self.end - self.start) < self.epsilan:
            peremen = (self.start + self.end) / 2
            BabaZina = (2 * peremen ** 2 - e ** peremen)
            print(f'МЕТОД ЗОЛОТОГО СЕЧЕНИЯ\n'
                  f'{peremen}'
                  f'[{self.start};{self.end}]'
                  f'На поиск решения было потраченно: {self.n} итераци\n'
                  f'Окончательный ответ f(x*)={BabaZina}')
        else:
            if (2 * self.alfa ** 2 - e ** self.alfa) > \
                    (2 * self.betta ** 2 - e ** self.betta):

                #m = self.start
                self.start = self.alfa
                self.alfa = self.betta
                self.betta = self.start + self.l * (self.end - self.start)
                self.n += 1
                #print('!!!!')
                gold.goldenratio(self)
            else:
                self.end = self.betta
                self.betta = self.alfa
                self.alfa = self.start + (1 - self.l) * (self.end - self.start)
                self.n += 1
                #print('&&&')
                gold.goldenratio(self)


class fibonacci:

    def __init__(self, start, end, epsilan, const):
        self.start = start
        self.end = end
        self.epsilan = epsilan
        self.const = const
        self.k = 1
        self.__bibanacci = bibanacci
        for i in range(len(self.__bibanacci)):
            if self.__bibanacci[i] > (self.end-self.start):
                self.n = i
                break
        self.alpha = self.start + self.__bibanacci[self.n - 2] / self.__bibanacci[self.n] * \
                     (self.end - self.start)
        self.betta = self.start + self.__bibanacci[self.n - 1] / self.__bibanacci[self.n] * \
                     (self.end - self.start)
    def starbibanacci(self):
        if 2 * self.alpha ** 2 - e ** self.alpha >= 2 * self.betta ** 2 - e ** self.betta:
            self.start = self.alpha
            self.alpha = self.betta
            sss = self.betta
            # -------------------------------------
            self.betta = self.start + self.__bibanacci[self.n - self.k - 2] / \
                         self.__bibanacci[self.n - self.k] * \
                         (self.end - self.start)

            if self.k == self.n - 2:

                self.alpha = self.start
                ss = self.start
                self.betta = self.alpha + self.const
                if 2 * self.alpha ** 2 - e ** self.alpha == 2 \
                        * self.betta ** 2 - e ** self.betta:
                    self.start = self.alpha
                    peremen = (self.start + self.end) / 2
                    BabaZina = 2 * peremen ** 2 - e ** peremen
                    print(f'МЕТОД ФИБОНАЧЧИ\n'
                          f'{peremen}'
                          f'[{self.start};{self.end}]'
                          f'На поиск решения было потраченно: {self.n} итераци\n'
                          f'Окончательный ответ f(x*)={BabaZina}')
                else:
                    self.end = self.betta
                    peremen = (self.start + self.end) / 2
                    BabaZina = 2 * peremen ** 2 - e ** peremen
                    print(f'МЕТОД ФИБОНАЧЧИ\n'
                          f'{peremen}'
                          f'[{self.start};{self.end}]'
                          f'На поиск решения было потраченно: {self.n} итераци\n'
                          f'Окончательный ответ f(x*)={BabaZina}')
            else:
                self.k += 1
                fibonacci.starbibanacci(self)

        else:
            self.end = self.betta
            sss = self.betta
            self.betta = self.alpha
            self.alpha = self.start + self.__bibanacci[self.n - self.k - 2] / \
                         self.__bibanacci[self.n - self.k] * \
                         (self.end - self.start)

            if self.k == self.n - 2:

                self.alpha = self.start
                ss = self.start
                self.betta = self.alpha + self.const
                if 2 * self.alpha ** 2 - e ** self.alpha == 2 \
                        * self.betta ** 2 - e ** self.betta:
                    self.start = self.alpha
                    peremen = (self.start + self.end) / 2
                    BabaZina = 2 * peremen ** 2 - e ** peremen
                    print(f'МЕТОД ФИБОНАЧЧИ\n'
                          f'{peremen}'
                          f'[{self.start};{self.end}]'
                          f'На поиск решения было потраченно: {self.n} итераци\n'
                          f'Окончательный ответ f(x*)={BabaZina}')
                else:
                    self.end = self.betta
                    peremen = (self.start + self.end) / 2
                    BabaZina = 2 * peremen ** 2 - e ** peremen
                    print(f'МЕТОД ФИБОНАЧЧИ\n'
                          f'итоговый x = {peremen}\n'
                          f'[{self.start};{self.end}]'
                          f'На поиск решения было потраченно: {self.n} итераци\n'
                          f'Окончательный ответ f(x*)={BabaZina}')
            else:
                self.k += 1
                fibonacci.starbibanacci(self)

    def get_bibanacci(self):
        return self.__bibanacci


dichotomy(-2, 2, 0.001, 0.0004).startiteration()

print('\n')
gold(-2, 2, 0.001).goldenratio()


def fiba(a):
    if len(bibanacci) < 1300:
        bibanacci.append(bibanacci[len(bibanacci) - 1]+bibanacci[len(bibanacci) - 2])
        fiba(bibanacci)


bibanacci = [1,1]
fiba(bibanacci)
print('\n')
fibonacci(-2,2,0.0001,0.00004).starbibanacci()