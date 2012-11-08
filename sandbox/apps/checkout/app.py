from oscar.apps.checkout import app

from .views import PaymentDetailsView


class CheckoutApplication(app.CheckoutApplication):
    payment_details_view = PaymentDetailsView


shop = application = CheckoutApplication()
