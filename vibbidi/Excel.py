import xlrd

location = r'C:\Users\ADMIN\Desktop\techkids\Fundamentals\a.xlsx'
wb = xlrd.open_workbook(location) 
sheet = wb.sheet_by_index(0) 

#in ra ô hàng 0 cột 0
print(sheet.cell_value(0, 0) )


#in ra số hàng, số cột
print(sheet.nrows) 
print(sheet.ncols) 

#in ra hàng đầu tiên ( không tính header ) dưới dạng list
print(sheet.row_values(1)) 