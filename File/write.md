---
title: 使用CloudFlare作为VPN
date: 2024-08-13 20:08:26
tags:
 - CloudFlare
 - VPN
---
# 方式
本文主要介绍以下两种方式
1. CloudFlare子服务Warp([1.1.1.1](https://1.1.1.1/))
2. 使用CloudFlare Workes搭建VPN通道
> CLoudFlare 牛bi！

# 1.1.1.1
## 下载
点击[warp官网](https://1.1.1.1/)，下载对应设备的版本
> 支持Linux、MacOS、Windows、Android、IOS

## 使用
> 本文使用Windows的Warp功能，其他设备也都差不多

点击 设置-->偏好设置-->账户-->使用其他密钥
![01](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_01.png)
![02](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_02.png)
这里可以使用我的密钥，或是自己生成一个(下文)
```
6ECl4z19-y0M862qC-A7490TKI
```

## 密钥生成
需要Telegram账号，如果没有请注册一个
> Telegram需要魔法上网，这里建议直接使用上面我提供的密钥即可

Robot: https://t.me/generatewarpplusbot
添加机器人，并按如图所操作
> 请注意！这里可能需要让你关注些群聊才能使用

![03](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_03.png)
`7lnfW439-3yX5C4m6-CXd5943m`就是我们生成的密钥了，接下来复制到Warp即可使用
![04](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_04.png)

## 无法连接
1. ~~优选IP~~ Ipv4基本失效
2. 换Ipv6

目前(2024/08/13)Warp在部分地区的Ipv4无法连接，最简单的解决方法就是切换为Ipv6
> 自己上网搜索一下如何开启Ipv6，本文不作解释

如果优选IP与Ipv6都不行，请继续往下看

# CloudFlare Workes
每天免费10w个请求，可以绑定自己的域名，可以访问外网，可以反代理外网的接口
这里选择的是`yonggekkk`大佬的脚本[Cloudflare_vless_trojan](https://github.com/yonggekkk/Cloudflare_vless_trojan)
> 原项目[edgetunnel](https://github.com/zizifn/edgetunnel)
> 改版[EDtunnel](https://github.com/3Kmfi6HP/EDtunnel)

## 前置条件
1. [CloudFlare](https://dash.cloudflare.com/)
2. [V2ray](https://github.com/2dust/v2rayN/releases?after=3.10)
3. 域名(可选)

## 使用脚本
下面将以最简单的方式使用此脚本(无域名操作)，更多扩展操作可看原项目
> 有无域名的区别 --> 有无Tls

### 新建Workers
名字随意
![05](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_05.png)
![06](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_06.png)

### 添加脚本
在项目仓库中的[Vless_workers_pages](https://github.com/yonggekkk/Cloudflare_vless_trojan/blob/main/Vless_workers_pages/_worker.js)文件夹内找到`_worker.js`
![07](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_07.png)
将里面的内容`CTRL+A`复制进刚才创建Workers
![08](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_08.png)

### 配置
#### userID
你应该确保有自己的userID
可以选择网上的[在线生成](https://www.uuidgenerator.net/)，或是在V2里的添加服务器内自动生成
![09](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_09.png)

#### ProxyIP
这是全局代理IP，选择默认的即可
> 不会设别乱设，可能会导致无法进去CloudFlare相关的网站

### 运行
然后点击右上角的部署保存
在URL中输入`https://你的Workers名.你的用户名.workers.dev/你的UID`
> 如我的`https://v2vpn.ui123456ax.workers.dev/a52c418e-a7d7-4d23-a348-1e055c1cb806`

![10](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_10.png)
复制链接后，导入至V2ray即可正常使用
PS: 这里选择可以复制我的链接:
```
vless://a52c418e-a7d7-4d23-a348-1e055c1cb806@www.visa.com.sg:8880?encryption=none&security=none&type=ws&host=v2vpn.ui123456ax.workers.dev&path=%2F%3Fed%3D2560#v2vpn.ui123456ax.workers.dev
```
![11](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_11.png)
![12](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_12.png)

### 无法打开Workers
> 如无此问题，跳过即可
在上一步操作中无法打开输入的`https://你的Workers名.你的用户名.workers.dev/你的UID`链接
通常是因为`.workers.dev`被墙了，要么科学上网，要么手动开启CF节点

#### 手动输入CF节点
在V2rayN中添加`VLESS`服务器，并按如图所设置
![13](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_13.png)
设置完毕即可正常打开网页。这里是属于配置节点，可以正常科学上网了

### 其他代理工具
在部署的Workes中可以看到，支持Clash-meta、Sing-box等链接导入
> 导入时需保持科学环境，否则可能导致导入失败
![14](https://gcore.jsdelivr.net/gh/ui123456ax/PicGo/Blog_images/15_/15_14.png)

## ProxyIP
设置ProxyIP的作用，就是保证能与CloudFlare的连通。说白了，不设置ProxyIP将无法连接与CloudFlare相关的网站(包括使用CFCDN的网站)。一般情况默认即可，无需修改

## 优选IP(域名)
不管你是使用哪个项目的代码搭建CloudFlareV2ray渠道，都应该要注意地址(address)，这将影响全局上网的速度。

1. CloudFlare优选官方IP --> [下载](https://github.com/yonggekkk/Cloudflare_vless_trojan/blob/main/CF%E4%BC%98%E9%80%89%E5%AE%98%E6%96%B9IP(%E7%94%B5%E8%84%91%E7%89%88).zip)
> 速度一般 节点稳定 IP地域大部分为美国
2. CloudFlare优选反代IP --> [下载](https://github.com/yonggekkk/Cloudflare_vless_trojan/blob/main/CF%E4%BC%98%E9%80%89%E5%8F%8D%E4%BB%A3IP(%E7%94%B5%E8%84%91%E7%89%88).zip)
> 速度快 不稳定容易失效 IP地域可根据节点选择
3. CloudFlare优选域名(官方、反代) --> [下载](https://github.com/yonggekkk/Cloudflare_vless_trojan/blob/main/CDN%E4%BC%98%E9%80%89%E5%9F%9F%E5%90%8DV23.8.18(%E7%94%B5%E8%84%91win64).exe)
> IP会随意变动

### 区别
- 域名: 优选域名里包含许多优选IP，并使用其中的一条IP作为连接CloudFlare的通道
- IP: 优选IP则是指定唯一的IP，这将可以选择VPN所在的代理位置
> 一般情况选择优选域名即可

# 结语
无论是所以Warp服务还是自建Workes，其根IP都是CloudFlare，其速度也相差无几。

---
https://www.youtube.com/watch?v=NaLd-orwFUE
https://www.youtube.com/watch?v=FE_gJrk2sSc&t=812s
https://www.youtube.com/watch?v=9V9CQxmfwoA
https://github.com/yonggekkk/warp-yg
https://github.com/yonggekkk/Cloudflare_vless_trojan
https://github.com/zizifn/edgetunnel
https://github.com/3Kmfi6HP/EDtunnel