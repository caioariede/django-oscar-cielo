from django.utils.formats import number_format
from django.utils.translation import ugettext_lazy as _

from oscar.apps.checkout.forms import *
from oscar.apps.payment.forms import BankcardForm

from cielo import PaymentAttempt


CARD_TYPE_CHOICES = (
    (PaymentAttempt.VISA, 'Visa'),
    (PaymentAttempt.MASTERCARD, 'Mastercard'),
    (PaymentAttempt.DINERS, 'Diners'),
    (PaymentAttempt.DISCOVER, 'Discover'),
    (PaymentAttempt.ELO, 'ELO'),
    (PaymentAttempt.AMEX, 'American Express'),
)


class CieloForm(BankcardForm):
    class Meta(BankcardForm.Meta):
        fields = (
            'name', 
            'card_type',
            'number',
            'expiry_month',
            'cvv_number',
            'installments',
        )

    name = forms.CharField(max_length=128, label=_("Name on card"))
    card_type = forms.ChoiceField(choices=CARD_TYPE_CHOICES)
    installments = forms.ChoiceField(choices=())

    number_of_installments = 3

    def __init__(self, order_total, *args, **kwargs):
        super(CieloForm, self).__init__(*args, **kwargs)

        del self.fields['start_month']

        # Needed to calculate installments
        self._order_total = order_total

        installments_choices = []

        for installment in range(1, self.number_of_installments+1):
            installment_label = self.get_installment_label(
                installment,
                order_total / installment,
            )
            installments_choices.append((installment, installment_label))

        self.fields['installments'].choices = installments_choices

    def get_installment_label(self, installment, value):
        return '%dx de R$%s (s/ juros)' % (
            installment,
            number_format(value, decimal_pos=2),
        )


class HiddenCieloForm(CieloForm):
    card_type = forms.ChoiceField(widget=forms.HiddenInput,
                                  choices=CARD_TYPE_CHOICES)
    name = forms.CharField(widget=forms.HiddenInput)
    number = forms.CharField(widget=forms.HiddenInput)
    expiry_month = forms.DateField(widget=forms.HiddenInput)
    cvv_number = forms.CharField(widget=forms.HiddenInput)
    installments = forms.ChoiceField(widget=forms.HiddenInput, choices=())
