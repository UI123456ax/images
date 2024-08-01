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
        
def Blog_images():
    # 文章
    passages = 11
    # 图片数
    images = 10
    for i in range(1,images+1):
        if i < 10:
            msg = f"![0{i}](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/{passages}_/{passages}_0{i}.png)"
        else:
            msg = f"![{i}](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/{passages}_/{passages}_{i}.png)"
        print(msg)
    
    
if __name__ == '__main__':
    Blog_images()