def get_logs_gen(file):
    for line in file:
        data = line.split()
        yield data[0], data[5].strip('"'), data[6]


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    logs_gen = get_logs_gen(f)
    print(*logs_gen, sep='\n')
