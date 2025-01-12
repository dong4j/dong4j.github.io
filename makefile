# 定义伪目标，避免与文件名冲突
.PHONY: image_convert image_upload image_clean replace_summary_and_tags commit-all deploy-m920x deploy-github clean

# 打印当前执行的目录
print-curdir:
	@echo Current directory is $(CURDIR)
	
########## 安装 vscode-makefile-term 插件

init:
	@echo "==================Step 0: 将修改的文件拷贝到原路径=================="
	nvm use 21 && rm -rf node_modules && npm install && cp -f dependencies/hexo-renderer-marked/lib/renderer.js ./node_modules/hexo-renderer-marked/lib/renderer.js

# 本地运行
local: 
	@echo "==================Step 5: Deploying application=================="
	hexo clean && hexo generate --config _config.yml,_config.anzhiyu.yml,_config.local.yml && hexo server --config _config.yml,_config.anzhiyu.yml,_config.local.yml

	# 本地运行
prod: 
	@echo "==================Step 5: Deploying application=================="
	hexo clean && hexo generate --config _config.yml,_config.anzhiyu.yml,_config.publish.yml && hexo server --config _config.yml,_config.anzhiyu.yml,_config.publish.yml

# 将图片转换为 webp 且重命名(年月日时分秒_8位随机字符串.webp)
image_convert: 
	@echo "==================Step 1: Convert images=================="
	python script/image_convert.py 

# 上传图片
image_upload: 
	@echo "==================Step 2: Upload images=================="
	python script/image_upload.py 

# 删除未被引用的图片, 不传任何参数则全部处理, 传 2023 则只处理 2023 目录下的文件, 传 md 文件名, 则只处理这一个文件
image_clean:
	@echo "==================Step 3: Cleaning images=================="
	python script/image_clean.py 

# 生成摘要和标签
replace_summary_and_tags: 
	python script/replace_summary_and_tags.py 

# 替换文章分类
replace_category: 
	python script/replace_category.py 

# 替换文章标题
replace_title: 
	python script/replace_title.py 

compress_static:
	script/compress_static.sh && script/upload_by_piclist.sh ../source/min COS-Blog-Static 

###################################### commit-dependencies #########################################

commit-github-homepage:
	dependencies/github-homepage/git-commit.sh || true

commit-equipment-materials:
	dependencies/equipment-materials/git-commit.sh "更新图片" || true

commit-npxcard:
	dependencies/npx-card/git-commit.sh "update" || true

commit-homepage:
	dependencies/deo-homepage/git-commit.sh "更新主页" || true

commit-wechatoa:
	dependencies/wechat-official-account-web/git-commit.sh "更新页面" || true

commit-overseasban:
	dependencies/overseas-ban/git-commit.sh "更新页面" || true

commit-starlist:
	dependencies/self-star-list/git-commit.sh "更新模版" || true

commit-workflow:
	dependencies/workflow/script/git-commit.sh "Update" || true

commit-dependencies: commit-github-homepage commit-equipment-materials commit-npxcard commit-homepage commit-wechatoa commit-overseasban commit-starlist commit-workflow
###################################### commit-dependencies #########################################

commit-theme:
	themes/anzhiyu/git-commit.sh "修改加载页面显示时间" || true

commit-hexo:
	script/git-commit.sh "更新状态页链接" && python script/update_log.py || true

# 重置忽略文件: git rm -r --cached .
commit-all: commit-dependencies commit-theme  commit-hexo

###################################### deploy-dependencies #########################################
upload-equipment-materials:
	dependencies/equipment-materials/convert_and_upload.sh || true

deploy-wechatoa: 
	dependencies/wechat-official-account-web/deploy.sh || true

deploy-overseasban:
	dependencies/overseas-ban/deploy.sh || true

deploy-starlist: 
	dependencies/self-star-list/deploy.sh || true

# homepage.dong4j.ink:3332
deploy-homepage: 
	dependencies/deo-homepage/deploy.sh m920x /opt/1panel/apps/openresty/openresty/www/sites/homepage.dong4j.ink/index

deploy-dependencies: upload-equipment-materials deploy-wechatoa deploy-overseasban  deploy-starlist deploy-homepage 
###################################### deploy-dependencies #########################################

# blog.dong4j.ink:3222
deploy-m920x: 
	script/deploy.sh m920x /opt/1panel/apps/openresty/openresty/www/sites/blog.dong4j.ink/index

deploy-aliyun: 
	script/deploy.sh aliyun /var/www/blog

# 发布到 github
deploy-github: 
	hexo deploy --config _config.yml,_config.anzhiyu.yml,_config.publish.yml

deploy-all: deploy-dependencies deploy-m920x deploy-aliyun deploy-github

deploy-workflow: all

clean:
	@echo "==================Step 7: Cleaning up=================="
	hexo clean && rm -rf .deploy_git && rm -rf db.json && rm -rf _multiconfig.yml

all: clean image_convert image_upload image_clean compress_static commit-all deploy-all clean
