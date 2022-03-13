from time import sleep
from random import random


class PaymentException(Exception):
    pass

class PaymentService:
    fail = False

    @staticmethod
    def charge(user, total):
        if PaymentService.fail:
            raise PaymentException("Transaction FAILED")
        sleep(0.5 + random())
        return "Transaction OK"
