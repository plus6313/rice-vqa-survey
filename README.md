# 水稻田間影像 VQA 標註工具

專家用田間照片視覺標註問卷，用於建立 VQA 視覺感知 Ground Truth。

## 快速開始（本機使用）

```bash
# 1. 把 50 張照片放進 image_survey/ 資料夾

# 2. 產生圖片清單
python generate_image_list.py

# 3. 啟動本機伺服器（擇一）
python -m http.server 8080
# 或
npx serve .

# 4. 開啟瀏覽器
# http://localhost:8080
```

## 部署到 GitHub Pages

```bash
# 1. 建立新 repo
git init rice-vqa-survey
cd rice-vqa-survey

# 2. 放入檔案
#    index.html          ← 標註工具主程式
#    image_list.json     ← 圖片清單（由 generate_image_list.py 產生）
#    image_survey/       ← 50 張照片

# 3. 推上 GitHub
git add .
git commit -m "init survey"
git remote add origin https://github.com/YOUR_NAME/rice-vqa-survey.git
git push -u origin main

# 4. 到 GitHub repo → Settings → Pages → Source: main / root → Save
# 約 1-2 分鐘後就能從 https://YOUR_NAME.github.io/rice-vqa-survey/ 存取
```

## 注意事項

- 標註進度自動存在瀏覽器 localStorage，**換瀏覽器或清除快取會遺失**
- 每次標註完成請按右上角「匯出 JSON」備份
- 多人標註時，各自匯出 JSON 後用「匯入」合併即可
- 鍵盤快捷鍵：`A/←` 上一張、`D/→` 下一張、`Enter` 儲存並下一張

## 輸出格式

匯出的 JSON 結構如下：

```json
{
  "image_survey/2025061116_01_CG.jpg": {
    "distance": "mid",
    "angle": "side",
    "lighting": "good",
    "colorchecker": "yes",
    "leaf_color": "normal_green",
    "density": "dense",
    "uniformity": "uniform",
    "ground": "flooded",
    "heading": "none",
    "abnormal": ["none"],
    "stage_guess": "tillering",
    "health": 4,
    "note": "",
    "_timestamp": "2025-06-19T10:30:00.000Z"
  }
}
```
