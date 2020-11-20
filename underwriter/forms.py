from django import forms
from .models import InsureDetails,InsuredAddress,policyAgentCommision,policyVehicleDetails,policyRiskDetails,PolicyDetails,PolicyBills
from master.models import ProductRiskMaster
from master.models import VehicleMaster
from datetime import datetime,date, timedelta
month = {"1":"JAN","2":"FEB","3":"MAR","4":"APR","5":"MAY","6":"JUN","7":"JUL","8":"AUG","9":"SEP","10":"OCT","11":"NOV","12":"DEC"}

class InsuredDetailsForms(forms.ModelForm):

    insured_dob = forms.DateField(widget=forms.SelectDateWidget(months=month,years = range(1980,2050)))
    class Meta:
        model = InsureDetails
        fields='__all__'

        exclude=[
            'created_by','last_updated_by'
        ]


class InsuredAddressForm(forms.ModelForm):
    address_type = (
        ("","------"),
        ("T","Temporary"),
        ("P","Permanent")
    )
    class Meta:
        model=InsuredAddress

        fields="__all__"
        exclude=[
            'created_by','last_updated_by',"insured_id"
        ]

class policyDetailsForm(forms.ModelForm):
    policy_issued_date = forms.DateField(widget=forms.SelectDateWidget(),
                                         initial=date.today())

    start_date = forms.DateField(widget=forms.SelectDateWidget(),
                                 initial=date.today() + timedelta(days=1))
    end_date = forms.DateField(widget=forms.SelectDateWidget(),
                               initial=date.today() + timedelta(days=365))
    policy_status = (
        ('', '---------'),
        ('QUOTE', ("Quotation")),
        ('PAYMENTPENDING', ("Payment Pending")),
        ('INFORCE', ("Inforce")),
        ('LAPSE', ("Policy Lapse"))
    )
    payment_mode = (
        ('', '---------'),
        ('Q', ("Quartely")),
        ('H', ("Harl Yearly")),
        ('A', ("Annual"))
    )

    policy_status = forms.ChoiceField(choices=policy_status, required=False)
    payment_mode = forms.ChoiceField(choices=payment_mode, required=False)
    policy_no = forms.IntegerField(initial=PolicyDetails.objects.count() + 1)
    renewal_no = forms.IntegerField(initial=0)

    class Meta:
        model = PolicyDetails
        fields = '__all__'
        #[
        #     'policy_no',
        #     'insured_id',
        #     'prod_code',
        #     'agent_code',
        #     'policy_issued_date',
        #     'start_date',
        #     'end_date',
        #     'policy_status',
        #     'renewal_no',
        #     'payment_mode',
        #     'total_premium',
        #     'created_by',
        #     'last_updated_by'
        # ]

        exclude = ['created_by',
                   'last_updated_by']

class VehicleDtlsForm(forms.ModelForm):

    mfg_comp = VehicleMaster.objects.values_list('mfg_company_name',flat=True).distinct()
    mfg_comp_choices = [('', 'None')] + [(id, id) for id in mfg_comp]

    model_id = VehicleMaster.objects.values_list('model_id', flat=True).distinct()
    model_id_choices = [('', 'None')] + [(id, id) for id in model_id]

    model_name = VehicleMaster.objects.values_list('model_name', flat=True).distinct()
    model_name_choices = [('', 'None')] + [(id, id) for id in model_name]

    vehicle_make = forms.ChoiceField(choices=mfg_comp_choices, required=False, widget=forms.Select())
    vehicle_model_id = forms.ChoiceField(choices=model_id_choices, required=False, widget=forms.Select())
    vehicle_model_name = forms.ChoiceField(choices=model_name_choices, required=False, widget=forms.Select())

    class Meta:
        model = policyVehicleDetails
        fields = '__all__'
        #     [
        #     'policy_no',
        #     'vehicle_year',
        #     'vehicle_make',
        #     'vehicle_model_id',
        #     'vehicle_model_name',
        #     'chasis_number',
        #     'engine_number',
        #     'created_by',
        #     'last_updated_by'
        # ]

        exclude = ['policy_no','created_by',
                   'last_updated_by']

class PolicyRiskDtlsForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.SelectDateWidget(),
                                 initial=date.today()+timedelta(days=1))
    end_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = policyRiskDetails
        fields = '__all__'
        #     [
        #     'policy_no',
        #     'risk_code',
        #     'risk_description',
        #     'risk_SA',
        #     'risk_premium',
        #     'start_date',
        #     'end_date',
        #     'created_by',
        #     'last_updated_by'
        # ]

        exclude = ['policy_no','created_by','last_updated_by']

class PolicyBillsForm(forms.ModelForm):
    class Meta:
        model = PolicyBills
        fields = '__all__'
        #     [
        #     'bill_id',
        #     'policy_no',
        #     'premium_amount',
        #     'due_date',
        #     'balance_amount',
        #     'created_by',
        #     'last_updated_by'
        # ]
        exclude = ['created_by','last_updated_by']
