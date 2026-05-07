from flask import Flask, render_template_string
import json
import os
from collections import Counter

app = Flask(__name__)

MEMORY_FILE = "memory.json"

# ====================================
# قراءة البيانات
# ====================================

def load_data():

    if not os.path.exists(MEMORY_FILE):

        return []

    try:

        with open(MEMORY_FILE, "r", encoding="utf-8") as f:

            return json.load(f)

    except:

        return []

# ====================================
# الصفحة الرئيسية
# ====================================

@app.route("/")
def home():

    data = load_data()

    # ترتيب عكسي

    data = data[::-1]

    latest = data[:20]

    # تحليل الأحداث

    events = [x["event"] for x in data]

    counts = Counter(events)

    labels = list(counts.keys())[:5]

    values = list(counts.values())[:5]

    cards = ""

    for item in latest:

       cards += f"""

<div class="relative overflow-hidden
bg-gradient-to-br from-gray-900 via-gray-800 to-black
p-6 rounded-3xl shadow-2xl border border-gray-700
hover:border-green-400 transition duration-300">

    <!-- LIVE -->

    <div class="absolute top-4 left-4
    bg-red-500 text-white px-3 py-1 rounded-full
    text-sm font-bold animate-pulse shadow-lg">

        🔴 LIVE

    </div>

    <!-- Time -->

    <div class="absolute top-4 right-4 text-gray-400 text-sm">

        ⏰ {item.get("time","")}

    </div>

    <!-- Teams -->

    <div class="grid grid-cols-3 items-center text-center mt-8">

        <!-- Team 1 -->

        <div>

            <img
            src="https://cdn-icons-png.flaticon.com/512/53/53283.png"
            class="w-16 mx-auto mb-3 opacity-80">

            <h2 class="text-2xl font-bold">

                {item.get("event","").split(" vs ")[0] if "vs" in item.get("event","") else item.get("event","")}

            </h2>

        </div>

        <!-- Score -->

        <div>

            <div class="text-6xl font-extrabold text-green-400 animate-pulse">

                2 - 1

            </div>

            <div class="mt-3 text-yellow-400 font-bold">

                ⚽ هدف 78'

            </div>

        </div>

        <!-- Team 2 -->

        <div>

            <img
            src="https://cdn-icons-png.flaticon.com/512/53/53283.png"
            class="w-16 mx-auto mb-3 opacity-80">

            <h2 class="text-2xl font-bold">

                {item.get("event","").split(" vs ")[1] if "vs" in item.get("event","") else ""}

            </h2>

        </div>

    </div>

    <!-- Stats -->

    <div class="grid grid-cols-2 gap-4 mt-8">

        <!-- Possession -->

        <div class="bg-gray-950 p-4 rounded-2xl border border-gray-800">

            <p class="text-gray-400 mb-2">
                📈 الاستحواذ
            </p>

            <div class="w-full bg-gray-700 rounded-full h-4 overflow-hidden">

                <div class="bg-green-400 h-4 rounded-full"
                style="width:65%"></div>

            </div>

            <p class="mt-2 text-sm text-gray-300">
                65%
            </p>

        </div>

        <!-- Cards -->

        <div class="bg-gray-950 p-4 rounded-2xl border border-gray-800">

            <p class="text-gray-400 mb-2">
                🟨 البطاقات
            </p>

            <div class="text-2xl">

                🟨 🟨 🟥

            </div>

        </div>

    </div>

    <!-- AI Comment -->

    <div class="bg-black/40 backdrop-blur-lg
    p-5 rounded-2xl border border-gray-700 mt-6">

        <p class="text-lg text-gray-200 leading-8">

            🤖 {item.get("reply","")}

        </p>

    </div>

    <!-- Goal Animation -->

    <div class="absolute -bottom-8 -right-8 text-[120px] opacity-10 animate-bounce">

        ⚽

    </div>

</div>


        """

    html = f"""

<!DOCTYPE html>

<html lang="ar" dir="rtl">

<head>

<meta charset="UTF-8">

<title>⚽ Live VAR Dashboard</title>

<!-- تحديث تلقائي -->

<meta http-equiv="refresh" content="5">

<!-- PWA -->

<meta name="theme-color" content="#111827">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="manifest" href="/manifest.json">

<!-- Tailwind -->

<script src="https://cdn.tailwindcss.com"></script>

<!-- Chart -->

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

</head>

<body class="bg-gray-950 text-white min-h-screen p-6">

<div class="max-w-7xl mx-auto">

<!-- Header -->

<div class="flex justify-between items-center mb-8">

    <div>

        <h1 class="text-5xl font-bold text-green-400">
            ⚽ Live VAR Dashboard
        </h1>

        <p class="text-gray-400 mt-2">
            غرفة أخبار رياضية مباشرة
        </p>

    </div>

    <div class="bg-green-500 text-black px-4 py-2 rounded-full font-bold shadow-lg animate-pulse">
        🟢 LIVE
    </div>

</div>

<!-- Popup -->

<div class="fixed top-5 left-1/2 -translate-x-1/2 bg-green-500 text-black px-6 py-3 rounded-2xl shadow-2xl animate-bounce">

🔥 يتم تحديث البيانات مباشرة

</div>

<!-- Stats -->

<div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">

    <div class="bg-gray-900 p-5 rounded-2xl shadow-lg">

        <p class="text-gray-400">
            إجمالي الأحداث
        </p>

        <h2 class="text-4xl text-green-400 mt-2 font-bold">
            {len(data)}
        </h2>

    </div>

    <div class="bg-gray-900 p-5 rounded-2xl shadow-lg">

        <p class="text-gray-400">
            آخر مباراة
        </p>

        <h2 class="text-2xl mt-2">
            {latest[0]["event"] if latest else "لا يوجد"}
        </h2>

    </div>

    <div class="bg-gray-900 p-5 rounded-2xl shadow-lg">

        <p class="text-gray-400">
            حالة النظام
        </p>

        <h2 class="text-2xl text-green-400 mt-2">
            🟢 يعمل
        </h2>

    </div>

</div>

<!-- Chart -->

<div class="bg-gray-900 p-6 rounded-2xl shadow-lg mb-8">

    <h2 class="text-2xl mb-4 text-green-400">
        📊 أكثر المباريات نشاطًا
    </h2>

    <canvas id="chart"></canvas>

</div>

<!-- Live Feed -->

<div>

    <h2 class="text-3xl mb-4 text-green-400 font-bold">
        ⚽ البث المباشر
    </h2>

    <div class="grid gap-4">

        {cards}

    </div>

</div>

</div>

<!-- Chart Script -->

<script>

const ctx = document.getElementById('chart');

new Chart(ctx, {{

    type: 'bar',

    data: {{

        labels: {labels},

        datasets: [{{
            label: 'عدد الأحداث',
            data: {values},
        }}]

    }}

}});

</script>

</body>

</html>

"""

    return render_template_string(html)

# ====================================
# Manifest PWA
# ====================================

@app.route("/manifest.json")
def manifest():

    return {{

        "name": "VAR Dashboard",

        "short_name": "VAR",

        "start_url": "/",

        "display": "standalone",

        "background_color": "#111827",

        "theme_color": "#22c55e"

    }}

# ====================================
# تشغيل السيرفر
# ====================================

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)