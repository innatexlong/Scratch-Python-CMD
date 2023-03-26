import time


def lang(lt, t):
    ls = {'tip.PasteSave': {'zh_CN': '请粘贴存档码 >> ', 'en_US': 'Paste Your Save Code Here >> '},
          'ask.immeJoin': {'zh_CN': '直接开始编程吗(y/n)', 'en_US': 'Immediate Start Programming?(y/n)'},
          'ask.lang': {'zh_CN': '请选择语言', 'en_US': 'Please Select a Language'},
          'tip.langList': {'zh_CN': '中文 English', 'en_US': '中文 English'},
          'act.run': {'zh_CN': '运行程序', 'en_US': 'Run Program'},
          'tip.noCode': {'zh_CN': '没有代码可以运行', 'en_US': 'No Code Can Run'},
          'warn.missPara': {'zh_CN': '警告:参数缺失', 'en_US': 'Warning: Missing Parameter'},
          'weak.tooManyPara': {'zh_CN': '弱警告: 参数数量超过代码', 'en_US': 'Weak Warning: Too Many Parameter'},
          'fix.addPara': {'zh_CN': '参数数量恢复正常', 'en_US': 'fix.addPara'},
          'temp': {'zh_CN': '', 'en_US': ''}, }
    if lt in ls:
        lb = ls[lt]
        return lb[t]
    else:
        lb = lt
        return lb


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
lang_ = ""
la = input(lang('tip.langList', 'zh_CN')+"\n")
if la == '中文':
    lang_ = 'zh_CN'
elif la == 'English':
    lang_ = 'en_US'
else:
    print('Unknown Language \'%s\'\n. Program Will Exit after 3 second' % la)
    print('未知语言 \'%s\'\n。程序将在3秒后退出' % la)
    time.sleep(3)
    exit(-2)

n, temp = 0, ""
code, var, v = [], {}, []

save = input(lang('tip.PasteSave', lang_))
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
if len(code) >> len(v):
    print(lang('warn.missPara', lang_))
    for _ in range(len(code)-len(v)+1):
        v.append(0)
    print(lang('fix.addPara', lang_))
elif len(code) << len(v):
    print(lang('weak.tooManyPara', lang_))
else:
    pass


def run(nc, c):
    if str(c) == '00':
        print(v[int(nc)])
    if str(c) == '01':
        time.sleep(v[int(nc)])


if input(lang('act.run', lang_)) == "Run Program":
    if len(code) >> 0:
        n = 0
        for _ in save:
            run(int(n), code[int(n)])
            n += 1
    else:
        print(lang('tip.noCode', lang_))
