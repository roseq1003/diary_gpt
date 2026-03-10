import sqlite3
from pathlib import Path

# パスの取得
ROOT = Path(__file__).resolve()  # 現在のファイル(init)の絶対パスを取得
while not (ROOT / ".git").exists():  # .gitが見つかるまで上の階層に遡る
    ROOT = ROOT.parent

# ROOTはdiary_gptになる。 ちなみにpathlib.Path は / を パス結合にしている
DB_PATH = ROOT / "data" / "lifelog.db"

# DB接続
db = sqlite3.connect(DB_PATH)

with open(ROOT / "src" / "diary_gpt" / "sql" / "schema.sql") as f:
    db.executescript(f.read())

db.commit()
db.close()

print("DB created")
