import os,re,shutil
from PIL import Image
from threading import Thread

def file_backup(source, path_backup = './Backup/'):
    '''
    文件备份 (原文件 || 备份路径)
    '''
    # 检查备份路径是否存在
    if not os.path.exists(path_backup):
        # 如果不存在则创建
        os.makedirs(path_backup)
    # 复制粘贴文件 shutil.copy || 剪切粘贴文件 shutil.move
    shutil.copy(source, path_backup)


def comic_link():
    '''
    漫画页面图片链接
    '''
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
        msg = f"https://gcore.jsdelivr.net/gh/ui123456ax/images/Caricature/{tag[0]}/{comic}/comic/{i}.{file[0]}"
        print(f'![]({msg})')


def Auto_Blog_images_link(path, backup = True, path_backup = '备份'):
    '''
    自动替换博客文章图片链接 (path读取路径 || backup是否备份 || path_backup备份文件夹)
    规范文档图片: ![图片索引]()
    规范文档名称: 文章编号_文章主题
    规范图片名称: 文章编号_图片索引(例:01_01)
    '''
    path = path + '/'
    def Blog_images(i, passages):
        # 文章
        msg = f"![{i}](https://gcore.jsdelivr.net/gh/ui123456ax/images/Blog_images/{passages}_/{passages}_{i}.png)"
        return msg
    
    for f_name in [fs for fs in os.listdir(path)]:
        read_file = path + f_name

        if os.path.isfile(read_file):
            print(f'开始读取：{f_name}')

            # 文件备份 默认开启
            if backup:
                # 将文件以 文件名，文件格式 拆分
                file_name, file_extension = os.path.splitext(f_name)
                with open(read_file, 'r', encoding='utf-8') as fr, open(path + path_backup + f'/{file_name}-备份{file_extension}', 'w', encoding='utf-8') as fw:
                    for line in fr:
                        fw.write(line)

            # 打开并读取文章数据
            with open(read_file,'r',encoding='utf-8') as fr, open(read_file,'r+',encoding='utf-8') as fw :
                # 获取文章编号 若无则输入
                try:
                    passages = re.findall('(.*?)\_', f_name)[0]
                except:
                    passages = input('输入指定的文章编号：')
                # 读取行数据
                for line in fr:
                    try:
                        images = re.findall('!\[(\d+)\]\(\)',line)[0]
                        new_line = line.replace(line, Blog_images(images, passages)+'\n')
                        print('{}: {}'.format(passages, images))
                    except:
                        new_line = line
                    fw.write(new_line)
            print('='*16)
    

def Auto_LearnNotes_images_link(path, backup = True, path_backup = '备份'):
    pass


def images_conversion(path, file_suffix = 'jpg', target_folder = "输出"):
    '''
    读取图片转为特定格式并排序 (读取路径 || 输出格式 || 输出文件夹)
    '''
    target_folder = path + '/' + target_folder
    image_paths = []
    # 读取文件列表
    for f_name in [fs for fs in os.listdir(path)]:
        file = path + '/' + f_name
        # 过滤非图片
        if not os.path.isdir(file):
            image_paths.append(file)
    print(image_paths)

    # 转换图片 (原路径 || 输出格式 || 输出名称 || 输出文件夹)
    def convert_and_move_image(image_path, output_format, output_name,  target_folder = 'converted_images'):
        image = Image.open(image_path)
        
        # 转换图片格式
        converted_image = image.convert('RGB')
        
        # 创建目标文件夹，如果不存在
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        # 保存转换后的图片到目标文件夹
        converted_image.save(os.path.join(target_folder, f"{output_name}.{output_format}"))
        print(image_path, '-->', f"{output_name}.{output_format}")

    threads = []
    for index,image_path in enumerate(image_paths):
        thread = Thread(target=convert_and_move_image, args=(image_path, file_suffix, index+1, target_folder))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f'共计完成 {len(image_paths)} 个任务')


if __name__ == '__main__':
    path = './File/读取'
    suffix = 'jpg'
    images_conversion(path=path, file_suffix=suffix)