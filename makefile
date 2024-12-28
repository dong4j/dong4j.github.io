# 定义伪目标，避免与文件名冲突
.PHONY: all process push deploy

# 默认目标
all: process push deploy clean

# 执行 images_process.py
process:
	@echo "Step 1: Processing images..."
	python images_process.py

# 执行 git-push.sh
push: process
	@echo "Step 2: Pushing changes to Git..."
	./git-push.sh

# 执行 deploy.sh
deploy-m920x: push
	@echo "Step 3: Deploying application..."
	./deploy.sh

deploy-github: push
	@echo "Step 4: Deploying Github..."
	hexo deploy

clean:
	@echo "Step 5: Cleaning up..."
	hexo clean && rm -rf .deploy_git