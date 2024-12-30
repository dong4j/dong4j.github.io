---
title: 为 rm 添加回收站
keywords:
  - Linux
categories:
  - Linux
tags:
  - bash-script
  - file-management
  - system-tools
  - command-line-utility
abbrlink: ae39e951
date: 2014-08-09 00:00:00
ai:
  - 这是一个用于在Linux系统中替代标准`rm`命令的脚本，称为`rmtrash`。该脚本可以将指定文件移动到一个名为`trash`的目录下（默认位于根目录），而不是直接删除它们，从而为用户提供回收站功能来恢复意外删除的文件。用户可以通过各种选项操作文件：查看已删除文件日志、从回收站恢复文件、清空整个回收站或选择性删除回收站中的文件。脚本还支持别名`rm`以简化命令使用，使得在系统中执行文件删除操作更为便捷和安全。
description: 这是一个用于在Linux系统中替代标准`rm`命令的脚本，称为`rmtrash`。该脚本可以将指定文件移动到一个名为`trash`的目录下（默认位于根目录），而不是直接删除它们，从而为用户提供回收站功能来恢复意外删除的文件。用户可以通过各种选项操作文件：查看已删除文件日志、从回收站恢复文件、清空整个回收站或选择性删除回收站中的文件。脚本还支持别名`rm`以简化命令使用，使得在系统中执行文件删除操作更为便捷和安全。
---

在 Linux 系统中，`rm` 命令是一个非常强大的工具，它可以永久删除文件和目录。然而，这种强大的能力也带来了风险，因为一旦文件被删除，就很难恢复。为了防止因误操作而丢失重要数据，我们可以创建一个自定义的回收站来保存被删除的文件。以下是实现这一功能的详细步骤和脚本。

## 背景

作为 Ubuntu 的用户，我们经常需要在命令行下执行文件删除操作。但是，命令行下的 `rm` 命令一旦执行，被删除的文件几乎不可能恢复。为了避免这种情况，我们编写了一个简单的脚本，将删除操作改为移动操作，从而实现了一个类似于 Windows 系统中回收站的功能。

## 脚本介绍

下面提供的脚本 `rmtrash` 可以作为 `rm` 命令的替代品。它将用户指定的文件或目录移动到一个特定的“回收站”目录中，而不是直接删除它们。这样，如果需要，用户可以从回收站中恢复这些文件。

### 脚本功能

- **移动文件到回收站**：而不是直接删除文件，脚本会将它们移动到用户家目录下的 `.rmtrash/` 目录。
- **记录删除操作**：脚本会记录所有删除操作的详细信息，包括删除的文件路径和时间，以便于恢复。
- **恢复文件**：可以从回收站中恢复文件到原始位置。
- **清空回收站**：当确认不再需要回收站中的文件时，可以清空回收站。
- **查看回收站内容**：可以列出回收站中的所有文件和目录。
- **详细日志**：可以查看已删除文件的详细日志。

## 脚本

