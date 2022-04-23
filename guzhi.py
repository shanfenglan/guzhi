#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Shanfenglan
# datetime:2022/4/1 16:31
# In god's hands.

# R是折现率
# g是10年后的现金流增长率
# CF当前平均每股的现金流，可查到
# rise_year为现金流的年增长率，可以预测
class guzhi:
    def __init__(self, R=None, g=None, CF=None, rise_year=None, name=None, zzn=None, PE=None, EPS=None, LIRUN=None,
                 LIRUN_R=None, XIANJIN_R=None, XIANJIN_RR=None,gujia=None):
        self.R = R
        self.g = g
        self.CF = CF
        self.ry = rise_year
        self.ten = None
        self.name = name
        self.zzn = zzn
        self.PE = PE
        self.EPS = EPS
        self.LIRUN = LIRUN
        self.LIRUN_R = LIRUN_R
        self.XIANJIN_R = XIANJIN_R
        self.XIANJIN_RR = XIANJIN_RR
        self.gujia=gujia

    def calc_jinglirun(self):
        sum1 = 0
        for i in range(self.zzn):
            tt = self.LIRUN * (1 + self.LIRUN_R) ** (i + 1)
            if i == self.zzn - 1:
                self.ten = tt
            tt = tt / (1 + self.R) ** (i + 1)
            sum1 += tt
            s = format(sum1, '.2f')
        # sum2为永续年金折现到现在的金额
        sum2 = self.ten * (1 + self.g) / (self.R - self.g)
        sum2 = sum2 / (1 + self.R) ** 10
        print("# 所有净利润流折现到今天后一股的价值为{0}，对应市盈率为{1}".format(format(sum1 + sum2, '.2f'),format((sum1 + sum2)/self.LIRUN, '.2f')))
        print("# 价值与价格的比值为 {0}，越大越好".format(format((sum1 + sum2)/self.gujia, '.2f')))
    def calc_xianjinjingzengjia(self):
        sum1 = 0
        for i in range(self.zzn):
            tt = self.XIANJIN_R * (1 + self.XIANJIN_RR) ** (i + 1)
            if i == self.zzn - 1:
                self.ten = tt
            tt = tt / (1 + self.R) ** (i + 1)
            sum1 += tt
            s = format(sum1, '.2f')
        sum2 = self.ten * (1 + self.g) / (self.R - self.g)
        sum2 = sum2 / (1 + self.R) ** 10
        print("# 按照现金净增加额折现到今天后一股的价值为{0}".format(format(sum1 + sum2, '.2f')))

    def calc(self):
        # sum1为十年内的现金流折现到当前年份的总和
        print("---------------------------------------------------------")
        print("开始计算十年内现金流折算至今到总和....")
        sum1 = 0
        for i in range(self.zzn):
            tt = self.CF * (1 + self.ry) ** (i + 1)
            if i == self.zzn - 1:
                self.ten = tt
            # print("第{0}年的现金流为{1}".format(i + 1, format(tt, '.2f')))
            tt = tt / (1 + self.R) ** (i + 1)
            sum1 += tt
            # print("第{0}年折现到当前到价值为{1}".format(i + 1, format(tt, '.2f')))
            s = format(sum1, '.2f')
        print("十年内的现金流折现到当前年份的总和为 {0}".format(s))
        # sum2为永续年金折现到现在的金额
        print("开始计算永续年金流折算至今到总和....")
        # print("第十年到现金流为{0}".format(format(self.ten, '.2f')))
        sum2 = self.ten * (1 + self.g) / (self.R - self.g)
        sum2 = sum2 / (1 + self.R) ** 10
        print("永续年金为{0}".format(format(sum2, '.2f')))
        print("---------------------------------------------------------\n")
        print("<{0}>".format(self.name))
        print("# 当前每股现金流为{0}".format(self.CF))
        print("# 平均每股现金净增加额为{0}".format(self.XIANJIN_R))
        print("# 当前每股净利润为{0},增长率为{1}".format(self.LIRUN, self.LIRUN_R))
        print("# 预测未来十年内的平均折现率为{0}，这个数据越大，折算到现在股票的价值就越低，与股票价值呈负相关性".format(self.R))
        print("# 预测未来十年之后的平均现金流增长率为{0}，这个数据肯定小于g，而且这个数据越大，折算到现在股票价值就会越高，与股票价值呈正相关性".format(self.g))
        print("# 预测未来10年现金流增长率为{0},这个数据越大股票未来的价值越大，折算到现在股票的价值就越高，与当前股票价值呈正相关性".format(self.ry))
        print("# 永续年金折算到当前到价值为{0}".format(format(sum2, '.2f')))
        print("# 十年内的现金流折现到当前年份的总和为 {0}".format(s))
        print("=============")
        PEG = self.PE / self.EPS
        print("# PEG的值为{0},大于1代表高估".format(format(PEG, '.2f')))
        heliPE = EPS * 2 + 1 / self.R
        print("# 当前合理PE应该为{0}".format(format(heliPE, '.2f')))
        print("# 所有现金流折现到今天后一股的价值为{0}".format(format(sum1 + sum2, '.2f')))
        self.calc_jinglirun()
        self.calc_xianjinjingzengjia()


if __name__ == '__main__':
    name = "泸州老窖"  # 股票名称
    zzn = 10  # 预测公司会保持这样到增长率几年
    R = 0.09  # 折现率
    g = 0.03  # 10年后的现金流/净利润 增长率

    PE = 27.62  # 当前市盈率

    gujia= 24.8 #当前股价

    CF = 2.53  # 当前平均每股现金流
    zengzhanglv = 0.09  # 从今天往未来看10年内每股现金流的增长率

    LIRUN = 32.80  # 每股净利润
    LIRUN_R = 0.13  # 每股净利润增长率

    XIANJIN_R = 44.37  # 每股现金净增加额
    XIANJIN_RR = 0.13  # 每股净现金增长率

    jyxjl = [640.29,	516.69,	452.11,	413.85,	221.53]  # 经营现金流
    b = [1094.64,	979.93,	888.54,	771.99,	610.63]      # 总营收


    EPS = LIRUN_R * 100  # 净利润增长率

    a = guzhi(rise_year=zengzhanglv, CF=CF, R=R, g=g, name=name, zzn=zzn, EPS=EPS, PE=PE, LIRUN=LIRUN, LIRUN_R=LIRUN_R,
              XIANJIN_R=XIANJIN_R, XIANJIN_RR=XIANJIN_RR,gujia=gujia)
    a.calc()
    print("--------------------------")
    print("经营现金流与总营收的比")
    d = 0
    for i in range(len(jyxjl)):
        c = jyxjl[i] / b[i]
        d+=c
        print(format(c,'.3f'))
    print("平均数为："+format(d/len(jyxjl),'.3f'))

