from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Drug

@registry.register_document
class DrugDocument(Document):
    prdlst_nm = fields.TextField(analyzer="korean_analyzer")
    bssh_nm = fields.TextField(analyzer="korean_analyzer")
    drug_cpnt_kor_nm = fields.TextField(analyzer="korean_analyzer")
    pthd_nm = fields.TextField(analyzer="korean_analyzer")

    class Index:
        name = "drugs"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
            "analysis": {
                "analyzer": {
                    "korean_analyzer": {
                        "type": "custom",
                        "tokenizer": "nori_tokenizer",
                        "filter": ["lowercase"]
                    }
                }
            }
        }

    class Django:
        model = Drug
        fields = ["drug_cpnt_eng_nm", "ptnt_no", "ptnt_reg_dt"]