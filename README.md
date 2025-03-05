# PharmaSearch

PharmaSearch는 의약품 및 특허 정보를 검색하고 필터링할 수 있는 웹 애플리케이션입니다. 사용자는 특정 성분명이나 특허권 등재자를 기준으로 의약품 데이터를 조회할 수 있습니다.

## 📌 프로젝트 실행 방법

### 1. 환경 설정

PharmaSearch는 Django와 Docker-compose를 기반으로 개발되었습니다. 따라서, 파이썬 환경과 docker-desktop을 미리 설치 후 아래의 단계를 따라 프로젝트를 실행할 수 있습니다.

- (맥 도커 설치) [https://docs.docker.com/desktop/setup/install/mac-install/](https://docs.docker.com/desktop/setup/install/mac-install/)
- (윈도우 도커 설치) [https://docs.docker.com/desktop/setup/install/windows-install/](https://docs.docker.com/desktop/setup/install/windows-install/)
- (파이썬 설치) [https://www.python.org/downloads/](https://www.python.org/downloads/)

#### 가상 환경 생성 및 활성화

```bash
# 파이썬 가상환경 생성
python -m venv bio-venv 

# 가상환경 활성화 (OS에 따라 선택)
source bio-venv/bin/activate  # macOS/Linux
bio-venv\Scripts\activate     # Windows
```

#### 필수 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 데이터베이스 마이그레이션

```bash
python manage.py migrate
```

### 3. 서버 실행

```bash
python manage.py runserver
```

Django 서버가 실행되면 브라우저에서 [http://127.0.0.1:8000/drugs](http://127.0.0.1:8000/drugs) 로 접속할 수 있습니다.

### 4. docker-compose로 Elasticsearch 서버 실행

```bash
docker compose up -d
```

Elasticsearch 서버가 실행되면 브라우저에서 [http://127.0.0.1:9200](http://127.0.0.1:9200) 로 접속할 수 있습니다.

### 5. 데이터 삽입 및 Elasticsearch 인덱스 생성
사이트에 접속 했을 때 데이터가 보인다면 데이터 삽입 과정은 생략하시면 됩니다.

- 데이터 삽입
```bash
cd MediSearch/data
python data.py
```

- Elasticsearch 인덱스 생성
```bash
cd ..
python manage.py search_index --rebuild
```

---

## 📊 데이터셋 설명
식품의약품안전처_의약품 국내 특허현황

데이터 소스 : https://www.data.go.kr/data/15117409/openapi.do#/API%20%EB%AA%A9%EB%A1%9D/getDrugDmstPtntStusService
[https://www.data.go.kr/data/15117409/openapi.do#/API%20%EB%AA%A9%EB%A1%9D/getDrugDmstPtntStusService](https://www.data.go.kr/data/15117409/openapi.do#/API%20%EB%AA%A9%EB%A1%9D/getDrugDmstPtntStusService)


PharmaSearch는 아래와 같은 주요 정보를 포함하는 데이터셋을 사용하며 726개의 데이터셋으로 이루어져있습니다.

| 컬럼명                | 설명      |
| ------------------ | ------- |
| `ptnt_no`          | 특허번호    |
| `ptnt_reg_dt`      | 등재일자    |
| `prdlst_nm`        | 제품명     |
| `drug_cpnt_kor_nm` | 한글 성분명  |
| `drug_cpnt_eng_nm` | 영문 성분명  |
| `bssh_nm`          | 특허권 등재자 |
| `pthd_nm`          | 등재 특허권자 |

---

## 🛠 주요 검색 기능

- **의약품 검색:** 제품명, 한글 성분명, 영어 성분명 기준 검색 가능
- **필터링 기능:** 특허권 등재자를 선택하여 필터링하여 검색 가능
- **페이지네이션 기능:** page와 page_size를 쿼리스트링으로 전달하여 페이지네이션 가능
- **영어성분명 자동완성 기능:** 검색창에 영어성분명에 해당하는 2글자 이상 입력시 추천 키워드를 5개 제공
- **동의어 검색 기능:** "큐록신정" 검색 시에 "타다라필" 도 동의어로 검색 가능 (실제 동의어는 아니고 임시로 지정해놓았습니다.)

---

## 🚀 API 엔드포인트

1️⃣ **약품 검색 API**
- **URL:** `/drugs`
- **Method:** `GET`
- **설명:** 사용자가 입력한 키워드를 기반으로 약품을 검색합니다.
- **쿼리 파라미터:**
  | 파라미터 | 타입 | 필수 여부 | 설명 |
  |---------|------|----------|-----|
  | `q` | `string` | ❌ | 검색 키워드 (약품명, 성분명) |
  | `bssh_nm` | `string` | ❌ | 제조사 필터 |
  | `page` | `int` | ❌ | 페이지 번호 (기본값: `1`) |
  | `page_size` | `int` | ❌ | 한 페이지에 표시할 결과 개수 (기본값: `20`) |

---
## 📌 개발 환경

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Javascript
- **Database:** SQLite3
- **Search Engine :** Elasticsearch
- **Tools/Deployment Environment :** Docker
---

## 👨‍💻 개발자

- **김신웅**

