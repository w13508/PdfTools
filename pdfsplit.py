from pathlib import Path
import pypdf
import sys

#-----------分割pdf文件-------------
# 需要安装库 pypdf (pip install pypdf)
# 首先需要在 <本py文件所在目录> 中手动生成名为 <pdfsplitk.txt> 的分割描述文件
# 分割描述文件 <pdfsplit.txt> 的 格式：
    # 第一行为要操作的pdf文件名字，需要包含完整的目录。
    # 下面各行为：初始页码 tab 结束页码
    # 注意 初始页码 和 结束页码 之间必须是tab！
# 运行本py文件完成分割，输出系列文件名为 <操作的pdf文件所在目录> 中的 <操作的pdf文件名+"初始页码-结束页码".pdf>

split_file_nme='pdfsplit.txt' #分割描述文件的名字

dir_name=Path(__file__).parent #当前py文件所在目录

splitlist=[] #list for split，格式：初始页码 tab 结束页码 (第一行是要操作的pdf文件名)

splitfile_read=Path(dir_name.joinpath(split_file_nme)) #读取split txt文件
with open(splitfile_read,'r',encoding='utf-8') as f:
    line=f.readline() #第一行读入是要操作的pdf文件名
    wk_in_file_name=line.strip() #整理此行：去头尾空格、换行等
    while line:
        line = f.readline()
        if line.strip():
            splitlist.append(line.strip().split('\t'))

reader = pypdf.PdfReader(wk_in_file_name)

for item in splitlist:
    writer = pypdf.PdfWriter()  # 创建一个PdfWriter类

    for i in range(int(item[0]),int(item[1])+1):
        writer.add_page(reader.pages[i-1])

    wk_out_file_name=Path(wk_in_file_name).parent.joinpath(Path(wk_in_file_name).stem + item[0]+'-'+item[1]+'.pdf')
    with open(wk_out_file_name, "wb") as f: # 如果wk_out_file_name不存在，则创建一个
        writer.write(f)  # PDF保存

    writer.close()

# Close File Descriptors
reader.close()


pass
