import os,re

# 漫画页面图片链接
def comic():
    # 页数
    pages = 96
    # 名称
    comic = 'U03'
    # 类型
    tag = [
        'porn_ero'
    ]
    # 文件格式
    file = [
        'webp','jpg','png'
    ]
    for i in range(1,pages+1):
        msg = f"https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Caricature/{tag[0]}/{comic}/comic/{i}.{file[0]}"
        print(f'![]({msg})')
     
     
# 博客文章图片链接
def Auto_Blog_images():
    def Blog_images(i):
        # 文章
        passages = 15
        msg = f"![{i}](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/{passages}_/{passages}_{i}.png)"
        return msg
    
    # 打开文件
    with open('./File/read.md','r',encoding='utf-8') as fr, open('./File/write.md','w',encoding='utf-8') as fw :
        # 读取行数据
        for line in fr:
            try:
                images = re.findall('!\[(\d+)\]\(\)',line)[0]
                print(images)
                new_line = line.replace(line, Blog_images(images)+'\n')
            except:
                new_line = line
            fw.write(new_line)
            
                    
    
if __name__ == '__main__':
    Auto_Blog_images()