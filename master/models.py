from django.db import models
from datetime import datetime
from django.conf import settings
#from dateutil.relativedelta import relativedelta
from django.urls import reverse

# Create your models here.
class AgentMaster(models.Model):
    agent_id = models.CharField(max_length=15,primary_key = True)
    agent_name = models.CharField(max_length=50,null=True,blank=True)
    agent_dob = models.DateField(blank=True,null=True)
    agent_age = models.IntegerField(blank=True
                                    ,null=True)
    agent_qualification = models.CharField(max_length=100,blank=True,null=True)
    agent_join_date = models.DateField(blank=True,null=True,auto_now_add=False)#auto_now_add =True
    agent_start_date = models.DateField(blank=True,null=True)
    agent_end_date = models.DateField(blank=True,null=True)
    agent_status = models.CharField(max_length=20,blank=True,null=True)
    created_by = models.CharField(max_length=200,blank=True,null=True).hidden
    created_date = models.DateField(null=True,blank=True)
    last_updated_by = models.CharField(max_length=150,null=True,blank=True).hidden
    last_updated_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.agent_id

    def get_agent_age(self):
        return int(((datetime.date.today()-self.agent_dob).days)/365.25)

    def get_unique_id(self):
        a = self.agent_name[:2].upper() #First Two letters
        b = self.agent_dob.strftime('%d') #Day of the month as string
        c = self.agent_qualification[:2].upper() #first two letters of qualification
        d = "AGC-"
        return d+a+b+c

    def save(self,*args,**kwargs):
        self.agent_id = self.get_unique_id
        self.agent_age = self.get_agent_age
        self.created_date = datetime.today()
        self.last_updated_date = datetime.today()
        super(AgentMaster,self).save(*args,**kwargs)

class ProductMaster(models.Model):
    prod_code = models.CharField(primary_key=True,max_length=20)
    prod_description = models.CharField(max_length=250,blank=True,null=True)
    prod_start_date = models.DateField(blank=True,null=True)
    prod_end_date = models.DateField(blank=True,null=True)
    created_by = models.CharField(max_length=150,null=True,blank=True)
    created_date = models.DateField(blank=True,null=True)
    last_updated_by = models.CharField(max_length=150,blank=True,null=True)
    last_updated_date = models.DateField(blank=True,null=True)


    def save(self):
        if not self.prod_code:
            self.created_date = datetime.today()
            self.last_updated_date = datetime.today()
        super(ProductMaster,self).save()

    def __str__(self):
        return self.prod_code


class ProductRiskMaster(models.Model):
    risk_code = models.CharField(primary_key=True,max_length=120)
    prod_code = models.ForeignKey(ProductMaster,models.DO_NOTHING,db_column='prod_code',blank=True,null=True)
    risk_description = models.CharField(max_length=500,blank=True,null=True)
    risk_premium_percent = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    risk_start_date = models.DateField(null=True,blank=True)
    risk_end_date = models.DateField(blank=True,null=True)
    created_by = models.CharField(max_length=150,blank=True,null=True)
    created_date = models.DateField(blank=True,null=True)
    last_updated_by = models.CharField(max_length=150,blank=True,null=True)
    last_updated_date = models.DateField(blank=True,null=True)
    prem_calc_method = models.CharField(max_length=100,blank=True,null=True)
    fixed_premium = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    fixed_si = models.BigIntegerField(blank=True,null=True)


    def __str__(self):
        return self.risk_code

    def save(self,*args,**kwargs):
        self.created_date = datetime.today()
        self.last_updated_date = datetime.today()
        super(ProductRiskMaster,self).save(*args,**kwargs)


class Agent_prod_comm_Master(models.Model):
    agent_id = models.ForeignKey(AgentMaster,models.DO_NOTHING,blank=False,null=False)
    prod_code = models.ForeignKey(ProductMaster,models.DO_NOTHING,blank=False,null=False,db_column='prod_code')
    comm_percent = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    created_by = models.CharField(max_length = 200,blank = True,null=True)
    created_date = models.DateField(blank=True,null=True)
    last_updated_by = models.CharField(max_length=200,blank=True,null=True)
    last_updated_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.prod_code
    def save(self):
        if not self.agent_id:
            self.created_date = datetime.today()
            self.last_updated_date = datetime.today()
            self.created_by = settings.AUTH_USER_MODEL
            self.last_updated_by = settings.AUTH_USER_MODEL
        super(Agent_prod_comm_Master,self).save()


class VehicleMaster(models.Model):
    mfg_company_name = models.CharField(max_length=200,blank=True,null=True)
    model_id = models.CharField(unique=True,max_length=20)
    model_name = models.CharField(max_length=100,blank=True,null=True)
    engine_cubic_capacity = models.CharField(max_length=100,blank=True,null=True)
    insured_declared_value = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    created_by = models.CharField(max_length=200,blank=True,null=True)
    created_date = models.DateField(blank=True,null=True,default=datetime.now)
    last_updated_by = models.CharField(max_length=200,blank=True,null=True)
    last_updated_date = models.DateField(blank=True,null=True,default=datetime.now)

    def __str__(self):
        return self.model_id

    def save(self,*args,**kwargs):
        self.created_date =datetime.today()
        self.last_updated_date = datetime.today()
        super(VehicleMaster,self).save(*args,**kwargs)

class VehicleDepriciation(models.Model):
    vehicle_age_from = models.IntegerField(blank=True, null=True)
    vehicle_age_to = models.IntegerField(blank=True, null=True)
    dep_percent_on_idv = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_date = datetime.today()
        self.last_update_date = datetime.today()
        super(VehicleDepriciation, self).save(*args, **kwargs)

class NCBMaster(models.Model):
    prod_code = models.ForeignKey(ProductMaster,models.DO_NOTHING,db_column='prod_code',blank=True,null=True)
    no_of_years_from = models.BigIntegerField(blank=True,null=True)
    no_of_years_to = models.BigIntegerField(blank=True,null=True)
    discount_on_premium = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    discount_desc =models.CharField(max_length=200,blank=True,null=True)
    created_by = models.CharField(max_length=100,blank=True,null=True)
    created_date = models.DateField(blank=True,null=True)
    last_updated_by = models.CharField(max_length=100,blank=True,null=True)
    last_updated_date = models.DateField(blank=True,null=True)

    # def __str__(self):
    #     return self.prod_code
    #

    def save(self,*args,**kwargs):
        self.created_date = datetime.today()
        self.last_updated_date = datetime.today()
        super(NCBMaster,self).save(*args,**kwargs)


class ClaimStatusMaster(models.Model):
    clm_status_code = models.CharField(unique=True, max_length=200)
    clm_status_desc = models.CharField(max_length=2000, blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.clm_status_code

    def get_absolute_url(self):
        return reverse('MasterSetup:claimStatusMaster', kwargs={"id": self.id})

    def save(self, *args, **kwargs):
        self.created_date = datetime.today()
        self.last_update_date = datetime.today()
        super(ClaimStatusMaster, self).save(*args, **kwargs)

class ClaimsSurveyorMaster(models.Model):
    surveyor_id = models.IntegerField(primary_key=True)
    surveyor_name = models.CharField(max_length=200, blank=True, null=True)
    surveyor_qualificaition = models.CharField(max_length=200, blank=True, null=True)
    surveyor_brach_code = models.CharField(max_length=200, blank=True, null=True)
    surveyor_city = models.CharField(max_length=200, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_date = datetime.today()
        self.last_update_date = datetime.today()
        super(ClaimsSurveyorMaster, self).save(*args, **kwargs)












