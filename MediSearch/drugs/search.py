from .documents import DrugDocument
from elasticsearch_dsl import Q

def search_drugs(
        query: str = None,
        company_filter: str = None,
        page: int = 1,
        page_size: int = 20
):

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

    # 페이지네이션 계산
    from_ = (page - 1) * page_size

    # 검색 쿼리 실행 및 정렬 설정
    return DrugDocument.search().query(q).extra(from_=from_,size=page_size)


#영어 성분명 자동완성 검색 (최대 5개 자동완성 추천)
def auto_complete_drug_eng(query: str, size: int = 5):
    if not query:
        return []

    # n-gram 필드에서 자동완성 검색
    q = Q("match_phrase_prefix", drug_cpnt_eng_nm=query) 
    return DrugDocument.search().query(q).extra(size=size)