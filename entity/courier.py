from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.request import Request


class Courier:
    def __int__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.__request = request

        self.departure: AbstractStorage = storages[self.__request.departure]
        self.destination: AbstractStorage = storages[self.__request.destination]

    def move(self):
        self.departure.remove(name=self.__request.product, amount=self.__request.amount)
        print(f"Курьер забирает {self.__request.amount} {self.__request.product} из {self.__request.departure}")

        print(
            f"Курьер везет {self.__request.amount} {self.__request.product} "
            f"со {self.__request.departure} в {self.__request.destination}"
        )

        self.destination.add(name=self.__request.product, amount=self.__request.amount)
        print(f"Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}")

    # def cancel(self):
    #     print("Доставка отменена")
