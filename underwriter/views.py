from django.shortcuts import render,redirect
from django.forms import modelformset_factory
from .forms import InsuredDetailsForms,InsuredAddressForm,policyDetailsForm,VehicleDtlsForm,PolicyRiskDtlsForm
from .models import InsureDetails,InsuredAddress,policyRiskDetails,PolicyDetails
from master.models import VehicleMaster
from django.db import transaction, IntegrityError
from .premiumCalc import motor_Risk_prem_calc
# Create your views here.

def underwriter(request):
    return render(request,'underwriter/underwriterdata.html')
def InsuredcreateView(request):
    context = {}
    InsuredAddrFormset = modelformset_factory(InsuredAddress, form=InsuredAddressForm,extra=2)
    Insuredform = InsuredDetailsForms(request.POST or None)
    formset = InsuredAddrFormset(request.POST or None)

    if request.method == "POST":
        if Insuredform.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    insured = Insuredform.save(commit=False)
                    print('12insured', insured.insured_id)
                    print('12insured', insured.insured_name)
                    insured.save()
                    for mark in formset:
                        data = mark.save(commit=False)
                        if not data.address_Type is None:
                            print('data.address_Type',data.address_Type)
                            print('data.insured_id', data.insured_id)
                            print('34insured',insured)
                            data.insured_id = insured
                            data.save()

            except IntegrityError:
                print("Error Encountered",IntegrityError.__name__)

    Insuredform = InsuredDetailsForms()
    formset = InsuredAddrFormset(queryset=InsuredAddress.objects.none())

    context = {
        "formset":formset,
        "form":Insuredform
    }
    #context['formset'] = formset
    #context['form'] = Insuredform
    return render(request, 'underwriter/InsuredCreate.html', context)

def PolicyCreateView(request):
    context = {}
    PolicyForm = policyDetailsForm(request.POST or None)
    VehicleForm = VehicleDtlsForm(request.POST or None)

    RiskFormset = modelformset_factory(policyRiskDetails, form=PolicyRiskDtlsForm, extra=3)
    formset = RiskFormset(request.POST or None)

    if request.method == "POST":

        if PolicyForm.is_valid():
            print(PolicyForm.cleaned_data)
            try:
                with transaction.atomic():
                    policy = PolicyForm.save(commit=False)
                    print('policy no:', policy.policy_no)
                    policy.created_by = str(request.user)
                    policy.last_updated_by = str(request.user)
                    policy.save()


                if VehicleForm.is_valid():
                    vehicle = VehicleForm.save(commit=False)
                    vehicle.created_by = str(request.user)
                    vehicle.last_updated_by = str(request.user)
                    print('vehicle data :', VehicleForm.cleaned_data)
                    vehicle.policy_no = policy
                    vehicle.created_by = str(request.user)
                    vehicle.last_updated_by = str(request.user)
                    print('No policy', vehicle.policy_no)
                    l_year =vehicle.vehicle_year
                    l_make = vehicle.vehicle_make
                    l_model = vehicle.vehicle_model_id
                    l_model_name = vehicle.vehicle_model_name
                    vehicle.save()

                l_tot_prem = 0
                if formset.is_valid():
                    for risk in formset:
                        data = risk.save(commit=False)
                        if not data.risk_code is None:
                            print('Riskcode', data.risk_code)
                            print('l_year',l_year)

                            data.policy_no = policy
                            data.created_by = str(request.user)
                            data.last_updated_by = str(request.user)
                            data.risk_description,data.risk_SA, data.risk_premium = \
                                motor_Risk_prem_calc(data.risk_code,l_year,l_make,l_model,l_model_name)
                            l_tot_prem = l_tot_prem + data.risk_premium
                            print('l_tot_prem',l_tot_prem)
                            policy.total_premium=l_tot_prem
                            data.save()
                print('l_tot_prem', l_tot_prem)
                policy.save()
            except IntegrityError as e:
                print("Error Encountered", e.__context__)

    PolicyForm = policyDetailsForm()
    VehicleForm = VehicleDtlsForm()
    formset = RiskFormset(queryset=policyRiskDetails.objects.none())

    context['Policyform'] = PolicyForm
    context['VehicleForm'] = VehicleForm
    context['PolicyRishForm'] = formset
    return render(request, 'underwriter/CreatePolicy.html', context)
