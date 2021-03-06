# 写给六个月前的自己——关联 GitHub 和 GitBook
## 解题思路
### 一. 搞定 GitHub 
#### 1.注册  [GitHub](https://github.com) 
#### 2.登陆
#### 3.入门
在 [GitHub Help](https://help.github.com) 学习如何使用 GitHub 。
> 如新建一个库，第三个步骤中会用到。 

也可以在 [GitHub Guides ](https://guides.github.com) 有针对性地深入学习。
### 二. 搞定 GitBook
#### 1.注册 [GitBook](https://www.gitbook.com)
可以用 GitHub 账号直接登陆。

>tips：不要忘记验证你的邮箱。如何验证请看下面的具体步骤。

#### 2.登陆
#### 3.入门
GitBook 非常简单，新建一个 book 就可以进入第三个步骤了。
#### 4.Gitbook 的命令行

#####下载并安装 [Nodejs](https://nodejs.org)
     $ note -v
     显示"v0.12.0"表示已安装。 
#####GitBook命令
     $ gitbook -V     
     显示 "1.5.0",表示Gitbook也已经安装。
     
     $ gitbook build ./repository --output=./outputFolder
     显示“Starting build ...
          ENOENT, open 'repository/README.md'”
     但不会处理。
     
     $ gitbook build 
     显示“Starting build ...
         Cannot read property 'text' of undefined”
     
     $ gitbook init

    显示如下错误
    
    “TypeError: Cannot read property 'text' of undefined
    at parseChapter (/usr/local/lib/node_modules/gitbook/lib/parse/summary.js:95:46)
    at Array.map (native)
    at Object.parseSummary [as summary] (/usr/local/lib/node_modules/gitbook/lib/parse/summary.js:134:6)
    at /usr/local/lib/node_modules/gitbook/lib/generate/init.js:33:22
    at _fulfilled (/usr/local/lib/node_modules/gitbook/node_modules/q/q.js:787:54)
    at self.promiseDispatch.done (/usr/local/lib/node_modules/gitbook/node_modules/q/q.js:816:30)
    at Promise.promise.promiseDispatch (/usr/local/lib/node_modules/gitbook/node_modules/q/q.js:749:13)
    at /usr/local/lib/node_modules/gitbook/node_modules/q/q.js:557:44
    at flush (/usr/local/lib/node_modules/gitbook/node_modules/q/q.js:108:17)
    at process._tickCallback (node.js:355:11)”
    
    
>我在谷歌搜索“TypeError: Cannot read property 'text' of undefined”，找到一个 issue 提了这个问题，给出的解决方法是在 Summary 中去掉了空行。我这并不奏效。

在这个过程中会发现 GitBook 的使用不知不觉已经会了，而这时候你发现你接着需要学习的是 [Markdown]***等md写好后在这里插入教程链接***。

### 三. 关联两者
#### 1.确认已经在 GitHub 中建立了库。
#### 2.确认已经在 GitBook 中建立了 book 。
#### 3.关联库和 book 。
## 思路小结
经过上面三个大步骤你会发现 GitHub 和 GitBook 的关联已经完成了。

也许你会说，这么笼统的教程谁能懂呢？确实，这只是希望能以程序员思维自居的我写的一个解决思路，抵达终点的路程当然磕磕碰碰，到处找教程、到处碰壁。作为一个新入门的学习者自然有非常多的细节不明白，我也是那样过来的，所以我准备了具体步骤。

但我仍然希望你能够按照上面的思路自己折腾一遍，这样也许你以后遇到问题就能够首先分解为几个大步骤，每个步骤再进行分解，逐一找到解决的办法，就像编程过程中程序员遇到问题时写方法和调用方法一样。

沿着这个思路，当你还是会遇到没有办法解决的问题时，那通常已经是一个非常细节的问题，任何一个过来人都能明白你的问题出在哪里并帮你指出来，而不是同样一头雾水，无法帮助你。
## 具体步骤
### 1. 注册并登陆 [GitHub](https://github.com) 。 
### 2. 新建一个库，右上方的＋号下拉，点击 New repository。  ![](http://img1.ph.126.net/4AGpUv1W8KddYm52Gcyjzw==/6630391566047723290.jpg) 


** 取一个炫酷的库名，我用 name做示范。 **


![](http://img2.ph.126.net/pfmPEdOI6m6Leb4_ejbD0g==/2452772947074564263.jpg)


** 点击 Create repository 你就得到了一个你命名的库。 **


![](http://img1.ph.126.net/IeTAhgj-Nq2eMJoooTq3Xw==/3360811222027360864.jpg)  


### 3. 用 GitHub 登陆 GitBook 。


### 4. 验证邮箱。右上角下拉，点击 Accout Setting 。


![](http://img0.ph.126.net/3jdkOyxGOI8Md8o2nkTiFw==/661747670264676873.png)  


** 输入邮箱和自己设定的密码，点击左下角 Save 。验证过邮箱中 GitBook 发送的邮件后，会得到'This email is verified.'的信息。 **


![](http://img0.ph.126.net/TH0h8NSpqT5JqQJBNvMb8g==/6599272088448547215.jpg)



### 5.新建一个 book ，右上方的＋号或＋Creat a new book 。 ![](http://img1.ph.126.net/YR01nW8cRDrMTN25PDNmQg==/646829496499017793.jpg)    


** 取一个炫酷的名字，我用的是和待关联库相同的名字name 。 **


![](http://img2.ph.126.net/5YL3UsKNC9fcCbBYMRJW8g==/6599273187960174962.jpg) 


** 点击 Create book 你得到了一个你命名的 book 。 **


### 6.关联刚刚新建的库，点击 Link to GitHub 。

![](http://img1.ph.126.net/ovoXWu-grJy11mOXZocqXg==/6619368961979988001.jpg) 


** 输入 ‘你的 GitHub 账户名／库名’，点击右下角 Save。 **


![](http://img2.ph.126.net/cyyogF0Jn6vMc2mjPF8nNg==/3096787693788560714.jpg) 


** 会得到如图 ' Book configuration has been updated!'信息。 **


![](http://img2.ph.126.net/hL3gZV_-n2pUqlcqu02bqA==/6608237506261334228.jpg)

### 7.点击 Edit 开始写你的 book 吧。保存并你打开 GitHub 中的库，会发现你所编辑的内容已经同步到 README.md 中了。

### 8.手动解决不同步问题
原因：
- gitbook 的图书仓库和 github 源内容仓库无法自动同步
- gitbook 有可接触的 git 仓库
- gitbook 的图书仓库,没有 github 仓库那些丰富的管理/分享/传播功能

目标:

- 希望原先图书管理流程不变
- github 仓库专注图书的管理/编辑/协同...
- gitbook 专注图书的编译/发布

所以:

- 人工解决 github 和 gitbook 仓库不同步问题
- 同时/接连 将图书内容 push 到两个仓库就好!


#### 技术上

`github`

- 使用 ssh 认证, 不用口令
- 通过 git/ssh 协议高速交互

`gitbook`

- 只能使用 https 协调交互
- 只能使用 明文 帐号+口令 认证
- 如果,图书发布 URI 是:
    + `https://www.gitbook.com/book/[帐号]/[图书名]/details`
    + 则对应的仓库应该是:
    + `https://git.gitbook.com/[帐号]/[图书名].git`


### 操作上

- 已经创建好 github 图书仓库, gitbook 图书实例
- 并将 github 仓库 clone 到本地: `/path/2/[图书名]`
- 则应该可以看到 `/path/2/[图书名]/.git/config` 有以下配置声明


```
[remote "origin"]
    url = git@github.com:OpenMindClub/[图书名].git
    fetch = +refs/heads/*:refs/remotes/origin/*
```

- 那么就可以手工增订为:

```
[remote "book"]
    url = https://git.gitbook.com/[帐号]/[图书名].git
    fetch = +refs/heads/*:refs/remotes/origin/*
[remote "hub"]
    url = git@github.com:OpenMindClub/[图书名].git
    fetch = +refs/heads/*:refs/remotes/origin/*
[remote "origin"]
    url = git@github.com:OpenMindClub/[图书名].git
    fetch = +refs/heads/*:refs/remotes/origin/*
```

- 回到仓库根目录,测试:

```
$ git remote -v
book    https://git.gitbook.com/[gitbook帐号]/[图书名].git (push)
book    https://git.gitbook.com/[gitbook帐号]/[图书名].git (fetch)
hub git@github.com:[github账号]/[图书名].git (push)
hub git@github.com:[github账号]/[图书名].git (fetch)
origin  git@github.com:[github账号]/[图书名].git (push)
origin  git@github.com:[github账号]/[图书名].git (fetch)
```



#### 手工双推

用两次 git 操作,完成两个仓库的内容发送:

```
$ git pu hub
Counting objects: 18, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (15/15), done.
Writing objects: 100% (16/16), 3.29 KiB | 0 bytes/s, done.
Total 16 (delta 3), reused 0 (delta 0)
To git@github.com:OpenMindClub/[图书名].git
   8c3c8b6..f27428a  master -> master

$ git pu book
Counting objects: 20, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (15/15), done.
Writing objects: 100% (16/16), 3.29 KiB | 0 bytes/s, done.
Total 16 (delta 3), reused 0 (delta 0)
To https://[用户名]:[口令]@git.gitbook.com/[帐号]/[图书名].git
   8c3c8b6..f27428a  master -> master

```

