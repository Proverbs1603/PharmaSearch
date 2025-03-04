from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Drug

@registry.register_document
class DrugDocument(Document):
    class Index:
        name = "drugs"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Drug
        fields = ["prdlst_nm", "drug_cpnt_kor_nm", "drug_cpnt_eng_nm", "bssh_nm", "pthd_nm", "ptnt_no", "ptnt_reg_dt"]