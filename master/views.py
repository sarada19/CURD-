from django.shortcuts import render,get_object_or_404
from .models import ProductMaster,ProductRiskMaster,AgentMaster,Agent_prod_comm_Master
from .forms import ProductMasterForm,ProductRiskForm,AgentCreateForm,AgentCommissionForm,VehicleMasterForm,\
    vehicleDepriciationForm,NCBMasterForm,ClaimStatusMasterForm,ClaimsSurveyorMasterForm
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
# Create your views here.

def master(request):
    return render(request,'Master/masterdata.html')

@login_required(login_url='/admin1/login/')
def ProductsMaster(request):
    pform = ProductMasterForm(request.POST or None)
    if pform.is_valid():
        form = pform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        pform = ProductMasterForm()
    context = {"pform":pform}
    return render(request,"Master/ProductMaster.html",context)

def ProductRisk(request):
    cformset = modelformset_factory(ProductRiskMaster,form=ProductRiskForm,extra =2,can_delete=True)
    formset = cformset(request.POST or None)
    if formset.is_valid():
        for form in formset.forms:
            if form['risk_code'].value() !="":
                for name,fields in form.fields.items():
                    tmpform = form.sve(commit=False)
                    setattr(tmpform,'created_by',str(request.user))
                    setattr(tmpform,'last_updated_by',str(request.user))
    context = {'formset':formset}
    return render(request,'Master/productRisk.html',context)



def AgentCreate(request):
    Aform = AgentCreateForm(request.POST or None)
    if Aform.is_valid():
        form = Aform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        Aform = AgentCreateForm()
    context = {'Aform':Aform}
    return render(request,'Master/Agentcreate.html',context)


def AgentCommission(request):
    cformset = modelformset_factory(Agent_prod_comm_Master,form=AgentCommissionForm,extra=2)
    formset = cformset(request.POST or None)
    if formset.is_valid():
        for form in formset.forms:
            print('agentform',form)
            if form['agent_id'].value() !="":
                for name,fields in form.fields.items():
                    print('name',name)
                    print('fields',fields)
                    tmpform = form.save(commit=False)
                    setattr(tmpform,'created_by',str(request.user))
                    setattr(tmpform,'last_updated_by',str(request.user))
                    tmpform.save()
    context = {'formset':formset}
    return render(request,'Master/AgentCommision.html',context)


def vehicleMasterView(request):
    vform = VehicleMasterForm(request.POST or None)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by=str(request.user)
        form.last_updated_by=str(request.user)
        form.save()
        vform = VehicleMasterForm()
    context = {'vform':vform}
    return render(request,'Master/vehiclemaster.html',context)


def vehicleDepreciationView(request):
    vform = vehicleDepriciationForm(request.POST or None)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by=str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = vehicleDepriciationForm()
    context = {'vform':vform}
    return render(request,'Master/vehicledepriciation.html',context)


def NCBMasterView(request):
    nform = NCBMasterForm(request.POST or None)
    if nform.is_valid():
        form = nform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        nform = NCBMasterForm()
    context = {'nform':nform}
    return render(request,'Master/ncbmaster.html',context)


def ClaimStatusMasterView(request):
    cform = ClaimStatusMasterForm(request.POST or None)
    if cform.is_valid():
        form = cform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        cform = ClaimStatusMasterForm()
    context = {'cform':cform}
    return render(request,'Master/claimstatus.html',context)


def ClaimsSurveyorMasterView(request):
    csform = ClaimsSurveyorMasterForm(request.POST or None)
    if csform.is_valid():
        form = csform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
    context = {'csform':csform}
    return render(request,'Master/claimsurveyor.html',context)























