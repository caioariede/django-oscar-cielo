from oscar.app import Shop as BaseShop

from .apps.checkout.app import custom_checkout_app


class Shop(BaseShop):
    checkout_app = custom_checkout_app


shop = application = Stop()
