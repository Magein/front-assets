# 生成的css
import sys

css = "body{margin:0 auto;} a{color:#333333;text-decoration:none;} a:hover{color:#2979ff;}"

# 单位 px、rpx
unit = 'px'
if len(sys.argv) == 2 and sys.argv[1]:
    unit = sys.argv[1]

# 边距样式
styles = [
    'm', 'mt', 'mb', 'ml', 'mr', 'mtb', 'mlr', 'p', 'pt', 'pb', 'pl', 'pr', 'ptb', 'plr',
]
values = list(range(1, 101))
for item in styles:
    start = 0
    for value in values:
        mod = value % 5
        if value > 20 and mod:
            continue

        style = ''
        val = value
        if item == 'm':
            style = 'margin'
        elif item == 'mt':
            style = 'margin-top'
        elif item == 'mb':
            style = 'margin-bottom'
        elif item == 'ml':
            style = 'margin-left'
        elif item == 'mr':
            style = 'margin-right'
        elif item == 'mtb':
            style = 'margin'
            val = str(value) + unit + " 0000"
        elif item == 'mlr':
            style = 'margin'
            val = "0 " + str(value)
        elif item == 'p':
            style = 'padding'
        elif item == 'pt':
            style = 'padding-top'
        elif item == 'pb':
            style = 'padding-bottom'
        elif item == 'pl':
            style = 'padding-left'
        elif item == 'pr':
            style = 'padding-right'
        elif item == 'ptb':
            style = 'padding'
            val = str(value) + unit + " 0000"
        elif item == 'plr':
            style = 'padding'
            val = "0 " + str(value)

        if not style:
            continue

        css = css + '.%s%s { %s: %s%s;}' % (item, value, style, val, unit)

css = css.replace('0000px', "0")

# 字体大小
for item in list(range(10, 41)):
    css = css + '.font%s {font-size:%s%s;}' % (item, item, unit)

'''
宽度高度
w0 百分之白
w010 百分之10
'''

# 百分比
css = css + '.w0 {width:100%;}'
css = css + '.h0 {height:100%;}'
for item in list(range(10, 101)):
    css = css + '.w0%s {width:%s%s;}' % (item, item, '%')
    css = css + '.h0%s {height:%s%s;}' % (item, item, '%')

# 宽度和高度具体数值
for item in list(range(10, 1201)):

    if 100 < item < 500 and item % 10:
        continue

    if item > 500 and item % 50:
        continue

    css = css + '.w%s {width:%s%s;}' % (item, item, unit)
    css = css + '.h%s {height:%s%s;}' % (item, item, unit)

# flex布局
css = css + '.flex {display:flex}'
for item in list(range(1, 13)):
    css = css + '.flex%s {flex:%s;}' % (item, item)

# 文字颜色
css = css + '.white-color {color:#ffffff;}'
css = css + '.black-color {color:#000000;}'
css = css + '.red-color {color:#ff0000;}'
css = css + '.gray-color {color:#808080;}'
css = css + '.blue-color {color:#0000ff;}'
css = css + '.blue-light-color {color:#2979ff;}'
css = css + '.main-color {color:#303133;}'
css = css + '.content-color {color:#606266;}'
css = css + '.tips-color {color:#909399;}'
css = css + '.light-color {color:#c0c4cc;}'

# 背景颜色
css = css + '.bg {background:#f3f4f6;}'
css = css + '.bg-gray {background:#808080;}'
css = css + '.bg-error {background:#fa3534;}'
css = css + '.bg-primary {background:#2979ff;}'
css = css + '.bg-warning {background:#ff9900;}'
css = css + '.bg-info {background:#909399;}'
css = css + '.bg-success {background:#19be6b;}'

# 文字位置
css = css + '.text-left {text-align: left;}'
css = css + '.text-center {text-align: center;}'
css = css + '.text-right {text-align: right;}'
# 溢出隐藏
css = css + '.text-line1 {overflow: hidden;text-overflow: ellipsis;-webkit-line-clamp: 1;-webkit-box-orient: vertical;display: -webkit-box;}'
css = css + '.text-line2 {overflow: hidden;text-overflow: ellipsis;-webkit-line-clamp: 2;-webkit-box-orient: vertical;display: -webkit-box;}'
css = css + '.text-line3 {overflow: hidden;text-overflow: ellipsis;-webkit-line-clamp: 3;-webkit-box-orient: vertical;display: -webkit-box;}'
# 显示隐藏
css = css + '.show {display:block;}'
css = css + '.hide {display:none;}'

f = open('css/utils.' + unit + '.css', 'w', encoding="utf-8")
f.write(css)
f.close()
