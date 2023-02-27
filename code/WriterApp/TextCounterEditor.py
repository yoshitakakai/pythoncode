import tkinter as tk
from tkinter import font as tkFont

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("テキストエディター")

        # テキスト入力欄
        self.text = tk.Text(self.master, height=20, width=50, wrap=tk.WORD)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # テキストのフォントサイズ調整用スケール
        self.font_size_scale = tk.Scale(self.master, from_=29, to=33, orient=tk.HORIZONTAL,
                                        command=self.change_font_size, label="フォントサイズ")
        self.font_size_scale.set(500)
        self.font_size_scale.pack(side=tk.TOP, fill=tk.X)

        # 文字数カウント用ラベル
        self.count_label = tk.Label(self.master, text="文字数: 0", font=("Helvetica", 20))
        self.count_label.pack(side=tk.BOTTOM, anchor=tk.SE)

        # イベントの設定
        self.text.bind("<KeyRelease>", self.count_chars)

    def count_chars(self, event):
        text = self.text.get("1.0", "end-1c")  # 入力されたテキストを取得
        char_count = len(text)  # 文字数をカウント
        self.count_label.config(text=f"文字数: {char_count}")  # カウント結果をラベルに表示

    def change_font_size(self, new_size):
        font = tkFont.Font(self.text, self.text.cget("font"))
        font.config(size=new_size)
        self.text.config(font=font)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
