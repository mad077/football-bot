from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)

MEMORY_FILE = "memory.json"

# ====================================
# Load Data
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
# Home
# ====================================

@app.route("/")
def home():

    data = load_data()[::-1]

    cards = ""

    for item in data:

        possession = item.get("possession", 50)

        cards += f"""

<div class="relative overflow-hidden
bg-gradient-to-br from-gray-900 via-gray-800 to-black
p-6 rounded-3xl shadow-2xl border border-gray-700
hover:border-green-400 transition duration-300
animate-fadeIn mb-8"

style="
background-image:url('https://images.unsplash.com/photo-1517927033932-b3d18e61fb3a?auto=format&fit=crop&w=1600&q=80');
background-size:cover;
background-position:center;
background-blend-mode:overlay;
">

    <!-- Overlay -->

    <div class="absolute inset-0 bg-black/75"></div>

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

            <!-- Home -->

            <div>

                <img
                src="https://cdn-icons-png.flaticon.com/512/53/53283.png"
                class="w-20 mx-auto mb-3 opacity-90">

                <h2 class="text-3xl font-extrabold text-white">

                    {item.get("home","")}

                </h2>

            </div>

            <!-- Score -->

            <div>

                <div class="text-7xl font-black text-green-400 animate-pulse drop-shadow-lg">

                    {item.get("home_score",0)} - {item.get("away_score",0)}

                </div>

                <!-- Goal Explosion -->

                <div class="relative mt-4">

                    <div class="text-yellow-400 font-black text-2xl animate-ping absolute inset-0">

                        ⚽ GOAL!

                    </div>

                    <div class="text-yellow-400 font-black text-2xl relative">

                        ⚽ {item.get("minute",0)}'

                    </div>

                </div>

            </div>

            <!-- Away -->

            <div>

                <img
                src="https://cdn-icons-png.flaticon.com/512/53/53283.png"
                class="w-20 mx-auto mb-3 opacity-90">

                <h2 class="text-3xl font-extrabold text-white">

                    {item.get("away","")}

                </h2>

            </div>

        </div>

        <!-- Live Stats -->

        <div class="grid md:grid-cols-4 gap-4 mt-8">

            <!-- Possession -->

            <div class="bg-black/40 p-4 rounded-2xl border border-gray-700">

                <p class="text-gray-300 mb-2">
                    📈 الاستحواذ
                </p>

                <div class="w-full bg-gray-700 h-4 rounded-full overflow-hidden">

                    <div class="bg-green-400 h-4 rounded-full animate-pulse"
                    style="width:{possession}%"></div>

                </div>

                <p class="mt-2 text-white font-bold">

                    {possession}%

                </p>

            </div>

            <!-- Shots -->

            <div class="bg-black/40 p-4 rounded-2xl border border-gray-700">

                <p class="text-gray-300">
                    🎯 التسديدات
                </p>

                <h2 class="text-4xl mt-3 text-green-400 font-black">

                    {item.get("shots",0)}

                </h2>

            </div>

            <!-- Corners -->

            <div class="bg-black/40 p-4 rounded-2xl border border-gray-700">

                <p class="text-gray-300">
                    🚩 الركنيات
                </p>

                <h2 class="text-4xl mt-3 text-green-400 font-black">

                    {item.get("corners",0)}

                </h2>

            </div>

            <!-- Cards -->

            <div class="bg-black/40 p-4 rounded-2xl border border-gray-700">

                <p class="text-gray-300">
                    🟨 البطاقات
                </p>

                <h2 class="text-4xl mt-3 text-yellow-400 font-black">

                    {item.get("yellow_cards",0)}

                </h2>

            </div>

        </div>

        <!-- Timeline -->

        <div class="mt-8 bg-black/40 backdrop-blur-lg
        rounded-2xl p-5 border border-gray-700">

            <h3 class="text-green-400 text-2xl font-bold mb-4">

                ⚽ Goals Timeline

            </h3>

            <div class="space-y-3 text-white">

                {

                "".join([

                f'''

                <div class="flex justify-between items-center">

                    <span class="text-green-400 font-bold">
                        {event}
                    </span>

                </div>

                '''

                for event in item.get("timeline",[])

                ])

                }

            </div>

        </div>

        <!-- AI Prediction -->

        <div class="mt-6 bg-green-500/20 border border-green-400
        p-5 rounded-2xl">

            <h3 class="text-green-400 font-bold text-2xl mb-2">

                🧠 AI Prediction

            </h3>

            <p class="text-white text-xl">

                🔥 فرصة الفوز: {item.get("prediction",50)}%

            </p>

        </div>

        <!-- AI Comment -->

        <div class="bg-black/50 mt-6 p-5 rounded-2xl
        border border-gray-700">

            <p class="text-xl text-gray-200 leading-8">

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

<meta http-equiv="refresh" content="10">

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

<!-- Goal Popup -->

<div id="goalPopup"
class="fixed inset-0 flex items-center justify-center
bg-black/80 z-50 hidden">

    <div class="text-center animate-bounce">

        <h1 class="text-8xl font-black text-yellow-400">

            ⚽ GOAL!!!

        </h1>

    </div>

</div>

<div class="max-w-7xl mx-auto">

    <!-- Header -->

    <div class="flex justify-between items-center mb-10">

        <div>

            <h1 class="text-5xl font-black text-green-400">

                ⚽ Live VAR Dashboard

            </h1>

            <p class="text-gray-400 mt-2 text-lg">

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

<!-- Goal Popup Script -->

<script>

setInterval(() => {{

    const popup = document.getElementById("goalPopup");

    popup.classList.remove("hidden");

    setTimeout(() => {{

        popup.classList.add("hidden");

    }}, 2000);

}}, 15000);

</script>

</body>

</html>

"""

    return render_template_string(html)

# ====================================
# Run
# ====================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)