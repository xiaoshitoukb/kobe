
#print sushu
# author kobe.yang


def sushu(n):
    for i in range(2, n):
        for x in range(2, i):
            if i % x == 0:
                print(i, 'not zhishu')
                break
        else:
            print(i, 'sushu')


if __name__ == '__main__':

    sushu(100)
