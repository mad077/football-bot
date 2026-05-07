import json
import os
import random
import time
from datetime import datetime

MEMORY_FILE = "memory.json"

TEAMS = [

    ("الهلال", "النصر"),
    ("برشلونة", "ريال مدريد"),
    ("مانشستر سيتي", "ليفربول"),
    ("ميلان", "يوفنتوس")

]

COMMENTS = [

    "واضح المباراة دخلت طور الجنون 🔥",
    "الدفاع اليوم بإجازة 😂",
    "الاستحواذ نار من الفريقين ⚽",
    "المباراة مفتوحة هجوميًا 👀"

]

PLAYERS = [

    "Ronaldo",
    "Neymar",
    "Messi",
    "Mbappe",
    "Vinicius"

]

# ====================================

def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return []

    try:

        with open(MEMORY_FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    except:

        return []

# ====================================

def save_memory(data):

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:

        json.dump(data, f, ensure_ascii=False, indent=4)

# ====================================

print("🚀 Dynamic Football Engine Running...\n")

while True:

    memory = load_memory()

    home, away = random.choice(TEAMS)

    home_score = random.randint(0, 4)

    away_score = random.randint(0, 4)

    possession = random.randint(45, 75)

    shots = random.randint(5, 20)

    corners = random.randint(1, 10)

    yellow_cards = random.randint(0, 5)

    minute = random.randint(1, 90)

    prediction = random.randint(50, 90)

    timeline = [

        f"⚽ {random.choice(PLAYERS)} {random.randint(1,90)}'",

        f"🟨 {random.choice(PLAYERS)} {random.randint(1,90)}'",

        f"⚽ {random.choice(PLAYERS)} {random.randint(1,90)}'"

    ]

    item = {

        "time": datetime.now().strftime("%H:%M:%S"),

        "home": home,

        "away": away,

        "home_score": home_score,

        "away_score": away_score,

        "possession": possession,

        "shots": shots,

        "corners": corners,

        "yellow_cards": yellow_cards,

        "minute": minute,

        "prediction": prediction,

        "timeline": timeline,

        "reply": random.choice(COMMENTS)

    }

    memory.append(item)

    memory = memory[-20:]

    save_memory(memory)

    print(f"⚽ {home} {home_score}-{away_score} {away}")

    time.sleep(10)