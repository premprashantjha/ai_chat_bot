import sys
print(sys.path)

try:
    from serpapi import GoogleSearch
    print("✅ SerpAPI imported successfully!")
except ModuleNotFoundError as e:
    print("❌ Still getting import error:", e)
