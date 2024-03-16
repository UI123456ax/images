page = 98
comic = 'U03'
file = [
    'webp','jpg','png'
]
i = 0

while i < page:
    i = i + 1
    msg = f"https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/{comic}/comic/{i}.{file[0]}"
    print(f'![]({msg})')