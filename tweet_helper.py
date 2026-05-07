import random
import webbrowser
import urllib.parse
import time

# =========================
# الردود
# =========================

TWEETS = [

    "واضح الحكم داخل المباراة بوضع تجريبي 😂",

    "الهجمة جميلة… النهاية كانت درامية 🎬😅",

    "واضح الـVAR يحتاج إعادة تشغيل ☕😂",

    "الفريقين داخلين المباراة بنظام توفير الطاقة 🔋😅",

    "الهجمة بدأت قوية وانتهت بفيلم وثائقي 😂",

    "واضح الدفاع يشاهد المباراة أكثر مما يلعب 😭⚽"

]

# =========================
# اختيار تغريدة
# =========================

tweet = random.choice(TWEETS)

print("🤖 التغريدة:")
print(tweet)

# =========================
# فتح تويتر
# =========================

encoded = urllib.parse.quote(tweet)

url = f"https://twitter.com/intent/tweet?text={encoded}"

print("\n🌐 فتح صفحة النشر...")

time.sleep(2)

webbrowser.open(url)