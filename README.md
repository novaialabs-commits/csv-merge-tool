# CSV・Excel 結合と重複削除（無料・ブラウザ内で完結）

**ツール:** https://novaialabs-commits.github.io/csv-merge-tool/

複数の CSV / Excel ファイルを1つにまとめ、指定した列で重複行を削除する無料ツールです。登録不要です。

- ファイルはアップロードされず、ブラウザ内だけで処理されます（ページの読み込み時に jsDelivr から SheetJS を取得します）
- UTF-8 / Shift_JIS の CSV を自動判定。xlsx も読み込み可
- 先頭ゼロ（商品コード「00123」など）を文字列のまま保持
- 処理前後の件数レポート、削除した重複行の書き出し
- 出力は UTF-8（BOM 付き）の CSV

## 使い方
1. ファイルを複数選ぶ（CSV・xlsx）
2. 重複を判定する列を選ぶ（選ばなければ、すべての列が一致する行を重複とみなします）
3. 「結合して重複を削除」→ 読み込み件数・削除件数・結果件数を確認
4. 結果と、削除した重複行をそれぞれ CSV でダウンロード

重複した行は、先に読み込んだファイル・上にある行が残ります。

## 制限
- 列名・列の並びが同じファイルの結合を想定しています。列名が違うファイルの対応付けはできません
- 1万行・重複100件の架空データで、重複削除の処理が約0.4秒（2026年10月、Chrome、一般的なノートパソコン。読み込み時間を除く）。大きなファイルはパソコンの性能に依存します
- ダウンロードした CSV を Excel でダブルクリックして開くと、Excel 側で先頭の0が消えることがあります（[対処法](https://novaialabs-commits.github.io/csv-merge-tool/articles/csv-leading-zero.html)）

## 関連記事
- [CSVをExcelで開くと文字化けする原因と直し方](https://novaialabs-commits.github.io/csv-merge-tool/articles/csv-mojibake.html)
- [先頭の0が消える・日付に変わるのを防ぐ方法](https://novaialabs-commits.github.io/csv-merge-tool/articles/csv-leading-zero.html)
- [複数のCSVを1つにまとめて重複を削除する方法](https://novaialabs-commits.github.io/csv-merge-tool/articles/csv-merge-dedupe.html)
- [Excelで2つの表を突き合わせて、片方にしかないデータを見つける方法](https://novaialabs-commits.github.io/csv-merge-tool/articles/excel-compare-two-lists.html)

## ほかの無料ツール
- [翻訳ファイル（JSON）のチェッカー](https://novaialabs-commits.github.io/csv-merge-tool/i18n-check/): 原文と訳の JSON を比べ、キーの欠落・空の訳・プレースホルダーやタグの不一致・用語の不一致を一覧にします（ブラウザ内で処理）

## 作業見本
- [CSV整理・UI翻訳・Excel関数の作業見本（架空データ）](https://novaialabs-commits.github.io/csv-merge-tool/portfolio/)

## ツールで対応できない作業
列名がファイルごとに違う、日付の表記をそろえたい、Excel の形で受け取りたいなどの個別作業は、[ココナラ（有料・見積り相談制）](https://coconala.com/services/4449146)で受け付けています。ツール自体は今後も無料です。

---
このツールと記事は生成AI（Claude）を使って作成しています。