```shell
#!/bin/bash

###trash目录define
realrm="/bin/rm"
trash_dir=~/.rmtrash/
trash_log=~/.rmtrash.log
###判断trash目录是否存在，不存在则创建
if [ ! -d $trash_dir ] ;then
	mkdir -v $trash_dir
fi

####function define
###usage function
rm_usage () {
	cat <<EOF
Usage1: `basename $0` file1 [file2] [dir3] [....] 删除文件或目录, 并将它们移动到 rmtrash 回收站
Usage2: rm         file1 [file2] [dir3] [....] 删除文件或目录, 并将它们移动到 rmtrash 回收站
        rm is alias to `basename $0`.
options:
	-f  移动一个或多个文件到 rmtrash 回收站
	-r  移动一个或多个文件到 rmtrash 回收站
	-fr 移动一个或多个文件到 rmtrash 回收站
	-rf 移动一个或多个文件到 rmtrash 回收站
	-R  将所选文件从 rmtrash 回收站恢复到原路径
	-l  列出 rmtrash 回收站的内容
	-i  显示已删除文件历史的详细日志
	-d  根据用户输入的文件名从回收站删除一个或多个文件
	-e  清空 rmtrash 回收站
	-h  显示此帮助菜单
EOF
}


###rm mv function
rm_mv () {
	echo ----------------------------
	now=`date +%Y%m%d_%H:%M:%S`
	dupfix=.`date +%Y%m%d%H%M%S`
	###将用户输入的文件循环mv到trash中
	###for file in $file_list ;do
		#echo $file
		###提取用户输入参数的文件名、目录名，拼出绝对路径
		file_name=`basename $file`
		file_dir=$(cd `dirname $file`;pwd)
		file_fullpath=$file_dir/$file_name
		###判断要删除的文件或者目录大小是否超过2G
		#echo file_fullpath: $file_fullpath
		#if [[ "$file_fullpath" == "/*" ]];then
		#	echo action deny!
		#else
		####判断即将删除的文件在trash目录里是否已存在
		if [[ `ls $trash_dir|grep ^${file_name}$` ]];then
			##已存在，文件名重复，需要rename，想原始名的基础上加后缀
			trash_dest_path=$trash_dir$file_name$dupfix
			echo trash目录里已存在$file_name,需要rename $file_name$dupfix
		else
			##不重名，直接按原始文件名保存
			trash_dest_path=$trash_dir$file_name
		fi
			###mv成功记录log,记录删除时的文件、目录的路径等信息到log，以便恢复数据
			mv $file_fullpath $trash_dest_path && \
			echo $now `whoami` moved from $file_fullpath to $trash_dest_path >> $trash_log && \
			echo -e "\033[31m\033[05m $file 从 $file_fullpath 被删除\033[0m"
			#cat $trash_log
		#fi
	###done
}

###rm list function
rm_list () {
	echo ----------------------------
	echo list trash_dir contents:
	ls $trash_dir
}


###rm restore function
rm_restore () {
	echo ----------------------------
	echo -en "请选择要恢复的文件名(多个文件中间空格分隔,取消ctl+c):"
	read reply
	for file in $reply ;do
		###判断原始位置的是否有同名文件存在
		originalpath=`cat $trash_log|grep /$file$|awk  '{print $5}'`
		if [[ `ls $originalpath` ]];then
			echo -en "originalpath:$originalpath 已经存在。是否继续覆盖(y/n):"
			read ack
			if   [[ $ack == y ]];then
				echo restore:
			elif [[ $ack == n ]];then
				echo bye && exit
			else
				echo 输入非法 && exit
			fi
		fi
		###
		mv $trash_dir$file  $originalpath && \
		###linux和mac下sed的用法有细微差别，故需通过操作系统类型进行选择对应的sed格式
		if [[ $os_type == Darwin ]];then
			sed -i .bak "/\/$file$/d" $trash_log
			echo os_type=Darwin
		elif [[ $os_type == Linux ]];then
			sed -i.bak "/\/$file$/d" $trash_log
			echo os_type=Linux
		fi && \
		echo -e  "\033[32m\033[05m$file 从 $originalpath 恢复成功\033[0m"
	done
}

### rm show delete log function
rm_infolog () {
	echo ----------------------------
	echo detailed deleted file log:
	cat $trash_log
}


###rm empty trash function
rm_empty () {
	echo ----------------------------
	echo -en "空回收站，回收站中的所有备份将被删除，是否继续(y/n):"
	read ack
	if   [[ $ack == y ]];then
		echo begin to empty trash:
	elif [[ $ack == n ]];then
		echo bye && exit
	else
		echo 输入非法 && exit
	fi
	/bin/rm -fr ${trash_dir} && \
	echo >$trash_log && \
	echo -e "\033[31m\033[05m 垃圾桶已经被清空了\033[0m"
}

###rm delete function
rm_delete () {
	echo ----------------------------
	echo -en "请选择trash中要删除的文件名(多个文件中间空格分隔,取消ctl+c):"
	read reply
		for file in $reply ;do
			###if file exist then delete it from trash
			if [[ `ls ${trash_dir}$file` ]];then
				/bin/rm -fr ${trash_dir}$file && \
				###linux和mac下sed的用法有细微差别，故需通过操作系统类型进行选择对应的sed格式
				if [[ $os_type == Darwin ]];then
					sed -i .bak "/\/$file$/d" $trash_log
					echo os_type=Darwin
				elif [[ $os_type == Linux ]];then
					sed -i.bak "/\/$file$/d" $trash_log
					echo os_type=Linux
				fi && \
					echo -e  "\033[32m\033[05m$file 从 ${trash_dir}$file 被删除\033[0m"
			else
				echo $file is not exist in $trash_dir
			fi
		done
}


###跨分区的问题

#####主程序开始
###参数个数为0，输出help
if [ $# -eq 0 ] ;then rm_usage ;fi
###根据用户输入选项执行相应动作
###通过非显示的方式(加入fr选项，但在case里不做匹配操作，遇到含-fr/-rf/-f/-r时直接删除)支持很多用户的使用习惯rm -fr file,rm -rf file
while getopts lRiedhfr option ;do
case "$option" in
		l) rm_list;;
		R) rm_list
		   rm_restore;;
		i) rm_infolog;;
		h) rm_usage;;
		e) rm_empty;;
		d) rm_list
		   rm_delete;;
		\?)rm_usage
		   exit 1;;
	esac
done
shift $((OPTIND-1))

###将文件名的参数依次传递给rm_mv函数
while [ $# -ne 0 ];do
	file=$1
	echo file=$file
	rm_mv
	shift
done

```

### 安装脚本

1. 将上面的脚本保存为一个文件，例如 `rmtrash`。
2. 将该脚本移动到 `/usr/local/bin/` 目录下，使其全局可执行：

   ```bash
   sudo mv rmtrash /usr/local/bin/
   sudo chmod +x /usr/local/bin/rmtrash
   ```

3. 使用别名替换原 `rm` 命令：

   ```bash
   alias rm='rmtrash'
   ```

   将上述别名添加到你的 `.bashrc` 或 `.bash_profile` 文件中，以便在每次登录时自动设置。

### 使用脚本

现在，你可以像使用 `rm` 命令一样使用 `rmtrash`。例如，删除一个文件：

```bash
rm file.txt
```

这将把 `file.txt` 移动到回收站，而不是直接删除它。

### 恢复文件

如果你想从回收站恢复文件，可以使用 `-R` 选项：

```bash
rm -R file.txt
```

这将提示你选择要恢复的文件。

### 清空回收站

当你确定回收站中的文件不再需要时，可以使用 `-e` 选项清空回收站：

```bash
rm -e
```
