from .documents import DrugDocument
from elasticsearch_dsl import Q

def search_drugs(
        query: str = None,
        company_filter: str = None,
        page: int = 1,
        page_size: int = 10
):
    """
    Elasticsearch에서 약품 검색 및 Django Paginator와 연동
    """

    # 기본 검색 쿼리 설정
    if query:
        q = Q(
            "bool",
            should=[
                Q("match_phrase", prdlst_nm=query),
                Q("match", drug_cpnt_kor_nm=query),
                Q("match", drug_cpnt_eng_nm=query),
            ],
            minimum_should_match=1
        )
    else:
        q = Q("match_all")  # query가 없을 경우 전체 검색

    # 필터 조건 설정
    filters = []

    if company_filter:
        # 특허권 등재자 필터링
        filters.append(Q("term", bssh_nm__raw=company_filter))

    # 필터를 bool 쿼리에 추가
    if filters:
        q = Q("bool", must=[q], filter=filters)

    # 페이지네이션을 위한 size 계산
    size = page_size

    # 검색 쿼리 실행 및 정렬 설정
    return DrugDocument.search().query(q).extra(size=size)


#영어 성분명 자동완성 검색 (최대 5개 자동완성 추천)
def auto_complete_drug_eng(query: str, size: int = 5):
    if not query:
        return []

    q = Q("match_phrase_prefix", drug_cpnt_eng_nm=query) # n-gram 필드에서 자동완성 검색
    return DrugDocument.search().query(q).extra(size=size)