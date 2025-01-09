# 定义伪目标，避免与文件名冲突
.PHONY: image_convert image_upload image_clean replace_summary_and_tags commit-all deploy-m920x deploy-github clean

# 打印当前执行的目录
print-curdir:
	@echo Current directory is $(CURDIR)
	
########## 安装 vscode-makefile-term 插件

init:
	@echo "==================Step 0: 将修改的文件拷贝到原路径=================="
	npm install && cp -f js/hexo-renderer-marked/lib/renderer.js ./node_modules/hexo-renderer-marked/lib/renderer.js

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
	script/compress_static.sh && script/upload_by_piclist.sh /Users/dong4j/Developer/3.Knowledge/site/hexo/source/min COS-Blog-Static 

update-js:
	script/compress_js.sh && script/upload_by_piclist.sh /Users/dong4j/Developer/3.Knowledge/site/hexo/source/min COS-Blog-Static 

updste-css:
	script/compress_css.sh && script/upload_by_piclist.sh /Users/dong4j/Developer/3.Knowledge/site/hexo/source/min COS-Blog-Static 

commit-github-homepage:
	github-homepage/git-commit.sh

commit-equipment-materials:
	equipment-materials/git-commit.sh "更新图片"

commit-theme:
	themes/anzhiyu/git-commit.sh "更新页面"

commit-homepage:
	deo-homepage/git-commit.sh "更新主页"

commit-wechatoa:
	wechat-official-account-web/git-commit.sh "更新页面"

commit-overseasban:
	overseas-ban/git-commit.sh "更新页面"

commit-starlist:
	self-star-list/git-commit.sh "更新模版" || true

commit-workflow:
	workflow/script/git-commit.sh "更新脚本"

commit-hexo:
	script/git-commit.sh "脚本大满贯"

# 重置忽略文件: git rm -r --cached .
commit-all: commit-equipment-materials commit-theme commit-homepage commit-wechatoa commit-overseasban commit-starlist commit-workflow commit-hexo

upload-equipment-materials:
	equipment-materials/convert_and_upload.sh || true

deploy-wechatoa: 
	wechat-official-account-web/deploy.sh

deploy-overseasban:
	overseas-ban/deploy.sh

deploy-starlist: 
	self-star-list/deploy.sh

# homepage.dong4j.ink:3332
deploy-homepage: 
	deo-homepage/deploy.sh m920x /opt/1panel/apps/openresty/openresty/www/sites/homepage.dong4j.ink/index

# blog.dong4j.ink:3222
deploy-m920x: 
	script/deploy.sh m920x /opt/1panel/apps/openresty/openresty/www/sites/blog.dong4j.ink/index

deploy-aliyun: 
	script/deploy.sh aliyun /var/www/blog

# 发布到 github
deploy-github: 
	hexo deploy --config _config.yml,_config.anzhiyu.yml,_config.publish.yml

deploy-all: upload-equipment-materials deploy-wechatoa deploy-overseasban deploy-homepage deploy-starlist deploy-m920x deploy-aliyun deploy-github

deploy-workflow: all

clean:
	@echo "==================Step 7: Cleaning up=================="
	hexo clean && rm -rf .deploy_git && rm -rf db.json && rm -rf _multiconfig.yml

all: image_convert image_upload image_clean compress_static commit-all deploy-all clean