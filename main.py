
def generate_sequence(n):
    seq = []
    free_spaces = n
    for num in range(n + 1):
        if free_spaces > num:
            values_to_extend = [num] * num
            seq.extend(values_to_extend)
            free_spaces -= len(values_to_extend)
        else:
            values_to_extend = [num] * free_spaces
            seq.extend(values_to_extend)
            break
    return seq


def main():
    while True:
        try:
            n = int(input('Введите число: '))
            if 0 <= n < 9223372036854775807:
                break
            else:
                print('Введено неверное значение, допустимы целые числовые значения от 0 и до 9223372036854775807.')
        except ValueError:
            print('Введено неверное значение, допустимы целые числовые значения от 0 и до 9223372036854775807.')
    print(*generate_sequence(n), sep='')


if __name__ == '__main__':
    main()
