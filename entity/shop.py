from typing import Dict

from entity.base_storage import BaseStorage
from exceptions import TooManyDifferentProductsError


class Shop(BaseStorage):

    def __init__(self, items: Dict[str, int], capasity: int, max_unique_items: int):
        """

        :rtype: object
        """
        self.__max_unique_items = max_unique_items
        super().__init__(items, capasity)

    def add(self, name: str, amount: int) -> None:
        if self.get_unique_items_count() >= self.__max_unique_items:
            raise TooManyDifferentProductsError

        super().add(name, amount)
