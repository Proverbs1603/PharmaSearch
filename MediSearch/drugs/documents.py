from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Drug

@registry.register_document
class DrugDocument(Document):
    prdlst_nm = fields.TextField(analyzer="korean_analyzer")
    drug_cpnt_kor_nm = fields.TextField(analyzer="korean_synonym_analyzer")  # 동의어 적용
    pthd_nm = fields.TextField(analyzer="korean_analyzer")
    drug_cpnt_eng_nm = fields.TextField(analyzer="ngram_analyzer")
    bssh_nm = fields.TextField(
        fields = {
            "raw" : {
                "type" : 'keyword'
            }
        }
    )

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
                    },
                    "ngram_analyzer": {    # n-gram 분석기
                        "type": "custom",
                        "tokenizer": "ngram_tokenizer",
                        "filter": ["lowercase"]
                    }
                },
                "tokenizer": {
                    "ngram_tokenizer": { # n-gram 토크나이저 설정
                        "type": "ngram",
                        "min_gram": 2,
                        "max_gram": 3,
                        "token_chars": ["letter", "digit"]
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
        fields = ["ptnt_no", "ptnt_reg_dt"]