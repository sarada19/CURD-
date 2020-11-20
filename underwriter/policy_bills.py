from .models import PolicyBills,PolicyDetails
def Generate_invoice(policy_no,premium_amount,submit_user):

    obj = PolicyDetails.objects.get(policy_no=policy_no)

    PolicyBills.objects.create(policy_no=policy_no,
                                    premium_amount=premium_amount,
                                    created_by=str(submit_user),
                                    last_updated_by=str(submit_user),
                                    bill_id=PolicyBills.objects.count()+1
                                    )