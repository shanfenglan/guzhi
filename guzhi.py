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
    def __init__(self, R=None, g=None, CF=None, rise_year=None,name=None,dangqian=None):
        self.R = R
        self.g = g
        self.CF = CF
        self.ry = rise_year
        self.ten = None
        self.name=name

    def calc(self):
        #sum1为十年内的现金流折现到当前年份的总和
        print("开始计算十年内现金流折算至今到总和....")
        sum1 = 0
        for i in range(10):
            tt=self.CF * (1 + self.ry)**(i+1)
            if i == 9:
                self.ten=tt
            print("第{0}年的现金流为{1}".format(i+1,format(tt,'.2f')))
            tt=tt/(1+self.R)**(i+1)
            sum1+=tt
            print("第{0}年折现到当前到价值为{1}".format(i+1,format(tt,'.2f')))
            s = format(sum1,'.2f')
        print("---------------------------------------------------------")
        #sum2为永续年金折现到现在的金额
        print("开始计算永续年金流折算至今到总和....")
        print("第十年到现金流为{0}".format(format(self.ten,'.2f')))
        sum2 = self.ten*(1+self.g)/(self.R-self.g)
        print("永续年金为{0}".format(format(sum2,'.2f')))
        sum2 = sum2 / (1+self.R)**10
        print("---------------------------------------------------------\n")
        print("<{0}>".format(self.name))
        print("# 预测未来10年现金流增长率为{0},这个数据越大股票未来的价值越大，折算到现在股票的价值就越高，与当前股票价值呈正相关性".format(self.ry))
        print("# 当前每股现金流为{0}".format(self.CF))
        print("# 预测未来十年内的平均折现率为{0}，这个数据越大，折算到现在股票的价值就越低，与股票价值呈负相关性".format(self.R))
        print("# 预测未来十年之后的平均现金流增长率为{0}，这个数据肯定小于g，而且这个数据越大，折算到现在股票价值就会越高，与股票价值呈正相关性".format(self.g))
        print("# 永续年金折算到当前到价值为{0}".format(format(sum2, '.2f')))
        print("# 十年内的现金流折现到当前年份的总和为 {0}".format(s))
        print("# 所有现金流折现到今天后一股的价值为{0}".format(format(sum1+sum2,'.2f')))

if __name__ == '__main__':

    name = "海尔智家"  # 股票名称
    zengzhanglv = 0.05 # 从今天往未来看10年内每股现金流的增长率
    CF=2.46  # 当前平均每股现金流
    R=0.08 # 折现率
    g=0.00 # 10年后的现金流增长率

    a = guzhi(rise_year=zengzhanglv,CF=CF,R=R,g=g,name=name)
    a.calc()
