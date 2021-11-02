# sqlite 연동 등..

import sqlite3  # 기본으로 설치되어있음.

print("sqlite3 version : ", sqlite3.version)
print("sqlite3.sqlite_engine version : ", sqlite3.sqlite_version)

# 생성
conn = sqlite3.connect("blabla.db", isolation_level=None)
# isolation_level  -> auto_commit

# Cursor -> 마우스 커서처럼 생각하면 됨 첫번째 데이터에 커서를 둔다고 생각하면된다.
c = conn.cursor()
print('Cursor Type: ', type(c))

# 테이블 생성(Data Type: TEXT, NUMERIC INTEGER:정수 REAL:소숫점 BLOB:파일
c.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text,"
    " email text, phone text, website text, regdate text)")

# 데이터 삽입

c.execute("insert into users(id, username, email, phone, website, regdate) values (?,?,?,?,?,?)",
          (1, "Kim", "kim@naver.com", "01011-213-12-312-31", "kim.com", "asdf"))

# 이런식으로 값을 받아서 넘기는것도 가능 ?로 값을 넘겨줌
# key binding
# c.exectuemany -> 튜플 혹은 리스트의 array 형태로 여러 데이터를 넘겨 줄 수 있다.

# 접속해제
# c.close()


# 지정 로우 선택
print(c.fetchone())  # 1개만
print(c.fetchmany(size=2))  # 2개만
print(c.fetchall())  # 전부

# 순회
for row in c.fetchall():
    print(row)

# sql key binding
# "%s",(string)
# :DICT, {"ID": 5}

# Dump 출력
# iterdump
with conn:
    with open("path", "w") as f:
        for line in conn.iterdump():
            f.write(line + "\n")
        print("dump done")


# 이하 CRUD 명령어
