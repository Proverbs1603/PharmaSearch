import pandas as pd
import requests

# CSV 파일 경로
csv_file = "./의약품_국내_특허현황.csv"

# pandas로 CSV 파일 읽고 정제하기
df = pd.read_csv(csv_file, encoding='euc-kr') 
df = df.drop(columns=['No'], errors='ignore') 
df = df.drop(columns=['rownum'], errors='ignore')  
df = df.where(pd.notna(df), None)


# 컬럼 이름에서 공백과 대괄호 제거 후, 모델의 컬럼 이름으로 수정
df = df.rename(columns={
    '품목일련번호 [PTNT_PRDLST_CRTR_CD] ': 'ptnt_prdlst_crtr_cd',
    '제품명 [PRDLST_NM] ': 'prdlst_nm',
    '주성분명 [DRUG_CPNT_KOR_NM] ': 'drug_cpnt_kor_nm',
    '주성분명(영문) [DRUG_CPNT_ENG_NM] ': 'drug_cpnt_eng_nm',
    '특허권등재자 [BSSH_NM] ': 'bssh_nm',
    '등재특허권자 [PTHD_NM] ': 'pthd_nm',
    '등재일자 [PTNT_REG_DT] ': 'ptnt_reg_dt',
    '특허번호 [PTNT_NO] ': 'ptnt_no'
})

print(len(df))


# 데이터 삽입
# API 엔드포인트
api_url = "http://127.0.0.1:8000/rest/drugs/"

# 데이터 삽입
for _, row in df.iterrows():
    data = {
        "ptnt_prdlst_crtr_cd": row["ptnt_prdlst_crtr_cd"],
        "prdlst_nm": row["prdlst_nm"],
        "drug_cpnt_kor_nm": row["drug_cpnt_kor_nm"],
        "drug_cpnt_eng_nm": row["drug_cpnt_eng_nm"],
        "bssh_nm": row["bssh_nm"],
        "pthd_nm": row["pthd_nm"],
        "ptnt_reg_dt": row["ptnt_reg_dt"],
        "ptnt_no": row["ptnt_no"]
    }
    
    response = requests.post(api_url, json=data)
    
    if response.status_code == 201:
        print(f"✅ 성공: {row['prdlst_nm']}")
    else:
        print(f"❌ 실패: {row['prdlst_nm']} - {response.text}")
