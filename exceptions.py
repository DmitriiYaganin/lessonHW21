class BaseError(Exception):
    message = 'Что-то пошло не так'


class NotEnoughSpaceError(BaseError):
    message = 'Недостаточно места'


class NotEnoughProductError(BaseError):
    message = 'Недостаточно товара'


class TooManyDifferentProductsError(BaseError):
    message = 'Слишком много разных товаров'


class InvalidRequestError(BaseError):
    message = 'Неправильный запрос'


class UnknownStorageError(BaseError):
    message = 'Не известный склад'
