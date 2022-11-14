if __name__ == '__main__':
    N = int(input())
    process_list = []
    for i in range(N):
        cmd, *args = input().split()
        if cmd == 'print':
            print(process_list)
        else:
            exec(f'process_list.{cmd}({",".join(args)})')
