"""i18n-check/index.html を生成（デモ用の架空サンプルを埋め込む）。python3 i18n-check/build.py"""
import json, csv, pathlib, copy
d = pathlib.Path(__file__).parent
s = d.parent.parent / "localize_service" / "sample"
en = json.load(open(s / "en.json", encoding="utf-8"))
ja = json.load(open(s / "ja.json", encoding="utf-8"))
glo = [{"en": r["en"], "ja": r["ja"]} for r in csv.DictReader(open(s / "glossary.csv", encoding="utf-8-sig"))]
# デモ用に、わざと間違いを3つ入れた訳
ja_demo = copy.deepcopy(ja)
keys = list(ja_demo)
k_ph = next(k for k in keys if "{" in en[k] or "%" in en[k])
ja_demo[k_ph] = ja_demo[k_ph].replace("{", "(").replace("}", ")")
del ja_demo[keys[-1]]
ja_demo[keys[2]] = ""
json.dump(ja_demo, open(d / "demo_ja.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
sample = {"en": en, "ja": ja_demo, "glossary": glo}
html = (d / "template.html").read_text(encoding="utf-8").replace("__SAMPLE__", json.dumps(sample, ensure_ascii=False))
(d / "index.html").write_text(html, encoding="utf-8")
print("demo errors:", k_ph, keys[-1], keys[2])
