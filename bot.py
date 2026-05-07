import time
import json
import random
import requests
from datetime import datetime

# ====================================
# API
# ====================================

API_KEY = ""

# ====================================
# TELEGRAM
# ====================================

TELEGRAM_TOKEN = ""

CHAT_ID = ""

# ====================================
# FILE
# ====================================

MEMORY_FILE = "memory.json"

# ====================================
# تحميل البيانات
# ====================================

def load_memory():

    try:

        with open(MEMORY_FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    except:

        return []

# ====================================
# حفظ البيانات
# ====================================

def save_memory(data):

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:

        json.dump(data, f, ensure_ascii=False, indent=4)

# ====================================
# TELEGRAM
# ====================================

def send_notification(message):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    requests.post(url, data={

        "chat_id": CHAT_ID,

        "text": message

    })

# ====================================
# المباريات المباشرة
# ====================================

def get_live_matches():

    url = "https://api.football-data.org/v4/matches"

    headers = {

        "X-Auth-Token": API_KEY

    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return data.get("matches", [])

# ====================================
# AI تعليق ذكي
# ====================================

def generate_comment(home, away, home_score, away_score):

    if home_score > away_score:

        return f"واضح {home} مسيطر على المباراة اليوم 🔥"

    elif away_score > home_score:

        return f"{away} داخل المباراة بثقة كبيرة 😅"

    else:

        comments = [

            f"مباراة {home} و {away} مشتعلة تكتيكيًا 👀",

            f"واضح الفريقين داخلين بحذر شديد 😅",

            f"الجماهير تنتظر هدف يفك الاشتباك 😂"

        ]

        return random.choice(comments)

# ====================================
# START
# ====================================

print("🚀 Live Football System Running...\n")

send_notification("🔥 نظام المباريات المباشرة يعمل الآن")

memory = load_memory()

# حفظ آخر النتائج
LAST_SCORES = {}

# ====================================
# LOOP
# ====================================

while True:

    try:

        matches = get_live_matches()

        for match in matches:

            home = match["homeTeam"]["name"]

            away = match["awayTeam"]["name"]

            status = match["status"]

            if status != "LIVE":
                continue

            home_score = match["score"]["fullTime"]["home"]

            away_score = match["score"]["fullTime"]["away"]

            # معالجة None

            if home_score is None:
                home_score = 0

            if away_score is None:
                away_score = 0

            match_key = f"{home}-{away}"

            current_score = f"{home_score}-{away_score}"

            # إذا تغيرت النتيجة = هدف جديد

            if LAST_SCORES.get(match_key) != current_score:

                LAST_SCORES[match_key] = current_score

                comment = generate_comment(

                    home,
                    away,
                    home_score,
                    away_score

                )

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                item = {

                    "time": now,

                    "event": f"{home} {home_score}-{away_score} {away}",

                    "reply": comment

                }

                memory.append(item)

                save_memory(memory)

                print(f"⚽ {home} {home_score}-{away_score} {away}")

                print(f"🤖 {comment}")

                print("-" * 50)

                # إشعار الجوال

                send_notification(

                    f"🔥 هدف أو تحديث جديد!\n\n⚽ {home} {home_score}-{away_score} {away}\n\n🤖 {comment}"

                )

                time.sleep(5)

    except Exception as e:

        print("❌ ERROR:", e)

    time.sleep(60)