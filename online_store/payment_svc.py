from time import sleep
from random import random


class PaymentService:
    @staticmethod
    def charge(self, user, total):
        sleep(0.5 + random())
        return "Transaction OK"
