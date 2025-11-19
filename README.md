# image-resizer

画像のリサイズと圧縮を行うPythonスクリプトです。

## 機能
- 画像を指定した幅にリサイズ（縦横比維持）
- JPEG形式で圧縮保存
- 複数の画像を一括処理

## 使用法

### 1. 必要なライブラリをインストール
```bash
pip install Pillow
```

### 2. 画像を配置
`images_input/` フォルダに処理したい画像ファイル（.jpg, .jpeg, .png）を配置してください。

### 3. スクリプトを実行
```bash
python image-resizer.py
```

### 4. 結果を確認
処理された画像は `images_output/` フォルダに保存されます。

## 設定

[image-resizer.py](image-resizer.py) の以下の値を変更することで設定をカスタマイズできます：

- `MAX_WIDTH`: リサイズ後の最大幅（デフォルト: 230px）
- `QUALITY`: JPEG圧縮品質（デフォルト: 70、60-85推奨）

## 対応形式
- 入力: JPG, JPEG, PNG
- 出力: JPEG

## 注意事項
- 元の画像ファイルは変更されません（安全に処理できます）
- 出力ファイル名は元のファイル名を維持し、拡張子のみ `.jpg` に変更されます
- `images_output/` フォルダが存在しない場合は自動的に作成されます

## プロジェクト構造
```
image-resizer/
├── image-resizer.py    # メインスクリプト
├── images_input/       # 入力画像フォルダ
├── images_output/      # 出力画像フォルダ
└── README.md          # このファイル
```

## ライセンス
MIT License