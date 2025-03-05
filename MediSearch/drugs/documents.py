from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Drug

@registry.register_document
class DrugDocument(Document):
    prdlst_nm = fields.TextField(analyzer="korean_analyzer")
    drug_cpnt_kor_nm = fields.TextField(analyzer="korean_synonym_analyzer")  # 동의어 적용
    pthd_nm = fields.TextField(analyzer="korean_analyzer")

    class Index:
        name = "drugs"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
            "analysis": {
                "analyzer": {
                    "korean_analyzer": {  # 기본 한국어 분석기
                        "type": "custom",
                        "tokenizer": "nori_tokenizer",
                        "filter": ["lowercase"]
                    },
                    "korean_synonym_analyzer": {  # 동의어 적용 분석기
                        "type": "custom",
                        "tokenizer": "nori_tokenizer",
                        "filter": ["lowercase", "synonym_filter"]
                    }
                },
                "filter": {
                    "synonym_filter": {  # 동의어 필터
                        "type": "synonym",
                        "synonyms": [
                            "큐록신정, 타다라필",
                        ]
                    }
                }
            }
        }

    class Django:
        model = Drug
        fields = ["drug_cpnt_eng_nm", "ptnt_no", "ptnt_reg_dt"]