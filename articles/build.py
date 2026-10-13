"""articles/*.html を生成する。python3 articles/build.py（csv_web_tool/ で実行）"""
import html, pathlib

BASE = "https://novaialabs-commits.github.io/csv-merge-tool/"
OUT = pathlib.Path(__file__).parent

STYLE = """
:root { --ink:#1F2937; --sub:#6B7280; --accent:#0F766E; --line:#D1D5DB; --bg:#F8FAFC; --card:#FFFFFF; --code:#EEF2F6; }
@media (prefers-color-scheme: dark) { :root { --ink:#E5E7EB; --sub:#9CA3AF; --accent:#2DD4BF; --line:#374151; --bg:#111827; --card:#1F2937; --code:#273244; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font-family:-apple-system,"Hiragino Sans","Noto Sans JP",sans-serif; line-height:1.8; }
main { max-width:760px; margin:0 auto; padding:32px 16px 64px; }
h1 { font-size:1.5rem; line-height:1.4; margin:0 0 8px; }
h2 { font-size:1.15rem; margin:32px 0 8px; padding-bottom:4px; border-bottom:1px solid var(--line); }
.meta, .note { color:var(--sub); font-size:.9rem; }
.card { background:var(--card); border:1px solid var(--line); border-radius:12px; padding:16px 20px; margin:16px 0; }
code, b.ui { background:var(--code); border-radius:4px; padding:0 4px; font-weight:600; }
a { color:var(--accent); }
ol, ul { padding-left:1.4em; }
"""

