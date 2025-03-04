from django.shortcuts import render
from .documents import DrugDocument
from elasticsearch_dsl import Q
from .models import Drug


def index(request):
    q = request.GET.get("q") #질의어  
    bssh_nm_filter = request.GET.get("bssh_nm") #특허권 등재자 필터 값
    context = {}
    query = None
    result = None
    
    # 키워드 검색 (q가 있을 경우)
    if q:
        query = Q("multi_match", query=q, fields=["prdlst_nm", "drug_cpnt_kor_nm", "drug_cpnt_eng_nm", "bssh_nm", "pthd_nm"]) | \
                Q("match_phrase", prdlst_nm=q) | \
                Q("term", drug_cpnt_eng_nm=q)
        result = DrugDocument.search().query(query)
    
    # bssh_nm 필터가 있을 경우 (특허권 등재자 기준으로 필터링)
    if bssh_nm_filter:
        filter_query = Q("term", bssh_nm=bssh_nm_filter)
        if result:  # 기존에 검색된 결과가 있으면 필터 추가
            result = result.filter(filter_query)
        else:  # 결과가 없다면 필터만 적용
            result = DrugDocument.search().filter(filter_query)


    context["drugs"] = result
    if result:
        for r in result:
            print(r)
    

    # 특허권 등재자 목록을 가져와서 드롭다운 메뉴에 사용
    unique_bssh_nm = Drug.objects.values('bssh_nm').distinct()
    context["bssh_nm_list"] = [entry['bssh_nm'] for entry in unique_bssh_nm]

    return render(request, 'drugs/index.html', context)