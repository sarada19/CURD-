from .models import policyAgentCommision
from master.models import Agent_prod_comm_Master
def Generate_agent_commision(prod_code,policyno,agent_code,total_prem,submit_user):
    agentdata = Agent_prod_comm_Master.objects.get(prod_code=prod_code,
                                                         agen_id=agent_code)
    CommPercent = agentdata.comm_percent
    pol_agent_comm = (total_prem*CommPercent)/100
    print('agent comm:',prod_code,policyno,agent_code,total_prem,
          submit_user,agentdata.comm_percent,pol_agent_comm)
    policyAgentCommision.objects.create(agent_id=agent_code,
                                        policy_no=policyno,
                                        prod_code=prod_code,
                                        policy_comm=pol_agent_comm,
                                        created_by=str(submit_user),
                                        last_updated_by=str(submit_user)
                                        )