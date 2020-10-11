# 1 初映像

- 速度
- 简单的设计
- 对非线性开发模式的强力支持（允许成千上万个并行开发的分支）
- 完全分布式
- 有能力高效管理类似 Linux 内核一样的超大规模项目（速度和数据量）

在 Git 中，每当你提交更新或保存项目状态时，它基本上就会对当时的全部文件创建一个快照并保存这个快照的索引。Git 对待数据更像是一个 **快照流**。 Git 更像是一个小型的文件系统，提供了许多以此为基础构建的超强工具，而不只是一个简单的 VCS。

#### 近乎所有操作都是本地执行

#### Git 保证完整性

#### Git 一般只添加数据

#### 三种状态

Git 有三种状态，你的文件可能处于其中之一： **已提交（committed）**、**已修改（modified）** 和 **已暂存（staged）**。

- 已修改表示修改了文件，但还没保存到数据库中。
- 已暂存表示对一个已修改文件的当前版本做了标记，使之包含在下次提交的快照中。
- 已提交表示数据已经安全地保存在本地数据库中。

基本的 Git 工作流程如下：

1. 在工作区中修改文件。
2. 将你想要下次提交的更改选择性地暂存，这样只会将更改的部分添加到暂存区。
3. 提交更新，找到暂存区的文件，将快照永久性存储到 Git 目录。



# 2 Git基础

#### 获得仓库

```
cd G:/Literature
cd/    # 返回根目录
cd..    # 返回上一级
```

- 初始化

```
git init
```

- 克隆

```
git clone https://github.com/libgit2/libgit    # 创建libgit2仓库
```

```
git clone https://github.com/libgit2/libgit2 mylibgit    # 创建mylibgit仓库
```

#### 仓库状态

```
git status
git status -s #简版
```

#### 常用操作

```
git add filename.xx    # 跟踪新文件 & 暂存已修改文件
git rm                 # Git中移除文件，并在本地删除指定文件
git rm --cached        # Git不继续追踪，本地保留
git rm log/\*.log      # glob模式，删除log/目录下扩展名为.log的所有文件
git diff               # 当前与暂存
git diff --staged(or cached) # 暂存与上次提交
```

#### 提交更新

```
git commit -m "Messages."    
git commit -a                # 跳过暂存区
```

#### 查看提交历史

```
git log
git log -p    # 补丁格式，显示diff
--stat       # 显示提交信息
--pretty=online    # 格式：online, short, full, fuller, format
-2    # 显示最近n条
--since/after="2008-10-01" / =2.weeks
--author="JiangYuYan"
--before/until="2008-10-01"
--no-merges    # 隐藏合并提交
```

#### 撤销操作

```
git commit -m 'initial commit'
git add forgotten_file
git commit --amend       # 最终只有一个提交即第二次的
```

```
git reset HEAD CONTRIBUTING.md    # 取消暂存
git checkout -- CONTRIBUTING.md    # 撤销对文件的修改
```

#### 远程仓库的使用

```
git remote    # 显示远程仓库服务器简写
git remote -v    # 简写和URL
git remote add <shortname> <URL>    # 添加远程仓库
git fetch <remote>    # 访问远程仓库，拉取本地还没有的数据
git merge <remote>/<branch>    # 合并分支到本地
git pull    # 如果当前分支设置了跟踪远程分支，自动抓取后合并该远程分支到当前分支
git push <remote> <branch>    # 将本地分支推送到远程仓库
git remote show <remote>    # 查看某一个远程仓库信息
git remote show
git remote rename <remote> <newname>    # 重命名
git remote remove <remote>    # 移除
```

#### 打标签

```
git tag    # 显示标签
git tag v1.0    # 轻量标签
git tag -a v1.4 -m "my version 1.4"    # 附注标签
git show v1.4    # 标签信息与提交信息
git tag -a v1.2 9fceb02    # 补打标签，末尾加校验和
git push origin v1.5    # 需显式推送标签到共享服务器上
git push origin --tags    # 不在远程仓库中的标签都传送上去
git tag -d v1.4    # 删除本地仓库上的标签
git push <remote> :refs/tags/<tagname> # 将将冒号前面的空值推送到远程标签名，高效地删除它
git push origin --delete <tagname>    # 删除远程标签
```

