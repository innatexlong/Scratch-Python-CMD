import time


def lang(lt, t):
    ls = {'tip.PasteSave': {'zh_CN': '请粘贴存档码 >> ', 'en_US': 'Paste Your Save Code Here >> '},
          'ask.immeJoin': {'zh_CN': '直接开始编程吗(y/n)', 'en_US': 'Immediate Start Programming?(y/n)'},
          'ask.lang': {'zh_CN': '请选择语言', 'en_US': 'Please Select a Language'},
          'tip.langList': {'zh_CN': '中文 English', 'en_US': '中文 English'},
          'act.run': {'zh_CN': '运行程序', 'en_US': 'Run Program'},
          'tip.noCode': {'zh_CN': '没有任何存储的代码', 'en_US': 'There is No Code'},
          'warn.missPara': {'zh_CN': '警告: 参数缺失', 'en_US': 'Warning: Missing Parameter'},
          'weak.tooManyPara': {'zh_CN': '弱警告: 参数数量超过代码', 'en_US': 'Weak Warning: Too Many Parameter'},
          'fix.addPara': {'zh_CN': '参数数量恢复正常', 'en_US': 'fix.addPara'},
          'act.tellCode': {'zh_CN': '识别存储的代码', 'en_US': 'Tell Code'},
          'ask.doSth': {'zh_CN': '', 'en_US': ''},
          'tip.unknownVar': {'zh_CN': '(未知变量)', 'en_US': '(Unknown Variable)'},
          'error.unknownVar': {'zh_CN': '[错误] 未知变量: ', 'en_US': '[Error] Unknown Variable: '},
          'error.unknownCode': {'zh_CN': '[错误] 未知代码: ', 'en_US': '[Error] Unknown Code: '},
          'act.priVar': {'zh_CN': '打印所有存储的变量', 'en_US': 'Print All Of Variable'},
          'temp': {'zh_CN': '', 'en_US': ''}, }
    if lt in ls and t in ls[lt]:
        return ls[lt][t]
    else:
        return lt


def i(s, mode=0):
    if s[0:2:] == "!&":
        try:
            int(s[2:])
        except ExceptionGroup:
            return s
        else:
            s = int(s[2:])
            return s
    elif mode == 1:
        try:
            int(s)
        except ExceptionGroup:
            return s
        else:
            return int(s)
    else:
        return s


print(lang('ask.lang', 'zh_CN'))
lang_ = ''
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
ans = input(lang('ask.immeJoin', lang_))
save = ''
if ans == 'n':
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


def tellCode(nc, c):
    if c == '00':
        print(lang('code.print', lang_), v[nc])
    elif c == '01':
        print(lang('code.time.sleep', lang_), v[nc])
    elif c == '02':
        print(lang('code.priVar', lang_), v[nc], end=' ')
        if v[nc] not in var:
            print(lang('tip.unknownVar', lang_), v[nc], end='')
        print('')
    else:
        print(lang('error.unknownCode', lang_), v[nc])


def run(nc, c):
    if c == '00':
        print(v[nc])
    elif c == '01':
        time.sleep(v[nc])
    elif c == '02':
        if v[nc] not in var:
            print(var[v[nc]])
        else:
            print(lang('error.unknownVar', lang_))
    else:
        print(lang('error.unknownCode', lang_))


while True:
    print(lang('act.run', lang_)+'/'+lang('act.tellCode', lang_)+'/'+lang('act.priVar', lang_))
    ans = input('\n')
    n = 0
    if ans == lang('act.run', lang_):
        if len(code) >> 0:
            for _ in save:
                run(n, _)
                n += 1
        else:
            print(lang('tip.noCode', lang_))
    elif ans == lang('act.tellCode', lang_):
        if len(code) >> 0:
            for _ in save:
                tellCode(n, _)
                n += 1
    elif ans == lang('act.priVar', lang_):
        print(var)
