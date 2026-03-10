import sqlite3
import sys
from datetime import datetime
from pathlib import Path

# パス取得君
ROOT = Path(__file__).resolve()  # 現在のファイル(init)の絶対パスを取得
while not (ROOT / ".git").exists():  # .gitが見つかるまで上の階層に遡る
    ROOT = ROOT.parent

# ROOTはdiary_gptになる。 ちなみにpathlib.Path は / を パス結合にしている
DB_PATH = ROOT / "data" / "lifelog.db"

db = sqlite3.connect(DB_PATH)

cmd = sys.argv[1]

if cmd == "metric":
    name = sys.argv[2]
    value = float(sys.argv[3])
    unit = sys.argv[4] if len(sys.argv) > 4 else None

    db.execute(
        "INSERT INTO metric (time,name,value,unit) VALUES (?,?,?,?)",
        (datetime.now().isoformat(), name, value, unit)
    )
    print(f"saved metric: {name}={value} {unit}")

if cmd == "event":
    text = " ".join(sys.argv[2:])

    db.execute(
        "INSERT INTO event (time,type,text) VALUES (?,?,?)",
        (datetime.now().isoformat(), "diary", text)
    )

    print(f"saved event: {text}")

db.commit()
db.close()
