from pathlib import Path
import pypdf
import sys

#-----------合并pdf文件-------------
# 需要安装库 pypdf (pip install pypdf)
# 将要合并的pdf文件放在 <本py文件所在目录>  的子目录 <pdf_files> 中，
# 运行本py文件完成合并，输出文件为 <本py文件所在目录> 中的 <combined.pdf>
# 注意：合并文件次序按 <文件名字排序> ！
# new: 自动在 <本py文件所在目录> 生成名为 <combined-pdfbookmark.txt>
#      的bookmark文件：页码 tab 文件名。为可能的加书签做准备

pdf_files_dir='pdf_files'  #需合并的pdf文件放置的目录名

dir_name=Path(__file__).parent #当前py文件所在目录

writer = pypdf.PdfWriter()  # 创建一个PdfWriter类

bookmark_gen_name = Path(dir_name).joinpath('combined-'+'pdfbookmark.txt')
pdf_path=Path(Path(dir_name).joinpath(pdf_files_dir))
wk_out_file_name=Path(dir_name).joinpath('combined.pdf')

with open (bookmark_gen_name, "w",encoding='utf-8') as f:
    f.write(f"{wk_out_file_name}")
    pagenum=1
    for item in pdf_path.iterdir():
        reader = pypdf.PdfReader(item)
        writer.append(reader)       
        f.write(f"\n{pagenum}\t{item.stem}")
        pagenum=pagenum+reader.get_num_pages()
        reader.close()

    # with open(item, "rb") as f: # 逐个打开需要合并的PDF    
    #     writer.append(f)  # 逐个将PDF读入writer中


#Write to an output PDF document
with open(wk_out_file_name, "wb") as f: # 如果wk_out_file_name不存在，则创建一个
    writer.write(f)  # 将添加书签后的PDF保存
 
# Close File Descriptors
writer.close()

 
pass
