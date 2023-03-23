import openpyxl


class Excel:

    def get_cell_value(path, sheet, row, col):
        wb = openpyxl.load_workbook(path)
        value = wb[sheet].cell(row, col).value
        print("Cell Value is:", value)
        return value
