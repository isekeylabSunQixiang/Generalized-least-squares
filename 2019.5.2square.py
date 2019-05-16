import matplotlib.pyplot as plt
from pylab import mpl
import xlrd

def liner_fitting(data_x, data_y):
    size = len(data_x)
    i = 0
    sum_xy = 0
    sum_y = 0
    sum_x = 0
    sum_sqare_x = 0
    while i < size:
        sum_xy += data_x[i] * data_y[i]
        sum_y += data_y[i]
        sum_x += data_x[i]
        sum_sqare_x += data_x[i] * data_x[i]
        i += 1
    a = (size * sum_xy - sum_x * sum_y) / (size * sum_sqare_x - sum_x * sum_x)
    print('a =', a)
    return a

def calculate(data_x, a):
    datay = []
    for x in data_x:
        datay.append(a * x)
    return datay

def draw(data_x, data_y_new, data_y_old):
    plt.plot(data_x, data_y_new, label="拟合曲线", color="black")
    plt.scatter(data_x, data_y_old, label="离散数据")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title("一元线性拟合数据")
    plt.legend(loc="upper left")
    plt.show()

if __name__=="__main__":
    data_excel = 'D:\\2\\2.xlsx'
    excel_workbook = xlrd.open_workbook(data_excel)
    data_table = excel_workbook.sheets()[0]
    nrows = data_table.nrows  # 行数
    ncols = data_table.ncols  # 列数
    # print(nrows, ncols)
    x = []
    y = []
    for i in range(0, nrows):
        all_rowdata = data_table.row_values(i)
        x.append(all_rowdata[0])
        y.append(all_rowdata[1])
    parameter = liner_fitting(x, y)
    draw_data = calculate(x, parameter)
    draw(x, draw_data, y)
