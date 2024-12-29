# 定义伪目标，避免与文件名冲突
.PHONY: all clean_images convert_and_rename upload_images push deploy

# 默认目标
all: clean_images convert_and_rename upload_images push deploy clean

# 删除未被引用的图片, 不传任何参数则全部处理, 传 2023 则只处理 2023 目录下的文件, 传 md 文件名, 则只处理这一个文件
clean_images:
	@echo "==================Step 1: Cleaning images=================="
	python script/clean_images.py

# 将图片转换为 webp 且重命名(年月日时分秒_8位随机字符串.webp)
convert_and_rename:
	@echo "==================Step 2: Cleaning images=================="
	python script/convert_and_rename.py

# 上传图片
upload_images:
	@echo "==================Step 3: Cleaning images=================="
	python script/upload_images.py

# 执行 git-push.sh
push: 
	@echo "==================Step 4: Pushing changes to Git=================="
	script/git-push.sh

# 执行 deploy.sh
deploy-m920x: push
	@echo "==================Step 5: Deploying application=================="
	script/deploy.sh

deploy-github: push
	@echo "==================Step 6: Deploying Github=================="
	hexo deploy

clean:
	@echo "==================Step 7: Cleaning up=================="
	hexo clean && rm -rf .deploy_git