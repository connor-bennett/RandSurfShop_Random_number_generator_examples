# Connor Bennett
# 02/ 25/23

"""
Hypothetical random number generator uses normal
and exponential distributions and numerical integration
"""


import random
import matplotlib
import numpy.random


class SurfShop:

    def __init__(self, name):
        self.name = None
        board = self.board()
        wettie = self.wettie()
        wax = self.wax()

    def board(self):
        boards = {0: "short board", 1: "mid-length", 2: "Log"}
        gen = random.randint(0, 2)
        my_board = boards[gen]
        return "Board style: " + my_board

    def wettie(self):
        suit_size = []
        m = numpy.random.randint(5)  # generate custom pdf essentially for num bought
        if m == 0:  # where 1 is much more likely others
            x = numpy.random.uniform(5, 10)
        elif 1 < m < 5:
            x = numpy.random.uniform(1)
        else:
            x = numpy.random.uniform(2, 5)

        wet_suits = ["small", "medium", "large"]
        num_bought = int(x)

        while len(suit_size) < num_bought:  # generate each size sold randomly
            suit_size.append(wet_suits[random.randint(0, 2)])

        return "Suits sold: " + str(num_bought) + '\n' + "Suit sizes: " + str(suit_size)

    def wax(self):
        temp_lst = ["cold", "warm", "tropical"]
        brand_lst = ["Sticky Bumps", "Zoggs", "Dana"]

        m = numpy.random.randint(3)  # generate custom pdf essentially for temp_lst
        if m == 0:  # where cold is twice as likely as the other two
            x = numpy.random.uniform(1, 3)
        else:
            x = numpy.random.uniform(0)

        temp = temp_lst[int(x)]
        brand = brand_lst[random.randint(0, 2)]  # generate random brand


        return "Brand: " + brand + '\n' + "Water temp: " + temp

    def individual_sales(self):
        return "Customer purchased: " + "\n" "________________________" + "\n" + self.board() + "\n" + self.wettie() + "\n" + self.wax()


if __name__ == "__main__":
    cons = SurfShop("me")
    print(cons.individual_sales())
