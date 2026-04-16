#!/usr/bin/env python3
"""
generate_image_list.py
======================
掃描 image_survey 資料夾，產生 image_list.json 供標註工具使用。

使用方式：
  python generate_image_list.py

輸出：image_list.json（與此腳本同層目錄）
"""
import os, json, glob

SURVEY_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image_survey")
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image_list.json")

images = []
for ext in ("*.jpg", "*.JPG", "*.jpeg", "*.png", "*.PNG"):
    images.extend(glob.glob(os.path.join(SURVEY_DIR, "**", ext), recursive=True))

# 轉為相對於此腳本的路徑
base = os.path.dirname(os.path.abspath(__file__))
rel_images = sorted(set(os.path.relpath(p, base).replace("\\", "/") for p in images))

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(rel_images, f, indent=2, ensure_ascii=False)

print(f"✅ 產生 {len(rel_images)} 張圖片清單 → {OUTPUT}")
