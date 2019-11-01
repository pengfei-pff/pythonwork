from openpyxl import load_workbook
from test_faker import properties_file
from test_faker.properties_file import ReadConfig
class DoExcel:
    def get_data(file_name):
        wb = load_workbook(file_name)
        res = eval(ReadConfig.get_config('case.config','MODE','mode'))
        test_data = []
        for key in res: #遍历这个存在配置文件里的字典
            # print(key)
            sheet = wb[key] #表单名
            for i in range(1,sheet.max_row+1):             #name,phone_number,idCard,company,address
                sub_data = {}
                sub_data['name'] = sheet.cell(i,1).value
                sub_data['phone_number'] = sheet.cell(i,2).value
                sub_data['idCard'] = sheet.cell(i,3).value
                sub_data['company'] = sheet.cell(i,4).value
                sub_data['address'] = sheet.cell(i,5).value
                sub_data['c_id'] = sheet.cell(i,6).value
                test_data.append(sub_data)
            # print(test_data)
        return test_data
    def write_data(self,file_name,sheet_name,i,name,phone_number,idCard,company,address):#专门用于写回Excel数据
        wb = load_workbook(file_name)
        sheet = wb[sheet_name]
        sheet.cell(i,1).value = name
        sheet.cell(i,2).value = phone_number
        sheet.cell(i,3).value = idCard
        sheet.cell(i,4).value = company
        sheet.cell(i,5).value = address
        sheet.cell(i,6).value = i
        wb.save(file_name) #保存结果

if __name__ == '__main__':
   res_data = DoExcel.get_data('data.xlsx')
   print(res_data)