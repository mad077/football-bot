from flask import Flask, render_template_string
import json
import os
import random

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

    data = load_data()[::-1]

    latest = data[:20]

    cards = ""

    for item in latest:

        possession = random.randint(45, 75)

        prediction = random.randint(55, 90)

        cards += f"""

<div class="relative overflow-hidden
bg-gradient-to-br from-gray-900 via-gray-800 to-black
p-6 rounded-3xl shadow-2xl border border-gray-700
hover:border-green-400 transition duration-300
animate-fadeIn mb-6"

style="
background-image:url('https://images.unsplash.com/photo-1547347298-4074fc3086f0');
background-size:cover;
background-position:center;
background-blend-mode:overlay;
">

    <!-- Overlay -->

    <div class="absolute inset-0 bg-black/70"></div>

    <!-- Content -->

    <div class="relative z-10">

        <!-- LIVE -->

        <div class="absolute top-0 left-0
        bg-red-500 text-white px-4 py-2 rounded-full
        text-sm font-bold animate-pulse shadow-lg">

            🔴 LIVE

        </div>

        <!-- Time -->

        <div class="absolute top-0 right-0 text-gray-300 text-sm">

            ⏰ {item.get("time","")}

        </div>

        <!-- Match -->

        <div class="grid grid-cols-3 items-center text-center mt-12">

            <!-- Team 1 -->

            <div>

                <img
                src="https://cdn-icons-png.flaticon.com/512/53/53283.png"
                class="w-20 mx-auto mb-3 opacity-90">

                <h2 class="text-3xl font-extrabold text-white">

                    {item.get("event","").split(" vs ")[0] if "vs" in item.get("event","") else item.get("event","")}

                </h2>

            </div>

            <!-- SCORE -->

            <div>

                <div class="text-7xl font-black text-green-400 animate-pulse drop-shadow-lg">

                    2 - 1

                </div>

                <!-- Goal Explosion -->

                <div class="relative mt-4">

                    <div class="text-yellow-400 font-black text-2xl animate-ping absolute inset-0">

                        ⚽ GOAL!

                    </div>

                    <div class="text-yellow-400 font-black text-2xl relative">

                        ⚽ GOAL 78'

                    </div>

                </div>

            </div>

            <!-- Team 2 -->

            <div>

                <img
                src="https://cdn-icons-png.flaticon.com/512/53/53283.png"
                class="w-20 mx-auto mb-3 opacity-90">

                <h2 class="text-3xl font-extrabold text-white">

                    {item.get("event","").split(" vs ")[1] if "vs" in item.get("event","") else ""}

                </h2>

            </div>

        </div>

        <!-- Possession -->

        <div class="mt-8 bg-black/40 p-5 rounded-2xl border border-gray-700">

            <div class="flex justify-between text-sm mb-2 text-white">

                <span>📈 الاستحواذ</span>

                <span>{possession}%</span>

            </div>

            <div class="w-full bg-gray-700 h-5 rounded-full overflow-hidden">

                <div class="bg-green-400 h-5 animate-pulse rounded-full"
                style="width:{possession}%"></div>

            </div>

        </div>

        <!-- Timeline -->

        <div class="mt-8 bg-black/40 backdrop-blur-lg
        rounded-2xl p-5 border border-gray-700">

            <h3 class="text-green-400 text-xl font-bold mb-4">

                ⚽ Goals Timeline

            </h3>

            <div class="space-y-3 text-white">

                <div class="flex justify-between items-center">

                    <span class="text-green-400 font-bold">
                        ⚽ Ronaldo
                    </span>

                    <span>
                        12'
                    </span>

                </div>

                <div class="flex justify-between items-center">

                    <span class="text-yellow-400 font-bold">
                        🟨 Militao
                    </span>

                    <span>
                        44'
                    </span>

                </div>

                <div class="flex justify-between items-center">

                    <span class="text-green-400 font-bold">
                        ⚽ Neymar
                    </span>

                    <span>
                        78'
                    </span>

                </div>

            </div>

        </div>

        <!-- AI Prediction -->

        <div class="mt-6 bg-green-500/20 border border-green-400
        p-5 rounded-2xl">

            <h3 class="text-green-400 font-bold text-xl mb-2">

                🧠 AI Prediction

            </h3>

            <p class="text-white text-lg">

                🔥 فرصة الفوز: {prediction}%

            </p>

        </div>

        <!-- AI Comment -->

        <div class="bg-black/50 mt-6 p-5 rounded-2xl
        border border-gray-700">

            <p class="text-lg text-gray-200 leading-8">

                🤖 {item.get("reply","")}

            </p>

        </div>

        <!-- Animated Ball -->

        <div class="absolute -bottom-8 -right-8
        text-[140px] opacity-10 animate-bounce">

            ⚽

        </div>

    </div>

</div>

"""

    html = f"""

<!DOCTYPE html>

<html lang="ar" dir="rtl">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>⚽ Live VAR Dashboard</title>

<meta http-equiv="refresh" content="5">

<script src="https://cdn.tailwindcss.com"></script>

<style>

body {{
    font-family: sans-serif;
}}

@keyframes fadeIn {{

    from {{
        opacity: 0;
        transform: translateY(20px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}

}}

.animate-fadeIn {{

    animation: fadeIn 0.8s ease;

}}

</style>

</head>

<body class="bg-black text-white min-h-screen p-6">

<div class="max-w-7xl mx-auto">

    <!-- Header -->

    <div class="flex justify-between items-center mb-10">

        <div>

            <h1 class="text-5xl font-black text-green-400">

                ⚽ Live VAR Dashboard

            </h1>

            <p class="text-gray-400 mt-2">

                منصة رياضية مباشرة مدعومة بالذكاء الاصطناعي

            </p>

        </div>

        <div class="bg-red-500 px-5 py-3 rounded-full
        animate-pulse font-bold shadow-lg">

            🔴 LIVE

        </div>

    </div>

    <!-- Cards -->

    {cards}

</div>

</body>

</html>

"""

    return render_template_string(html)

# ====================================
# تشغيل السيرفر
# ====================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)