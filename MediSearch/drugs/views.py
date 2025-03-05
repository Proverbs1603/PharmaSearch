from django.shortcuts import render
from .documents import DrugDocument
from elasticsearch_dsl import Q
from .models import Drug
from .search import search_drugs
from django.core.paginator import Paginator

def index(request):
    search_query = request.GET.get("q")  # 질의어 (검색 키워드)
    company_filter = request.GET.get("bssh_nm")  # 특허권 등재자 필터 값
    page = int(request.GET.get("page", 1))  # 기본값은 1
    page_size = int(request.GET.get("page_size", 10))  # 기본값은 10

    context = {}

    if search_query or company_filter:  # 검색 조건이 하나라도 있으면
        # drug_search 검색 객체 생성
        drug_search = search_drugs(
            query=search_query,
            company_filter=company_filter,
            page=page,
            page_size=page_size
        )
        # 검색 결과 컨텍스트에 저장
        context["drugs"] = drug_search.execute()
    else:
        #all_drugs = Drug.objects.all()
    
        # 검색 조건이 없으면 모든 데이터를 Elasticsearch로 페이지네이션하여 반환
        drug_search = search_drugs(
            page=page,
            page_size=page_size
        )
        context["drugs"] = drug_search.execute()

    # 특허권 등재자 목록을 가져와서 드롭다운 메뉴에 사용
    distinct_companies = Drug.objects.values('bssh_nm').distinct()
    context["bssh_nm_list"] = [entry['bssh_nm'] for entry in distinct_companies]

    return render(request, 'drugs/index.html', context)