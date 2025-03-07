---
title: 使用CloudFlare给GithubPage加速
date: 2024-09-16 11:13:32
tags:
 - cloudflare
 - github
---
# 条件
+ 域名
+ CloudFlare账号
+ Github账号

# 设置CloudFlareDNS解析
使用CloudFlare解析并添加自己的域名
> 注意！输入自己的域名时不要带www或者https

在DNS解析设置界面添加一条**CNAME**记录和一条**A**记录
| type | name | ip |
| ---- | ---- | ---- |
| A  | @ | 185.199.108.153 |
| CNAME  | www | <username>.github.io |
> 其中\<usename\>为自己的GitHub仓库名

![01](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/17_/17_01.png)


如果上述行不通请参考以下方法：
手动将DNS解析指向GitHubPages
添加指向 GitHub Pages 的 IPv4 地址
| type | name | ipv4 |
| ---- | ---- | ---- |
| A  | @ | 185.199.108.153 |
| A  | @ | 185.199.109.153 |
| A  | @ | 185.199.110.153 |
| A  | @ | 185.199.111.153 |

添加指向 GitHub Pages 的 IPv6 地址
| type | name | ipv6 |
| ---- | ---- | ---- |
| AAA | @ | 2606:50c0:8000::153 |
| AAA | @ | 2606:50c0:8001::153 |
| AAA | @ | 2606:50c0:8002::153 |
| AAA | @ | 2606:50c0:8003::153 |


# 设置GitHubPage
`GitHub.io`仓库地址中`Settings`里设置pages，在 Custom domain 里输入自己的域名，点击save
![02](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/17_/17_02.png)
过一会就能生效了

# 优点
能加速域名下的所有内容，可以用来存储图床、博客文章等公开性内容至GitHub
