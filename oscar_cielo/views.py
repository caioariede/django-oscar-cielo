# encoding: UTF-8

from django.conf import settings

from oscar.apps.payment.models import SourceType, Source
from oscar.apps.checkout.views import PaymentDetailsView \
    as BasePaymentDetailsView

from oscar_cielo.mixins import CieloPaymentDetailsMixin


class CieloPaymentDetailsView(BasePaymentDetailsView,
                              CieloPaymentDetailsMixin):

    PROCESSED_STATUS = getattr(settings, 'OSCAR_CIELO_PROCESSED_STATUS',
                                         'Processado')

    def get_context_data(self, **kwargs):
        context = super(CieloPaymentDetailsView, self).get_context_data(
            **kwargs)
        context.update(self.get_cielo_context_data())

        return context

    def post(self, *args, **kwargs):
        self.handle_cielo_post(*args, **kwargs)
        return super(CieloPaymentDetailsView, self).post(*args, **kwargs)

    def handle_payment(self, order_number, total_incl_tax, **kwargs):
        attempt = self.capture_cielo_payment(order_number, total_incl_tax)
        transaction_id = attempt.transaction_id

        source_type, _ = SourceType.objects.get_or_create(name='Cielo')

        source = Source(
            source_type=source_type,
            currency='BRL',
            amount_allocated=total_incl_tax,
            amount_debited=total_incl_tax,
            reference=transaction_id,
        )

        self.add_payment_source(source)

    def place_order(self, *args, **kwargs):
        order = super(CieloPaymentDetailsView, self).place_order(*args,
                                                                 **kwargs)
        order.set_status(self.PROCESSED_STATUS)

        return order
