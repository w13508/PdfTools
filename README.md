**Contains tools for pdf files (written in Python):**  
1. merge the pdf files into one  
2. split one pdf file into multiple ones  
3. add bookmarks to pdf file



# pdfmerge.py & pdfmerge-new.py
## 合并pdf文件  
- 需要安装库 pypdf (`pip install pypdf`)  
- 将要合并的pdf文件放在 **本py文件所在目录** 的子目录 **pdf_files** 中，运行本py文件完成合并  
- 输出文件为 **本py文件所在目录** 的子目录 **pdf_files**中的 **combined.pdf**   
- 注意：合并文件次序按 **文件名字排序** ！  
- pdfmerge-new: 自动在 **本py文件所在目录** 生成名为 **combined-pdfbookmark.txt** 的bookmark文件：页码 tab 文件名。为可能的加书签做准备

# pdfbookmark.py
## 给pdf文件加书签  
- 需要安装库 pypdf (`pip install pypdf`)  
- 首先需要在 **本py文件所在目录** 中手动制作名为 **pdfbookmark.txt** 的书签描述文件  
- 书签描述文件 **pdfbookmark.txt** 的 格式：
   - 第一行为要操作的pdf文件名字，需要包含完整的目录。
   - 下面各行为：页码 tab 书签名
   - 注意 页码 和 书签名 之间必须是tab！
- 运行本py文件完成加书签，输出文件为 **操作的pdf文件所在目录** 中的 **操作的pdf文件名+“-output”.pdf**

# pdfsplit.py
## 分割pdf文件  
- 需要安装库 pypdf (`pip install pypdf`)  
- 首先需要在 **本py文件所在目录** 中手动生成名为 **pdfsplit.txt** 的分割描述文件  
- 分割描述文件 **pdfsplit.txt** 的 格式：
    - 第一行为要操作的pdf文件名字，需要包含完整的目录。
    - 下面各行为：初始页码 tab 结束页码
    - 注意 初始页码 和 结束页码 之间必须是tab！
- 运行本py文件完成分割，输出系列文件名为 **操作的pdf文件所在目录** 中的 **操作的pdf文件名+"初始页码-结束页码".pdf**
