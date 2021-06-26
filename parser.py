import openpyxl


def parse_xlsx_file(filename):
    book = openpyxl.load_workbook('sample.xlsx')
    print(book.active['A1'])


if __name__ == "__main__":
    parse_xlsx_file('data/CA20210624_224522.xlsx')
