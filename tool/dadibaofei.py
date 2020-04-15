import unittest,csv
from ddt import ddt,data,unpack
import xlrd
import time

#大地百万医疗保费计算


ageRange_haveSS=[[748,50,40,70,30],[748,50,40,70,30]
,[328,20,30,70,20],[138,10,30,70,20],
[176,10,30,70,20],[226,10,50,80,30],
[296,10,80,80,40],
[366,10,150,140,60],
[468,20,240,230,110],
[558,30,400,370,170],
[858,30,600,550,250],
[1088,30,880,800,350],
[1458,30,1300,1100,480],
[1958,50,2200,1400,700],
[2898,50,2800,1800,900],
[3668,50,3600,2400,1300],
[4498,50,4100,2800,1900],
[5998,100,4500,3400,2300],
[7918,100,4900,4500,2900],
[10358,100,5500,6300,3600],
[13438,100,6200,8800,4300]]

ageRange_nohaveSS=[[0,0,0,0,0],[1578,50,40,70,80],
[668,20,30,70,50],
[288,10,30,70,50],
[328,10,30,70,50],
[458,10,50,80,60],
[588,10,80,80,90],
[788,10,150,140,130],
[1208,20,240,230,220],
[1668,30,400,370,340],
[2618,30,600,550,500],
[3608,30,880,800,700],
[4508,30,1300,1100,950],
[5858,50,2200,1400,1300],
[8378,50,2800,1800,1800],
[10598,50,3600,2400,2600],
[12988,50,4100,2800,4100],
[16838,100,4500,3400,4900],
[21938,100,4900,4500,6100],
[28618,100,5500,6300,7600],
[37298,100,6200,8800,9200]]


dadi_family23=[[0,0,0,0,0],[788,50,40,70,30],
[338,20,30,70,20],
[138,10,30,70,20],
[178,10,30,70,20],
[228,10,50,80,30],
[306,10,80,80,40],
[378,10,150,140,60],
[488,20,240,230,110],
[578,30,400,370,170],
[898,30,600,550,250],
[1138,30,880,800,350],
[1518,30,1300,1100,480],
[2038,50,2200,1400,700],
[3018,50,2800,1800,900],
[3818,50,3600,2400,1300],
[4688,50,4100,2800,1900],
[6238,100,4500,3400,2300],
[8238,100,4900,4500,2900],
[10768,100,5500,6300,3600],
[13978,100,6200,8800,4300]]

dadi_family47=[[0,0,0,0,0],[818,50,40,70,30],
[358,20,30,70,20],
[148,10,30,70,20],
[178,10,30,70,20],
[238,10,50,80,30],
[308,10,80,80,40],
[388,10,150,140,60],
[518,20,240,230,110],
[608,30,400,370,170],
[938,30,600,550,250],
[1188,30,880,800,350],
[1588,30,1300,1100,480],
[2128,50,2200,1400,700],
[3138,50,2800,1800,900],
[3978,50,3600,2400,1300],
[4868,50,4100,2800,1900],
[6478,100,4500,3400,2300],
[8558,100,4900,4500,2900],
[11188,100,5500,6300,3600],
[14518,100,6200,8800,4300]]




def get_kms_case(sheetName):
    value_rows = []
    workbook = xlrd.open_workbook('data.xlsx')
    standSheet = workbook.sheet_by_name(sheetName)
    #获取行数和列数
    nrows = standSheet.nrows
    ncols = standSheet.ncols
    for row in range(1, nrows):
        age = standSheet.cell(row, 0).value
        planid= standSheet.cell(row, 1).value
        a1 = int(standSheet.cell(row, 2).value)
        a2 = int(standSheet.cell(row, 3).value)
        a3 = int(standSheet.cell(row, 4).value)
        a4 = int(standSheet.cell(row, 5).value)
        total = int(standSheet.cell(row, 6).value)
        value_rows.append([age,a1,a2,a3,a4,total,planid])
        #print(age, a1, a2, a3, a4, total)
        # print(str(caseId) +' '+ str(caseName)+' '+str(caseParams)+' '+str(caseAssert))
    # return caseId,caseName,caseParams,caseAssert

    return value_rows



@ddt
class KMSCaseTest(unittest.TestCase):
    def setUp(self):
        print('runTestCase start!')
        myTotal = 0

    def tearDown(self):
        print('test over')
    @data(*get_kms_case('Sheet1'))
    @unpack
    def testDadiBaofei(self,age,a1,a2,a3,a4,total,planid):
        # time.sleep(1)

        # moneyList=ageRange_haveSS[int(age)]

        if a1==1:
            aa1 = ageRange_haveSS[int(age)][1]
        else:
            aa1 = 0
        if a2==1:
            aa2 = ageRange_haveSS[int(age)][2]
        else:
            aa2=0
        if a3==1:
            aa3 = ageRange_haveSS[int(age)][3]
        else:
            aa3=0
        if a4==1:
            aa4 = ageRange_haveSS[int(age)][4]
        else:
            aa4=0

        self.myTotal=ageRange_haveSS[int(age)][0]+aa1+aa2+aa3+aa4
        print(ageRange_haveSS[int(age)][0],aa1,aa2,aa3,aa4)


        print("计算得出总保费%d"%self.myTotal)
        self.assertEqual(self.myTotal,total)

    @data(*get_kms_case('Sheet2'))
    @unpack
    def testDadiBaofei_wushebao(self,age,a1,a2,a3,a4,total,planid):
        # time.sleep(1)

        # moneyList=ageRange_haveSS[int(age)]

        if a1==1:
            aa1 = ageRange_nohaveSS[int(age)][1]
        else:
            aa1 = 0
        if a2==1:
            aa2 = ageRange_nohaveSS[int(age)][2]
        else:
            aa2=0
        if a3==1:
            aa3 = ageRange_nohaveSS[int(age)][3]
        else:
            aa3=0
        if a4==1:
            aa4 = ageRange_nohaveSS[int(age)][4]
        else:
            aa4=0

        self.myTotal=ageRange_nohaveSS[int(age)][0]+aa1+aa2+aa3+aa4
        print(ageRange_nohaveSS[int(age)][0],aa1,aa2,aa3,aa4)


        print("计算得出总保费%d"%self.myTotal)
        self.assertEqual(self.myTotal,total)

    @data(*get_kms_case('Sheet3'))
    @unpack
    def testDadiBaofei_family_23(self,age,a1,a2,a3,a4,total,planid):
        if planid==10117:
            rate=dadi_family23
        else:
            rate=dadi_family47

        if a1==1:
            aa1 = rate[int(age)][4]
        else:
            aa1 = 0
        if a2==1:
            aa2 = rate[int(age)][3]
        else:
            aa2=0
        if a3==1:
            aa3 = rate[int(age)][2]
        else:
            aa3=0
        if a4==1:
            aa4 = rate[int(age)][1]
        else:
            aa4=0

        self.myTotal=rate[int(age)][0]+aa1+aa2+aa3+aa4
        print(rate[int(age)][0],aa1,aa2,aa3,aa4)

        print("计划是：%d 取的费率是 %s"%(planid,rate[int(age)]))
        print("计算得出总保费%d"%self.myTotal)
        self.assertEqual(self.myTotal,total)



if __name__ == '__main__':
    unittest.main(verbosity=2)
    # get_kms_case()
