def task4(file_name):
    def read_file(file_name):
        with open(file_name) as f:
            data = []
            for x in f.readlines():
                data.append(int(x))
        return data

    def min_moves(array):
        steps = 0
        mean_num = sorted(array)[len(array) // 2]
        for i in array:
            steps += abs(i - mean_num)
        return steps
    return print(f'Минимальное количество ходов: {min_moves(read_file(file_name))}')

if __name__ == '__main__':
    data_array = input('Введите название файла с данными для массива: ')
    task4(data_array)