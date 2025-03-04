from django.shortcuts import render
from .documents import DrugDocument
from elasticsearch_dsl.query import MultiMatch

def index(request):
    q = request.GET.get("q")
    context = {}
    if q:
        query = MultiMatch(query=q, fields=["prdlst_nm", "drug_cpnt_kor_nm", "drug_cpnt_eng_nm", "bssh_nm", "pthd_nm"])
        s = DrugDocument.search().query(query)
        context["drugs"] = s
    return render(request, 'drugs/index.html', context)