ARTICLES = [
    {
        "slug": "csv-mojibake",
        "title": "CSVをExcelで開くと文字化けする原因と直し方",
        "desc": "CSVファイルをExcelでダブルクリックして開くと日本語が文字化けする原因（UTF-8とShift_JIS）と、データを壊さずに正しく開く3つの方法をまとめました。",
        "body": """
<p>ダウンロードしたCSVをExcelで開いたら、日本語が「縺薙ｓ縺ｫ縺｡縺ｯ」のような記号の羅列になってしまった。よくあるこのトラブルの原因と直し方をまとめます。</p>

<h2>原因：文字コードの食い違い</h2>
<p>CSVはただのテキストファイルで、文字を保存する方式（文字コード）がファイルごとに違います。日本でよく使われるのは次の2つです。</p>
<ul>
<li><b>UTF-8</b>：Webサービスや海外のツールが出力するCSVの多く</li>
<li><b>Shift_JIS</b>：古い業務システムや、日本語版Excelが昔から使ってきた方式</li>
</ul>
<p>日本語版のExcelでCSVをダブルクリックすると、ファイルの先頭に「BOM」という目印がないUTF-8のファイルを、Shift_JISとして読んでしまうことがあります。これが文字化けの正体です。ファイルが壊れているわけではありません。</p>

<h2>方法1：Excelの「テキストまたはCSVから」で開く</h2>
<ol>
<li>Excelで空のブックを開く</li>
<li><b class="ui">データ</b> タブ → <b class="ui">テキストまたはCSVから</b> を選び、CSVファイルを指定</li>
<li>取り込み画面の <b class="ui">元のファイル</b> で文字コードを選ぶ。UTF-8なら <b class="ui">65001</b>（Unicode UTF-8）、Shift_JIS系なら <b class="ui">932</b>（日本語 Shift-JIS）</li>
<li>プレビューで文字が正しく表示されたことを確認してから <b class="ui">読み込み</b></li>
</ol>
<p class="note">Windows版Excelを想定しています。Microsoft 365・Excel 2016以降でも、バージョンや更新状況によってメニューの表示が異なる場合があります。</p>

<h2>方法2：ファイルを「BOM付きUTF-8」で保存し直す</h2>
<p>Windowsのメモ帳などのテキストエディターでCSVを開き、<b>元の日本語が正しく表示されていることを確認してから</b>、<b class="ui">名前を付けて保存</b> で文字コードを <b class="ui">UTF-8 (BOM 付き)</b> にしてコピーを保存します。以後はダブルクリックでも文字化けしにくくなります。文字化けした表示のまま保存し直さないでください。元のファイルは残しておきましょう。</p>

<h2>方法3：Excelから保存するときは「CSV UTF-8」を選ぶ</h2>
<p>ExcelからUTF-8形式で保存するときは、<b class="ui">ファイル</b> → <b class="ui">名前を付けて保存</b> で <b class="ui">CSV UTF-8 (コンマ区切り)</b> を選びます。ダブルクリックでの表示を安定させるためにBOM付きが必要な場合は、保存されたファイルが実際にBOM付きか確認してください（BOMはファイル先頭の3バイト <code>EF BB BF</code> です）。</p>
<p>取り込み先がShift_JIS系を指定している場合は、その仕様に合った文字コードで保存する必要があります。通常の <b class="ui">CSV (コンマ区切り)</b> で保存される文字コードは環境によって異なるため、形式名だけで判断しないでください。</p>

<h2>やってはいけないこと</h2>
<p>文字化けした状態のまま上書き保存すると、元の文字に戻せなくなることがあります。おかしいと思ったら、保存せずに閉じてから上の方法で開き直してください。</p>
""",
    },
    {
        "slug": "csv-leading-zero",
        "title": "CSVをExcelで開くと先頭の0が消える・日付に変わるのを防ぐ方法",
        "desc": "商品コードの「00123」が「123」になる、「1-2」が「1月2日」になる、長い番号が「1.23E+15」になる。CSVをExcelで開いたときの自動変換を防ぐ方法をまとめました。",
        "body": """
<p>CSVをExcelで開くと、次のような「勝手な変換」が起きることがあります。</p>
<ul>
<li>商品コード <b>00123</b> → <b>123</b>（先頭の0が消える）</li>
<li>型番 <b>1-2</b> → <b>1月2日</b>（日付になる）</li>
<li>長い番号 <b>1234567890123456789</b> → 15桁を超える部分が <b>0</b> に置き換わり、表示も <b>1.23457E+18</b> のような指数形式になることがある</li>
</ul>
<p>Excelがダブルクリックで開いたCSVの中身を「数値」や「日付」だと推測して変換するのが原因です。一度この状態で上書き保存すると、元の値には戻せません。</p>

<h2>方法1：取り込むときに「文字列」として読む</h2>
<ol>
<li><b class="ui">データ</b> タブ → <b class="ui">テキストまたはCSVから</b> でファイルを指定</li>
<li>プレビュー画面の <b class="ui">データ型検出</b> を <b class="ui">データ型を検出しない</b> にする</li>
<li><b class="ui">読み込み</b>。すべての列が文字列のまま取り込まれ、先頭の0や型番がそのまま残ります</li>
</ol>
<p>一部の列だけ数値として計算したい場合は、<b class="ui">データの変換</b> を押して開く画面（Power Query エディター）で、列ごとにデータ型を <b class="ui">テキスト</b> や <b class="ui">整数</b> に指定してから読み込みます。</p>

<h2>方法2：Excelの自動変換の設定を確認する</h2>
<p>対応するWindows版のMicrosoft 365 Excelでは、<b class="ui">ファイル</b> → <b class="ui">オプション</b> → <b class="ui">データ</b> → <b class="ui">自動データ変換</b> で、先頭の0の削除や長い数値の変換などを個別に止められます。表示されない場合は、Excelのバージョンや更新状況を確認してください。設定を変える前に失われたデータは、この操作では元に戻りません。</p>

<h2>方法3：開くだけならブラウザの無料ツールを使う</h2>
<p>CSVを結合したり重複を消したりするだけなら、<a href="../">CSV・Excel 結合と重複削除ツール</a>（無料・登録不要）も使えます。値を文字列として扱うため、ツールの中では先頭の0や長い番号は変わりません。ただし、出力したCSVをExcelでダブルクリックして開くと、Excel側で同じ変換が起きます。出力したCSVも、上の方法1で開いてください。</p>

<h2>覚えておくこと</h2>
<p>「ダブルクリックで開いて、そのまま上書き保存」が一番危険です。大事なCSVは、まずコピーを取ってから作業してください。</p>
""",
    },
    {
        "slug": "csv-merge-dedupe",
        "title": "複数のCSVを1つにまとめて重複を削除する方法（Excel・無料ツール）",
        "desc": "月ごとに分かれた売上CSVなど、複数のCSVファイルを1つにまとめ、重複した行を削除する方法を、ExcelのPower Queryと無料のブラウザツールの2通りで説明します。",
        "body": """
<p>月ごと・店舗ごとに分かれたCSVを1つの表にまとめたい。期間が重なっていて、同じ注文が2回入ってしまう。そんなときの手順です。</p>

<h2>前提：列名をそろえる</h2>
<p>結合する前に、各CSVの列名・列数・列の並び・文字コードを確認してください。下で紹介する方法は、どちらも同じ構造のファイルをまとめる用途に向いています。列名が違ったり列の位置がずれたりすると、意図しない列への取り込みや欠損、エラーの原因になります。結合するCSVだけを専用のフォルダーに入れ、バックアップや別形式のファイルが混ざらないようにしましょう。</p>

<h2>方法1：ExcelのPower Queryでフォルダーごとまとめる</h2>
<ol>
<li>まとめたいCSVだけを1つのフォルダーに入れる</li>
<li><b class="ui">データ</b> タブ → <b class="ui">データの取得</b> → <b class="ui">ファイルから</b> → <b class="ui">フォルダーから</b> でそのフォルダーを選ぶ</li>
<li><b class="ui">結合</b> → <b class="ui">データの結合と変換</b> を選ぶ。文字化けする場合は、この画面の <b class="ui">元のファイル</b> で文字コードを選び直す</li>
<li>Power Query エディターで結合結果・列名・データ型を確認する</li>
<li>重複を判定する列（例：注文番号）を選ぶ。すべての列が一致する行だけを消したい場合は、すべての列を選ぶ</li>
<li><b class="ui">ホーム</b> → <b class="ui">行の削除</b> → <b class="ui">重複の削除</b></li>
<li><b class="ui">閉じて読み込む</b></li>
</ol>
<p>次の月のCSVをフォルダーに追加したら、<b class="ui">データ</b> → <b class="ui">すべて更新</b> で結果が更新されます。注意：Power Queryの <b class="ui">重複の削除</b> では、重複した行のうち<b>どの行が残るかは保証されていません</b>（並べ替えておいても、その順序が保たれるとは限りません）。例えば同じ顧客IDに古い住所と新しい住所がある場合、新しい方が残るとは限りません。「最新の行を残す」などの条件がある場合は、単純な重複の削除ではなく、条件に合う行を選ぶ処理が必要です。</p>
<p class="note">Windows版Excelを想定しています。バージョンや更新状況によってメニューの表示が異なる場合があります。</p>

<h2>方法2：無料のブラウザツールでまとめる</h2>
<p>Power Queryの設定が面倒なときや、1回だけまとめたいときは、<a href="../">CSV・Excel 結合と重複削除ツール</a>が使えます。</p>
<ol>
<li>ファイルを複数選ぶ（CSV・xlsx、UTF-8／Shift_JISは自動判定）</li>
<li>重複を判定する列を選ぶ（選ばなければ、すべての列が一致する行を重複とみなします）</li>
<li><b class="ui">結合して重複を削除</b> → 読み込み件数・削除件数・結果件数が表示される。重複した行は、<b>先に読み込んだファイル・上にある行が残ります</b></li>
<li>結果と、削除した重複行をそれぞれCSVでダウンロード</li>
</ol>
<p>処理はブラウザの中だけで行われ、ファイルの内容はどこにも送信されません。1万行・重複100件の架空データで、重複削除の処理が0.4秒ほどで終わることを確認しています（2026年10月、Chrome、一般的なノートパソコン。読み込み時間は含みません）。作業前に元ファイルをコピーし、出力結果の件数と内容を確認してください。</p>

<h2>必ず件数を確かめる</h2>
<p>結合と重複削除だけを行った場合は、「取り込んだデータ行数（見出し行を除く）＝ 重複削除後の行数 ＋ 削除した行数」になっているか確認してください。合わない場合は、読み込みエラーや空行の扱い、意図しない絞り込みを確認します。件数が合っていても内容が正しいとは限らないため、代表的な行の値も確かめましょう。</p>
""",
    },
]

