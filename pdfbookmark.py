from pathlib import Path
import pypdf
import sys


#-----------给pdf文件加书签-------------
# 需要安装库 pypdf (pip install pypdf)
# 首先需要在 <本py文件所在目录> 中手动制作名为 <pdfbookmark.txt> 的书签描述文件
# 书签描述文件 <pdfbookmark.txt> 的 格式：
    # 第一行为要操作的pdf文件名字，需要包含完整的目录。
    # 下面各行为：页码 tab 书签名
    # 注意 页码 和 书签名 之间必须是tab！
# 运行本py文件完成加书签，输出文件为 <操作的pdf文件所在目录> 中的 <操作的pdf文件名+“-output”.pdf>

bookmark_file_name='pdfbookmark.txt' #书签描述文件的名字

dir_name=Path(__file__).parent #当前py文件所在目录

bookmarklist=[] #list for bookmark，格式：页码 tab 书签名(第一行是要操作的pdf文件名)

bookmark_file_read=Path(dir_name.joinpath(bookmark_file_name)) #读取bookmark文件
with open(bookmark_file_read,'r',encoding='utf-8') as f:
    line=f.readline() #第一行读入是要操作的pdf文件名
    wk_in_file_name=line.strip() #整理此行：去头尾空格、换行等
    while line:
        line = f.readline()
        if line.strip():
            bookmarklist.append(line.strip().split('\t'))

writer = pypdf.PdfWriter()  # 创建一个PdfWriter类

with open(wk_in_file_name, "rb") as f: # 打开需要添加书签的PDF
    writer.append(f)  # 将PDF读入writer中，然后进行书签的编辑

for item in bookmarklist:
    if item[0].isdigit():
        writer.add_outline_item(title=item[1], page_number=int(item[0])-1, parent=None)  # 添加第一个书签

# Write to an output PDF document
wk_out_file_name=Path(wk_in_file_name).parent.joinpath(Path(wk_in_file_name).stem + '-outlined.pdf')

with open(wk_out_file_name, "wb") as f: # 如果wk_out_file_name不存在，则创建一个
    writer.write(f)  # 将添加书签后的PDF保存

# Close File Descriptors
writer.close()


pass
