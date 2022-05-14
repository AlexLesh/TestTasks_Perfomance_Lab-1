
def read_file(file_name):
    with open(file_name) as f:
        data = []
        for line in f:
            data.append([float(x) for x in line.split()])
    return data

def check_points_in_circle(data_circle, data_points):

    def get_circle_data(data_circle):
        cirle_data = read_file(data_circle)
        circle_x, circle_y, circle_r = cirle_data[0][0], cirle_data[0][1], cirle_data[1][0]
        return circle_x, circle_y, circle_r

    def get_points_data(data_points,i):
        points_data = read_file(data_points)
        point_x, point_y = points_data[i][0], points_data[i][1]
        return point_x, point_y

    def point_is_circle(data_circle, data_points, i):
        c_x, c_y, r = get_circle_data(data_circle)
        p_x, p_y = get_points_data(data_points,i)

        if (p_x - c_x) ** 2 + (p_y - c_y) ** 2 == r ** 2:
            print("0")
        elif (p_x - c_x) ** 2 + (p_y - c_y) ** 2 < r ** 2:
            print("1")
        else:
            print("2")

    [point_is_circle(data_circle, data_points, i) for i in range(len(read_file(data_points)))]



if __name__ == '__main__':
    f_data_cirlce, f_data_points = input('Введите название файла с данными для окружности: '),\
                                   input('Введите название файла с данными для точек: ')
    check_points_in_circle(f_data_cirlce, f_data_points)