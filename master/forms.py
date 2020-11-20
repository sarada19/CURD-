from django import forms
from master.models import AgentMaster,ProductMaster,ProductRiskMaster,Agent_prod_comm_Master,\
    VehicleMaster,VehicleDepriciation,NCBMaster,ClaimStatusMaster,ClaimsSurveyorMaster
import datetime
# class AgentForm(forms.ModelForm):
#     class Meta:
#         model = AgentMaster
#         fields = "__all__"



class ProductMasterForm(forms.ModelForm):
    prod_start_date = forms.DateField(widget=forms.SelectDateWidget(),initial=datetime.date.today())
    prod_end_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model=ProductMaster
        fields = [
            'prod_code',
            'prod_description',
            'prod_start_date',
            'prod_end_date',
            'created_by',
            'last_updated_by'
        ]
        exclude=[
            'created_by',
            'last_updated_by'
        ]


    def clean_prod_code(self,*args,**kwargs):
        data = self.cleaned_data['prod_code']
        print("product data",data)
        if not data.isupper():
            raise forms.ValidationError("Prod code should be in Upper case")
        if '@' in data or "*" in data or "|" in data:
            raise forms.ValidationError("Prod code should not have special character")
        if len(data)<5:
            self._errors['prod_code'] = self.error_class(["Minimum 5 characters required"])

        return data

    def clean(self):
        super(ProductMasterForm,self).clean()
        prod_desc = self.cleaned_data.get('prod_description')
        if len(prod_desc)<10:
            self._errors['prod_description'] = self.error_class(["Product Description is not less than 10 Characters"])
        return self.cleaned_data


class ProductRiskForm(forms.ModelForm):

    cal_method = (
        ("","--------"),
        ("F","Fixed"),
        ("P","Percentage")
    )
    risk_start_date = forms.DateField(widget=forms.SelectDateWidget(),required=False)
    risk_end_date = forms.DateField(widget=forms.SelectDateWidget(),required=False)
    risk_code = forms.CharField(widget=forms.TextInput(attrs={"size":10}),required=True)
    risk_description  = forms.CharField(widget=forms.TextInput(attrs={"size":10}),required=True)
    risk_premium_percent = forms.DecimalField(required=False)
    prem_calc_method = forms.ChoiceField(choices=cal_method,required=False)

    class Meta:
        model = ProductRiskMaster
        fields=[
            'prod_code',
            'risk_code',
            'risk_description',
            'risk_premium_percent',
            'risk_end_date',
            'risk_start_date',
            'fixed_premium',
            'fixed_si',
            'created_by',
            'last_updated_by'
        ]
        exclude=[
            'created_by','last_updated_by'
        ]
    def clean_risk_code(self,*args,**kwargs):
        data = self.cleaned_data['risk_code']
        if not data.isupper():
            raise forms.ValidationError("risk_code code should be in upper case")
        if "@" in data or "*" in data or "|" in data:
            raise forms.ValidationError("risk_code code should not contain @,*,|")
        if len(data) < 5 :
            self._errors['risk_code']=self.error_class(["Minimum 5 charcters required"])
        return data
    def clean_risk_premium_percent(self,*args,**kwargs):
        data = self.cleaned_data['risk_premium_percent']
        if data is None:
            print("is none")
        else:
            if data>100:
                raise forms.ValidationError("Premium percent should not exceed 100")
        return data

    def clean(self):
        super(ProductRiskForm,self).clean()
        risk_desc = self.cleaned_data.get('risk_description')
        calmethod = self.cleaned_data.get('prem_calc_method')

        if calmethod == "F":
            if self.cleaned_data.get('fixed_premium')==""or self.cleaned_data.get('fixed_premium') or None:
                self._errors['fixed_premium'] = self.error_class([
                    "Fixed premium should not be null when premium calc method is fixed"
                ])
            if self.cleaned_data.get("fixed_si") == "" or self.cleaned_data.get("fixed_si") or None:
                self._errors['fixed_si'] = self.error_class([
                    "Fixed si should not be null when premium calc method is percntage"
                ])
        elif calmethod == "P":
            print('percent',self.cleaned_data.get('risk_premium_percent'))
            if self.cleaned_data.get("risk_premium_percent") is None:
                self._errors["risk_premium_percent"]=self.error_class([
                    "risk_premium_percent should not be null When premium  calc method is percentage"
                ])
        return self.cleaned_data

class AgentCreateForm(forms.ModelForm):
    agent_checkbox=[
        ('Active','Active'),
        ('Deactive','Deactive')
    ]
    month = {'jan':'jan','feb':'feb','mar':'mar','apr':'apr','may':'may','jun':'jun','jul':'jul','aug':'aug',
             'sep':'sep','oct':'oct','nov':'nov','dec':'dec'}
    agent_dob = forms.DateField(widget=forms.SelectDateWidget(months=month,years=range(1980,2030)))
    agent_start_date = forms.DateField(widget=forms.SelectDateWidget(months=month))
    agent_end_date = forms.DateField(widget=forms.SelectDateWidget(months=month),required=False)
    agent_status = forms.ChoiceField(choices=agent_checkbox,required=False)
    class Meta:
        model = AgentMaster

        fields = [
            'agent_id',
            'agent_age',
            'agent_name',
            'agent_dob',
            'agent_qualification',
            'agent_join_date',
            'agent_end_date',
            'agent_start_date',
            'agent_status',
            'created_by',
            'last_updated_by'
        ]
        exclude=[
            'agent_id','agent_age','created_by','last_updated_by'
        ]

class AgentCommissionForm(forms.ModelForm):
    class Meta:
        model = Agent_prod_comm_Master
        fields = [
            'agent_id',
            'prod_code',
            'comm_percent',
            'created_by',
            'last_updated_by'
        ]
        exclude = [
            'created_by','last_updated_by'
        ]

class VehicleMasterForm(forms.ModelForm):

    class Meta:
        model= VehicleMaster

        fields = [
            'mfg_company_name',
            'model_id',
            'model_name',
            'engine_cubic_capacity',
            'insured_declared_value',
            'created_by',
            'last_updated_by'
        ]
        exclude=[
            'created_by','last_updated_by'
        ]

class vehicleDepriciationForm(forms.ModelForm):
    class Meta:
        model=VehicleDepriciation
        fields=[
            'vehicle_age_from',
            'vehicle_age_to',
            'dep_percent_on_idv',
            'created_by',
            'last_updated_by'
        ]
        exclude=[
            'created_by','last_updated_by'
        ]


class NCBMasterForm(forms.ModelForm):
    class Meta:
        model = NCBMaster

        fields=[
            'prod_code',
            'no_of_years_from',
            'no_of_years_to',
            'discount_on_premium',
            'discount_desc',
            'created_by',
            'last_updated_by'
        ]
        exclude = [
            'created_by','last_updated_by'
        ]


class ClaimStatusMasterForm(forms.ModelForm):
    class Meta:
        model =ClaimStatusMaster
        fields = [
            'clm_status_code',
            'clm_status_desc',
            'created_by',
            'last_updated_by'
        ]
        exclude = [
            'created_by','last_updated_by'
        ]

class ClaimsSurveyorMasterForm(forms.ModelForm):
    class Meta:
        model = ClaimsSurveyorMaster
        fields='__all__'
        #     [
        #     'surveyor_id',
        #     'surveyor_name',
        #     'surveyor_city',
        #     'surveyor_qualificaition',
        #     'surveyor_brach_code'
        #     'phone',
        #     'created_by',
        #     'last_updated_by'
        # ]
        exclude = [
            'created_by','last_updated_by','surveyor_id'
        ]



