FOOT = """
<div class="card note">
制作・確認について：本記事の原案は生成AI（Claude）を使用して作成し、Excel・Power Queryに関する技術的な記述を別の生成AI（ChatGPT）でMicrosoft公式資料と照合しました。実際の画面表示や利用できる機能は、Excelのバージョン・OS・更新状況によって異なる場合があります。<br>
{PROMO}
</div>
<p class="note"><a href="../">← 無料ツールに戻る</a>　|　<a href="./">記事一覧</a></p>
"""


PROMO = {
    "csv-mojibake": "文字コードが混在した複数のCSVをまとめて整えたい場合は、<a href=\"https://coconala.com/services/4449146\" target=\"_blank\" rel=\"noopener\">ココナラ（有料・見積り相談制）</a>でも受け付けています。",
    "csv-leading-zero": "商品コードの先頭の0や日付の表記をそろえた形で受け取りたい場合は、<a href=\"https://coconala.com/services/4449146\" target=\"_blank\" rel=\"noopener\">ココナラ（有料・見積り相談制）</a>でも受け付けています。",
    "csv-merge-dedupe": "列名がファイルごとに違う、どの行を残すかの条件があるなど、ツールで対応できない結合は<a href=\"https://coconala.com/services/4449146\" target=\"_blank\" rel=\"noopener\">ココナラ（有料・見積り相談制）</a>で受け付けています。",
}


def page(title, desc, url, body):
    t = html.escape(title)
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<style>{STYLE}</style>
</head>
<body>
<main>
<p class="meta"><a href="../">CSV・Excel 結合と重複削除（無料ツール）</a> ／ 記事</p>
<h1>{t}</h1>
<p class="meta">2026年10月13日公開</p>
{body}
</main>
</body>
</html>
"""


def main():
    for a in ARTICLES:
        url = f"{BASE}articles/{a['slug']}.html"
        (OUT / f"{a['slug']}.html").write_text(page(a["title"], a["desc"], url, a["body"] + FOOT.replace("{PROMO}", PROMO[a["slug"]])), encoding="utf-8")
    items = "\n".join(f'<li><a href="{a["slug"]}.html">{html.escape(a["title"])}</a><br><span class="note">{html.escape(a["desc"])}</span></li>' for a in ARTICLES)
    body = f'<ul style="list-style:none;padding:0">{items}</ul><p class="note"><a href="../">← 無料ツールに戻る</a></p>'
    (OUT / "index.html").write_text(page("CSV・Excelのよくあるトラブルと対処法", "CSVをExcelで扱うときによくある文字化け・先頭の0の消失・複数ファイルの結合と重複削除の対処法をまとめた記事一覧です。", f"{BASE}articles/", body), encoding="utf-8")


if __name__ == "__main__":
    main()
