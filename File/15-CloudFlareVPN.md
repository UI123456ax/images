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
2. 使用CloudFlare Workes + V2ray搭建VPN通道
> CLoudFlare 牛！

# 1.1.1.1
## 下载
点击[warp官网](https://1.1.1.1/)，下载对应设备的版本
> 支持Linux、MacOS、Windows、Android、IOS

## 使用
> 本文使用Windows的Warp功能，其他设备也都差不多

点击 设置-->偏好设置-->账户-->使用其他密钥
![01]()
![02]()
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
![03]()
`xx`即是我们生成的密钥了，接下来复制到Warp即可使用
![04]()

## 无法连接
1. ~~优选IP~~ Ipv4基本失效
2. 换Ipv6

目前(2024/08/13)Warp在部分地区的Ipv4无法连接，最简单的解决方法就是切换为Ipv6
> 自己上网搜索一下如何开启Ipv6，本文不作解释

如果优选IP与Ipv6都不行，请继续往下看

# CloudFlare + V2ray
每天免费10w个请求，可以绑定自己的域名，可以访问外网，可以反代理外网的接口
这里选择的是`yonggekkk`大佬的脚本[Cloudflare_vless_trojan](https://github.com/yonggekkk/Cloudflare_vless_trojan)
> 原版[EDtunnel](https://github.com/3Kmfi6HP/EDtunnel)

## 前置条件
1. [CloudFlare](https://dash.cloudflare.com/)
2. [V2ray](https://github.com/2dust/v2rayN/releases?after=3.10)
3. 域名(可选)

## 使用脚本
下面将以最简单的方式使用此脚本(无域名操作)，更多扩展操作可看原项目
> 有无域名的区别 --> 有无Tls

### 新建Workers
名字随意
![05]()
![06]()

### 添加脚本
在项目仓库中的[Vless_workers_pages](https://github.com/yonggekkk/Cloudflare_vless_trojan/blob/main/Vless_workers_pages/_worker.js)文件夹内找到`_worker.js`
![07]()
将里面的内容`CTRL+A`复制进刚才创建Workers
![08]()

### 配置
#### userID
你应该确保有自己的userID
可以选择网上的[在线生成](https://www.uuidgenerator.net/)，或是在V2里的添加服务器内自动生成
![09]()

#### ProxyIP
这是全局代理IP，可以选择不理它
> 不会设别乱设，可能会导致无法进去CloudFlare相关的网站

### 运行
然后点击右上角的部署保存
在URL中输入`https://你的Workers名.你的用户名.workers.dev/你的UID`
> 如我的`https://v2vpn.ui123456ax.workers.dev/a52c418e-a7d7-4d23-a348-1e055c1cb806`

![10]()
复制链接后，导入至V2ray即可正常使用
PS: 这里选择可以复制我的链接:
```
vless://a52c418e-a7d7-4d23-a348-1e055c1cb806@www.visa.com.sg:8880?encryption=none&security=none&type=ws&host=v2vpn.ui123456ax.workers.dev&path=%2F%3Fed%3D2560#v2vpn.ui123456ax.workers.dev
```
![11]()
![12]()

---
https://www.youtube.com/watch?v=9V9CQxmfwoA
https://github.com/yonggekkk/warp-yg
https://github.com/yonggekkk/Cloudflare_vless_trojan
https://github.com/3Kmfi6HP/EDtunnel