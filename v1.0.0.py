#导入模块
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
import  PySimpleGUI as gui
import os, sys

#一些要用的函数
def select(type):
    layout = [
        [gui.Text('请选择文件')],
        [gui.Input(), gui.FileBrowse()],
        [gui.OK(), gui.Cancel()]
    ]
    window = gui.Window('选择文件', layout)
    event, values = window.read()
    window.close()
    with open('filepath.ptmp', 'w', encoding='utf-8') as f:
        text = values['Browse']
        f.write(text)
        f.close()

def cut_pdf(pdf_name):
    pdf_reader = PdfFileReader(pdf_name)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf_reader.getPage(page))
        page = page + 1
        with open(f'./PDF第 {page} 页.pdf', 'wb') as out:
            pdf_writer.write(out)

#布局
layout_welcome = [
    [gui.Text('欢迎使用PDF拆分工具！这是一款简易的PDF工具，永久免费！')],
    [gui.Text('作者：wdd   Github:PWBC-China')],
    [gui.Text('点击下方按钮开始使用！处理完成后窗口将自动关闭！')],
    [gui.Text('转换完成后，请在原目录查看！')],
    [gui.Button('选择文件')]
]

layout_turn_success = [
    [gui.Text('转换完成后，请在原目录查看！！！')],
]

layout_turning = [
    [gui.Text('正在转换中……')],
    [gui.Text('您可以关闭这个窗口，操作将在后台进行！')]
]

layout_notice = [
    [gui.Text('在窗口自动关闭以后，请至原目录查看文件！')]
]

#正式开始操作
window = gui.Window('简易PDF工具', layout_welcome)
event, values = window.read()
while event == '选择文件':
    notice = gui.Window('注意事项', layout_notice)
    event1, values1 = notice.read()
    select('file')
    break
reader = open('filepath.ptmp', 'r', encoding='utf-8')
filepath = reader.readline()
reader.close()
window2 = gui.Window('转换中！', layout_turning)
event2, values2 = window2.read()
cut_pdf(filepath)
window3 = gui.Window('转换成功', layout_turn_success)
event3, values3 = window3.read()
os.remove('filepath.ptmp')