from master.models import ProductRiskMaster,VehicleMaster,VehicleDepriciation
import datetime

def motor_Risk_prem_calc(mycode,vehicle_year,make,model_id,model_name):
    now = datetime.datetime.now()
    curyear = now.year
    obj = ProductRiskMaster.objects.get(risk_code=mycode)
    risk_desc = obj.risk_description
    if obj.prem_calc_method == 'F':
        risk_prem = obj.fixed_prem
        risk_sa = obj.fixed_si
    if obj.prem_calc_method == 'P':

        vobj = VehicleMaster.objects.get(mfg_company_name=make,model_id=model_id,model_name=model_name)
        print('vehiclebject', vobj)
        vehicle_age = curyear - vehicle_year
        print('vehicle_age', vehicle_age)
        #vdep = XxgenVehicleDepriciation.objects.filter(vehicle_age_from__gte=vehicle_age,vehicle_age_to__lte=vehicle_age)
        vdep = VehicleDepriciation.objects.get(vehicle_age_from=vehicle_age)
        print('vehicle_dep_percet', vdep.vehicle_age_from,vdep.vehicle_age_from)

        vehicle_dep_percet = vdep.dep_percent_on_idv
        print('vehicle_dep_percet', vehicle_dep_percet)
        print('new vehicle value :',vobj.insured_declared_value)
        vehicle_dep_value = (vobj.insured_declared_value*vehicle_dep_percet)/100
        vehicle_currrent_value = vobj.insured_declared_value-vehicle_dep_value
        print('vehicle_currrent_value', vehicle_currrent_value)
        risk_prem = (vehicle_currrent_value*obj.risk_premium_percent)/100
        risk_sa = vehicle_currrent_value
    return risk_desc,risk_sa, risk_prem