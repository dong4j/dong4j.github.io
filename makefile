# 定义伪目标，避免与文件名冲突
.PHONY: convert_and_rename upload_images clean_images replace_summary_and_tags push deploy-m920x deploy-github clean

########## 需要终端在 hexo 顶层目录才能正常执行

init:
	@echo "==================Step 0: 将修改的文件拷贝到原路径=================="
	npm install && cp js/hexo-renderer-marked/lib/renderer.js ./node_modules/hexo-renderer-marked/lib/renderer.js

# 本地运行
dev: 
	@echo "==================Step 5: Deploying application=================="
	hexo clean && hexo generate --config _config.yml,_config.anzhiyu.yml,_config.local.yml && hexo server --config _config.yml,_config.anzhiyu.yml,_config.local.yml

# 默认目标
all: convert_and_rename upload_images clean_images replace_summary_and_tags push deploy-m920x deploy-github clean


# 将图片转换为 webp 且重命名(年月日时分秒_8位随机字符串.webp)
convert_and_rename: 
	@echo "==================Step 2: Cleaning images=================="
	python script/convert_and_rename.py

# 上传图片
upload_images: 
	@echo "==================Step 3: Cleaning images=================="
	python script/upload_images.py

# 删除未被引用的图片, 不传任何参数则全部处理, 传 2023 则只处理 2023 目录下的文件, 传 md 文件名, 则只处理这一个文件
clean_images:
	@echo "==================Step 1: Cleaning images=================="
	python script/clean_images.py

# 生成摘要和标签
replace_summary_and_tags: 
	@echo "==================Step 3: Cleaning images=================="
	python script/replace_summary_and_tags.py 

# 执行 git-push.sh
push: 
	@echo "==================Step 4: Pushing changes to Git=================="
	script/git-push.sh "添加文档"

# 执行 deploy.sh
deploy-m920x: push
	@echo "==================Step 5: Deploying application=================="
	script/deploy.sh

# 发布到 github
deploy-github: push
	@echo "==================Step 6: Deploying Github=================="
	hexo deploy --config _config.yml,_config.anzhiyu.yml,_config.publish.yml

deploy-all: deploy-m920x deploy-github

clean:
	@echo "==================Step 7: Cleaning up=================="
	hexo clean && rm -rf .deploy_git


# 2025-01-02 自动化部署
2025-01-02: replace_summary_and_tags convert_and_rename upload_images clean_images push deploy-m920x deploy-github clean

# 打印当前执行的目录
print-curdir:
	@echo Current directory is $(CURDIR)