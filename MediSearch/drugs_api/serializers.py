from rest_framework import serializers
from drugs.models import Drug

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = [
            'id', 
            'ptnt_prdlst_crtr_cd', 
            'prdlst_nm', 
            'drug_cpnt_kor_nm', 
            'drug_cpnt_eng_nm', 
            'bssh_nm', 
            'pthd_nm', 
            'ptnt_reg_dt', 
            'ptnt_no'
        ]