# encoding: UTF-8

from oscar.apps.checkout.views import PaymentDetailsView \
    as BasePaymentDetailsView

from oscar_cielo.mixins import CieloPaymentDetailsMixin


class CieloPaymentDetailsView(BasePaymentDetailsView,
                              CieloPaymentDetailsMixin):
    def handle_payment(self, order_number, total_incl_tax, **kwargs):
        self.handle_cielo_payment(order_number, total_incl_tax)

    def get_context_data(self, **kwargs):
        context = super(CieloPaymentDetailsView, self).get_context_data(**kwargs)
        context.update(self.get_cielo_context_data())

        return context

    def post(self, *args, **kwargs):
        self.handle_cielo_post(*args, **kwargs)
        return super(CieloPaymentDetailsView, self).post(*args, **kwargs)
