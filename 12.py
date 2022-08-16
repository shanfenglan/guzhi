#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk
import tkinter.messagebox


class te:
    def __init__(self):
        self.t = None #存储text组件

        self.ten = None

        self.root = tk.Tk()
        self.root.geometry("1100x700")
        self.root.title("数据分析")

        self.gujia = None #股价
        self.get_gujia = None

        self.name = None  # 股票名称
        self.get_name = None

        self.zzn = None  # 预测公司会保持这样到增长率几年
        self.get_zzn = None

        self.R = None  # 折现率 0.09
        self.get_R = None

        self.g = None  # 10年后的经营现金流/净利润 增长率
        self.get_g = None

        self.CF = None  # 当前平均每股经营现金流
        self.get_CF = None

        self.CF_R = None  # 从今天往未来看10年内每股现金流的增长率
        self.get_CF_R = None

        self.LIRUN = None  # 每股净利润
        self.get_LIRUN = None

        self.LIRUN_R = None # 每股净利润增长率
        self.get_LIRUN_R = None

    def calc(self):
        sum1 = 0
        for i in range(int(self.get_zzn)):
            tt = self.get_CF * (1 + self.get_CF_R) ** (i + 1)
            if i == self.get_zzn - 1:
                self.ten = tt
            tt = tt / (1 + self.get_R) ** (i + 1)
            sum1 += tt
            s = format(sum1, '.2f')
        sum2 = self.ten * (1 + self.get_g) / (self.get_R - self.get_g)
        sum2 = sum2 / (1 + self.get_R) ** 10

        # print("<{0}>".format(self.get_name))
        self.t.insert(tk.INSERT, "<{0}>\n".format(self.get_name))
        # print("# 当前股价为：{0}".format(self.get_gujia))
        self.t.insert(tk.INSERT, "# 当前股价为：{0}\n".format(self.get_gujia))
        sum11 = 0
        for i in range(self.get_zzn):
            tt = self.get_LIRUN * (1 + self.get_LIRUN_R) ** (i + 1)
            if i == self.get_zzn - 1:
                self.ten = tt
            tt = tt / (1 + self.get_R) ** (i + 1)
            sum11 += tt
        sum22 = self.ten * (1 + self.get_g) / (self.get_R - self.get_g)
        sum22 = sum22 / (1 + self.get_R) ** 10

        # print("# 十年内的现金流折现到当前年份的价值为 {0}，与价格的比值为{1}".format(s, format(float(s) / self.get_gujia,'.2f')))
        self.t.insert(tk.INSERT,"# 十年内的现金流折现到当前年份的价值为 {0}，与价格的比值为{1}\n".format(s, format(float(s) / self.get_gujia,'.2f')))

        # print("# 所有现金流折现到今天后一股的价值为{0}，与价格的比值为{1}".format(format(sum1 + sum2, '.2f'), format(float(format(sum1 + sum2, '.2f')) / self.get_gujia, '.2f')))
        self.t.insert(tk.INSERT,"# 所有现金流折现到今天后一股的价值为{0}，与价格的比值为{1}\n".format(format(sum1 + sum2, '.2f'), format(float(format(sum1 + sum2, '.2f')) / self.get_gujia, '.2f')))

        # print("\n# 十年内的利润折现到当前年份的价值为 {0}，与价格的比值为{1}".format(format(sum11, '.2f'),
        #                                                                             format(float(format(sum11,
        #                                                                                                 '.2f')) / self.get_gujia,
        #                                                                                    '.2f')))
        self.t.insert(tk.INSERT,"\n# 十年内的利润折现到当前年份的价值为 {0}，与价格的比值为{1}\n".format(format(sum11, '.2f'),
                                                                                    format(float(format(sum11,
                                                                                                        '.2f')) / self.get_gujia,
                                                                                           '.2f')))

        # print("# 所有净利润流折现到今天的价值为{0}，与价格的比值为{1}".format(format(sum11 + sum22, '.2f'),
        #                                                                      format((sum11 + sum22) / self.get_gujia, '.2f')))
        self.t.insert(tk.INSERT, "# 所有净利润流折现到今天的价值为{0}，与价格的比值为{1}\n".format(format(sum11 + sum22, '.2f'),
                                                                             format((sum11 + sum22) / self.get_gujia, '.2f')))

        # print("=============")
        self.t.insert(tk.INSERT, "=============\n")

        # print("按照净利润来说，十年内可以收回 {0}% 的钱,一共可以回收 {1}%的钱".format(format(float(format(sum11,'.2f'))*100 / self.get_gujia,'.2f'),format((sum11 + sum22)*100 / self.get_gujia, '.2f')))
        self.t.insert(tk.INSERT, "按照净利润来说，十年内可以收回 {0}% 的钱,一共可以回收 {1}%的钱\n".format(format(float(format(sum11,'.2f'))*100 / self.get_gujia,'.2f'),format((sum11 + sum22)*100 / self.get_gujia, '.2f')))

        # print("按照现金流来说，十年内可以收回 {0}% 的钱,一共可以回收 {1}%的钱".format(format(float(s) *100/ self.get_gujia,'.2f'),format(
        #     float(format(sum1 + sum2, '.2f'))*100 / self.get_gujia, '.2f')))
        self.t.insert(tk.INSERT, "按照现金流来说，十年内可以收回 {0}% 的钱,一共可以回收 {1}%的钱\n".format(format(float(s) *100/ self.get_gujia,'.2f'),format(
            float(format(sum1 + sum2, '.2f'))*100 / self.get_gujia, '.2f')))

    def shurukuangming(self):
        # 形成输入框前面的字
        tk.Label(self.root, text="1.公司名", font=("华文行楷", 13)).place(x=0, y=10)
        tk.Label(self.root, text="2.股价", font=("华文行楷", 13)).place(x=0, y=35)
        tk.Label(self.root, text="3.增长时间", font=("华文行楷", 13)).place(x=0, y=60)
        tk.Label(self.root, text="4.折现率", font=("华文行楷", 13)).place(x=0, y=85)
        tk.Label(self.root, text="5.永续增长率", font=("华文行楷", 13)).place(x=0, y=110)

        tk.Label(self.root, text="6.现金流", font=("华文行楷", 13)).place(x=0, y=135)
        tk.Label(self.root, text="7.现金流增长率", font=("华文行楷", 13)).place(x=0, y=160)
        tk.Label(self.root, text="8.利润", font=("华文行楷", 13)).place(x=0, y=185)
        tk.Label(self.root, text="9.利润增长率", font=("华文行楷", 13)).place(x=0, y=210)

        tk.Label(self.root, text="默认增长时间是10年，折现率百分之9，永续增长率百分之3", font=("华文行楷", 13)).place(x=300, y=210)



    def shurukuang(self):
        # 形成输入框
        self.name = tk.Entry(self.root)
        self.name.place(x=100, y=10, width=80, height=23)

        self.gujia = tk.Entry(self.root)
        self.gujia.place(x=100, y=35, width=80, height=23)

        self.zzn = tk.Entry(self.root)
        self.zzn.place(x=100, y=60, width=80, height=23)

        self.R = tk.Entry(self.root)
        self.R.place(x=100, y=85, width=80, height=23)

        self.g = tk.Entry(self.root)
        self.g.place(x=100, y=110, width=80, height=23)

        self.CF = tk.Entry(self.root)
        self.CF.place(x=100, y=135, width=80, height=23)

        self.CF_R = tk.Entry(self.root)
        self.CF_R.place(x=100, y=160, width=80, height=23)

        self.LIRUN = tk.Entry(self.root)
        self.LIRUN.place(x=100, y=185, width=80, height=23)

        self.LIRUN_R = tk.Entry(self.root)
        self.LIRUN_R.place(x=100, y=210, width=80, height=23)

    def get_va(self):
        # 接收所有的值
        self.get_name = self.name.get()
        if self.get_name == '':
            self.get_name = "无公司名"
        else:
            pass

        self.get_gujia = self.gujia.get()

        if self.get_gujia=='':
            tkinter.messagebox.showwarning("error","股价不能为空")
            self.get_gujia =1
        else:
            self.get_gujia = float(self.gujia.get())

        self.get_zzn=self.zzn.get()
        if self.get_zzn == '':
            self.get_zzn = 10
        else:
            self.get_zzn=int(self.zzn.get())


        self.get_R=self.R.get()
        if self.get_R == '':
            self.get_R = 0.09
        else:
            self.get_R=float(self.R.get())

        self.get_g = self.g.get()
        if self.get_g == '':
            self.get_g = 0.03
        else:
            self.get_g=float(self.g.get())

        self.get_CF = self.CF.get()

        self.get_CF_R = self.CF_R.get()

        self.get_LIRUN = self.LIRUN.get()

        self.get_LIRUN_R = self.LIRUN_R.get()

        if self.get_CF=='':
            tkinter.messagebox.showwarning("error","当前现金流不能为空")
            self.get_CF=1
        else:
            self.get_CF = float(self.CF.get())

        if self.get_CF_R=='':
            tkinter.messagebox.showwarning("error","现金流增长率不能为空")
            self.get_CF_R =1
        else:
            self.get_CF_R = float(self.CF_R.get())

        if self.get_LIRUN=='':
            tkinter.messagebox.showwarning("error","利润不能为空")
            self.get_LIRUN =1
        else:
            self.get_LIRUN = float(self.LIRUN.get())

        if self.get_LIRUN_R=='':
            tkinter.messagebox.showwarning("error","利润增长率不能为空")
            self.get_LIRUN_R =1
        else:
            self.get_LIRUN_R = float(self.LIRUN_R.get())

    def hell(self):
        #输出结果
        self.get_va()
        self.calc()

    def text(self):
        tk.Text()
        self.t = tk.Text(self.root, height=20,font=(15))
        self.t.place(x=0, y=400)

    def clean(self):
        #清空输入框
        self.name.delete("0","end")
        self.gujia.delete("0","end")
        self.CF.delete("0","end")
        self.R.delete("0","end")
        self.LIRUN.delete("0","end")
        self.g.delete("0","end")
        self.CF_R.delete("0","end")
        self.zzn.delete("0","end")
        self.LIRUN_R.delete("0","end")
        self.t.delete("0.0","end")


    def run(self):
        self.shurukuangming()
        self.shurukuang()
        self.text()
        tk.Button(self.root, text="计算", command=self.hell).place(x=300, y=0)
        tk.Button(self.root, text="清空", command=self.clean).place(x=400, y=0)
        tk.mainloop()


a = te()
a.run()
