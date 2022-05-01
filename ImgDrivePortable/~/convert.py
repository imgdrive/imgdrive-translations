import os

def convert(f):
    srcfile = open(f,'r', encoding='utf-8-sig')
    dstfile = open(f.replace('.txt', '.ini'), 'w', encoding='utf-8-sig')
    dstfile.write('[STRING]\n')
    lineNum = 1
    for line in srcfile:
        line=line.strip('\n').replace('L"', '').replace('",', '')
        print(str(lineNum) + '=' + line)
        if lineNum != 1:
            dstfile.write('\n')
        dstfile.write(str(lineNum) + '=' + line)
        lineNum = lineNum + 1
    srcfile.close()
    dstfile.close()
    
    if lineNum != 32:
        assert(0)

file = os.listdir('.')
for f in file:
    if f.endswith('.txt'):
        print(f)
        convert(f)
