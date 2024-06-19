
# 晶面切割腳本

這是一個用於切割晶面的腳本，使用 `tkinter` 作為圖形用戶界面，並使用 `ase` 庫進行晶體結構處理。

## 功能

- 從 VASP 優化後的慣用晶胞(conventional cell)文件中讀取結構
- 按照指定的蜜勒指數切割晶面
- 設定原子層數、超晶胞大小及真空層厚度
- 保存處理後的晶體結構為 VASP 格式文件

## 安裝

請確保你已經安裝了 Python 及 pip。然後，按照以下步驟安裝必要的套件：

1. clone這個倉庫到本地：
   ```sh
   git clone https://github.com/H6rst0n/supercell_maker.git
   cd supercell_maker
   ```

2. 安裝所需的 Python 套件：
   ```sh
   pip install -r requirements.txt
   ```

## 使用方法

### 方法一

透過終端機執行腳本：
   ```sh
   python supercell_maker.py
   ```
### 方法二

直接滑鼠雙擊 `supercell_maker.pyw` 檔。

### 腳本操作
在彈出的圖形界面中，按照以下步驟操作：
   - 選擇優化完的原胞文件(僅支援VASP格式)
   - 輸入蜜勒指數 (h k l)
   - 輸入原子層數
   - 輸入超晶胞大小 (a b)
   - 輸入真空層厚度（必須大於5Å）
   - 選擇輸出文件位置
   - 點擊“執行”按鈕

## 依賴

- Python 3.x
- ase

## 貢獻

如果你有任何建議或改進，歡迎提交 issue 或 pull request。

