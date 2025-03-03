from django.db import models

class Drug(models.Model): 
    ptnt_prdlst_crtr_cd = models.CharField(max_length=10)      #품목일련번호
    prdlst_nm = models.TextField()                             #제품명
    drug_cpnt_kor_nm = models.TextField(null=True, blank=True) #주성분명 (한글)
    drug_cpnt_eng_nm = models.TextField(null=True, blank=True) #주성분명 (영문)
    bssh_nm = models.TextField(null=True, blank=True)          #특허권등재자
    pthd_nm = models.TextField(null=True, blank=True)          #등재특허권자
    ptnt_reg_dt = models.DateTimeField(auto_now_add=True)      #등재일자
    ptnt_no = models.CharField(max_length=20)                  #특허번호
