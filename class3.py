import time


def lang(lt, t):
    ls = {'tips.PasteSave': {'zh_CN': '请粘贴存档码 >> ', 'en_US': 'Paste Your Save Code Here >> '},
          'ask.immeJoin': {'zh_CN': '直接开始编程吗(y/n)', 'en_US': 'Immediate Start Programming?(y/n)'},
          'ask.lang': {'zh_CN': '请选择语言', 'en_US': 'Please Select a Language'},
          'tips.langList': {'zh_CN': '中文 English', 'en_US': '中文 English'},
          'act.run': {'zh_CN': '运行程序', 'en_US': 'Run Program'},
          'temp': {'zh_CN': '', 'en_US': ''}, }
    lb = ls[lt]
    return lb[t]


def i(s):
    if s[0:2:] == "!&":
        try:
            int(s[2:])
        except ExceptionGroup:
            return -1
        else:
            s = int(s[2:])
            return s
    else:
        return s


print(lang('ask.lang', 'zh_CN'))
la = input(lang('tips.langList', 'zh_CN')+"\n")
if la == '中文':
    l = 'zh_CN'
elif la == 'English':
    l = 'en_US'
else:
    print('Unknown Language \'%s\'\nProgram Will Exit' % la)
    exit(-2)

n, temp = 0, ""
code, var, v = [], {}, []

save = input(lang('tips.PasteSave', 'zh_CN'))
b = False
for _ in save:
    if save[2*n:2*n+2] == "||":
        if not b:
            b = True
            n = 2*n+2
    else:
        if not b:
            code.append(save[2*n:2*n+2])
    if save[n] != "," and n << len(save)-1:
        if b:
            temp = temp+save[n]
            # continue
    else:
        if b:
            v.append(temp)
            temp = ""
            if n >= len(save)-1:
                break
    n += 1
n = 0


def run(nc, c):
    if str(c) == '00':
        print(v[nc])
    if str(c) == '01':
        time.sleep(v[nc])


if input(lang('act.run', l)):
    for n in save:
        run(int(n), code[int(n)])
