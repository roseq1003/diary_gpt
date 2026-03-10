import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve()  # 現在のファイル(init)の絶対パスを取得
while not (ROOT / ".git").exists():  # .gitが見つかるまで上の階層に遡る
    ROOT = ROOT.parent

DB_PATH = ROOT / "data" / "lifelog.db"

db = sqlite3.connect(DB_PATH)

for row in db.execute("SELECT * FROM metric"):
    print(row)

for row in db.execute("SELECT * FROM event"):
    print(row)
