def circular_array(n, m):
    array = m * [i for i in range(1, n + 1)]
    b = ''
    for j in range(m-1, m*n, m-1):
        if array[j] != 1:
            b += str(array[j-(m-1)])
        else:
          b += str(array[j - (m - 1)])
          break
    return (b)


if __name__ == '__main__':
    n, m = int(input('Размер кругового массива n: ')), int(input('Интервал m: '))
    if m == 1:
        raise Exception("Шаг не может ровняться 1")
    print(circular_array(n, m))
