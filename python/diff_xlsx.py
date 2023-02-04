# Compare the two xls files and find out the difference between them

import os
import pandas
import re
import time

class getdiff:
    def __init__(self) -> None:
        self.xls_dir = os.getcwd()
        self.get_diff()
    
    # 选择文件夹中最新的两个xlsx文件
    def get_two_xlsx_file(self):
        file_list = [ x for x in os.listdir(self.xls_dir) if x.endswith(".xlsx") and re.search(r"\d{6}", x) ]
        file_list.sort(key=lambda fn: os.path.getmtime(self.xls_dir + "\\" + fn))
        return file_list[-2:]
    
    # 获取两个xlsx文件的差异
    def get_diff(self, file_list=None):
        if file_list is None:
            file_list = self.get_two_xlsx_file()
        xlsx1 = pandas.read_excel(os.path.abspath(file_list[0]))
        xlsx2 = pandas.read_excel(os.path.abspath(file_list[1]))
        xlsx1_list = [tuple(xlsx1.loc[i][["商品编码", "分库库存"]]) for i in xlsx1.index]
        xlsx2_list = [tuple(xlsx2.loc[i][["商品编码", "分库库存"]]) for i in xlsx2.index]
        all_data = set(xlsx1_list + xlsx2_list)
        diff_set = set([x[0] for x in all_data if x not in xlsx1_list or x not in xlsx2_list])
        res1 = xlsx2.loc[xlsx2["商品编码"].isin(diff_set)]
        res2 = pandas.DataFrame(res1[["商品名称", "单位", "分库库存"]])
        res2.to_excel(time.strftime("%Y-%m-%d", time.localtime()) + ".xlsx", index=False)
        print("差异数据已保存至当前目录下！")
        
if __name__ == "__main__":
    getdiff()   
        