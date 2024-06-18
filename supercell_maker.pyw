import tkinter as tk
from tkinter import filedialog, messagebox
from ase import Atoms
from ase.io import read, write
from ase.build import surface

class SlabGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("晶面切割腳本")
        self.master.geometry("400x350")
        self.master.resizable(False, False)  # 禁止調整視窗大小

        # 文件選擇
        self.label_file = tk.Label(master, text="選擇VASP優化完的原胞文件")
        self.label_file.pack()
        self.button_file = tk.Button(master, text="瀏覽", command=self.load_file)
        self.button_file.pack()
        self.label_file_path = tk.Label(master, text="")
        self.label_file_path.pack()

        # 蜜勒指數輸入
        self.label_miller = tk.Label(master, text="輸入蜜勒指數 (h k l)")
        self.label_miller.pack()
        self.entry_miller = tk.Entry(master)
        self.entry_miller.pack()

        # 原子層數輸入
        self.label_layers = tk.Label(master, text="輸入原子層數")
        self.label_layers.pack()
        self.entry_layers = tk.Entry(master)
        self.entry_layers.pack()

        # 超晶胞大小輸入
        self.label_supercell = tk.Label(master, text="輸入超晶胞大小 (a b)")
        self.label_supercell.pack()
        self.entry_supercell = tk.Entry(master)
        self.entry_supercell.pack()

        # 真空層厚度輸入
        self.label_vacuum = tk.Label(master, text="輸入真空層厚度 (必須大於5Å)")
        self.label_vacuum.pack()
        self.entry_vacuum = tk.Entry(master)
        self.entry_vacuum.pack()

        # 輸出文件位置選擇
        self.label_output = tk.Label(master, text="選擇輸出文件位置")
        self.label_output.pack()
        self.button_output = tk.Button(master, text="瀏覽", command=self.save_file)
        self.button_output.pack()
        self.label_output_path = tk.Label(master, text="")
        self.label_output_path.pack()

        # 執行按鈕
        self.button_execute = tk.Button(master, text="執行", command=self.execute)
        self.button_execute.pack()

    def load_file(self):
        self.input_path = filedialog.askopenfilename()
        self.label_file_path.config(text=self.input_path)

    def save_file(self):
        self.output_path = filedialog.asksaveasfilename(defaultextension=".vasp")
        self.label_output_path.config(text=self.output_path)

    def execute(self):
        miller_indices = tuple(map(int, self.entry_miller.get().split()))
        layers = int(self.entry_layers.get())
        supercell = tuple(map(int, self.entry_supercell.get().split())) + (1,)
        vacuum = float(self.entry_vacuum.get())

        if vacuum <= 5:
            messagebox.showerror("錯誤", "真空層厚度必須大於5Å")
            return

        # 讀取原胞
        structure = read(self.input_path)

        # 切割晶面
        slab = surface(structure, miller_indices, layers)
        slab = slab * supercell

        # 增加真空層
        z_positions = slab.positions[:, 2]
        max_z = max(z_positions)
        min_z = min(z_positions)

        # 將結構移動到正中央，增加底部和頂部的真空層
        slab.positions[:, 2] -= min_z  # 將結構移動到 z = 0
        slab.cell[2, 2] = max_z - min_z + vacuum  # 調整晶胞高度
        slab.positions[:, 2] += 5  # 將結構向上移動5Å，使得底部增加5Å真空層

        # 保存文件
        write(self.output_path, slab, format='vasp')

if __name__ == "__main__":
    root = tk.Tk()
    app = SlabGUI(root)
    root.mainloop()

