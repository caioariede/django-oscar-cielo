from oscar_cielo.views import CieloPaymentDetailsView


class PaymentDetailsView(CieloPaymentDetailsView):
    def handle_payment(self, order_number, total_incl_tax, **kwargs):
        super(PaymentDetailsView, self).handle_payment(
            order_number, total_incl_tax, **kwargs)

        self.add_payment_event('Aprovado', total_incl_tax)
