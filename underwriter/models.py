from django.db import models
from datetime import datetime
# Create your models here.
class  InsureDetails(models.Model):
    insured_id =models.CharField(primary_key=True,max_length=20)
    insured_name = models.CharField(max_length=100,blank=True,null=True)
    insured_dob = models.DateField(blank=True,null=True)
    insured_qualification = models.CharField(max_length=100,blank=True,null=True)
    insured_profission = models.CharField(max_length=200,blank=True,null=True)
    insured_addr_code = models.IntegerField(blank=True,null=True)
    insured_phone_no = models.BigIntegerField(blank=True,null=True)
    insured_email = models.EmailField(blank=True,null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.insured_id

    def save(self, *args, **kwargs):
        self.created_date = datetime.today()
        self.last_update_date = datetime.today()
        super(InsureDetails, self).save(*args, **kwargs)

class InsuredAddress(models.Model):
    insured_addr_id = models.IntegerField(primary_key=True)
    insured_id = models.ForeignKey(InsureDetails,models.DO_NOTHING,db_column='insured_id',blank=True,null=True)
    address_type= models.CharField(max_length=200,blank=True,null=True)
    insured_addr=models.CharField(max_length=200,null=True,blank=True)
    insured_city = models.CharField(max_length=20,null=True,blank=True)
    insured_state = models.CharField(max_length=200,null=True,blank=True)
    insured_country = models.CharField(max_length=20,blank=True,null=True)
    insured_pincode = models.IntegerField(blank=True,null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.insured_id

    def save(self,*args,**kwargs):
        self.created_date = datetime.today()
        self.last_updated_date = datetime.today()
        super(InsuredAddress,self).save(*args,**kwargs)

class PolicyDetails(models.Model):
    policy_no = models.IntegerField(primary_key=True)
    insured_id=models.ForeignKey('InsureDetails',models.DO_NOTHING,blank=True,null=True)
    prod_code = models.ForeignKey('master.ProductMaster',models.DO_NOTHING,db_column='prod_code',blank=True,null=True)
    agent_code = models.ForeignKey('master.AgentMaster',models.DO_NOTHING,db_column='agent_id',blank=True,null=True)
    policy_issued_date = models.DateField(blank=True,null=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    policy_status = models.CharField(max_length=20,blank=True,null=True)
    renewal_no = models.BigIntegerField(blank=True,null=True)
    payment_mode = models.CharField(max_length=30,blank=True,null=True)
    total_premium = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)

    def __int__(self):
        return self.policy_no

    def save(self, *args, **kwargs):
        self.created_date = datetime.today()
        self.last_update_date = datetime.today()
        super(PolicyDetails, self).save(*args, **kwargs)


class policyRiskDetails(models.Model):

    policy_risk_id = models.IntegerField(primary_key=True)
    policy_no =models.ForeignKey(PolicyDetails,models.DO_NOTHING,db_column='policy_no',blank=True,null=True)
    risk_code = models.ForeignKey('master.ProductRiskMaster',models.DO_NOTHING,blank=True,null=True)
    risk_description = models.CharField(max_length=100,blank=True,null=True)
    risk_SA = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    risk_premium = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.risk_code

    def save(self, *args, **kwargs):
        self.created_date = datetime.today()
        self.last_update_date = datetime.today()
        super(policyRiskDetails, self).save(*args, **kwargs)

class policyVehicleDetails(models.Model):
    policy_no = models.IntegerField(blank=True)
    vehicle_year = models.IntegerField(blank=True, null=True)
    vehicle_make = models.CharField(max_length=200, blank=True, null=True)
    vehicle_model_id = models.CharField(max_length=200, blank=True, null=True)
    vehicle_model_name = models.CharField(max_length=200, blank=True, null=True)
    chasis_number = models.CharField(max_length=200, blank=True, null=True)
    engine_number = models.BigIntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)

    def __int__(self):
        return self.policy_no

    def save(self, *args, **kwargs):
        self.created_date = datetime.today()
        self.last_update_date = datetime.today()
        super(policyVehicleDetails, self).save(*args, **kwargs)

class policyAgentCommision(models.Model):
    policy_no = models.IntegerField(blank=True)
    agent_id = models.CharField(max_length=120, blank=True, null=True)
    prod_code = models.CharField(max_length=200, blank=True, null=True)
    policy_comm = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)

class PolicyBills(models.Model):
    bill_id = models.AutoField(primary_key=True)
    # policy_no = models.ForeignKey('XxgenPolicyDtls', models.DO_NOTHING, db_column='policy_no', blank=True, null=True)
    policy_no = models.IntegerField(blank=True)
    premium_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    balance_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    created_by = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    last_update_date = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=200, blank=True, null=True)





