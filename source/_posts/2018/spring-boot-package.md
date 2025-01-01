---
title: 定制你的Spring Boot：探索maven-assembly-plugin
categories:
  - Java
tags:
  - Maven
  - Spring Boot
  - 自动化构建
  - zip打包
  - maven-assembly-plugin
abbrlink: d16c10eb
date: 2018-05-12 00:00:00
ai:
  - 本文介绍了从手动到自动化的Spring Boot项目打包过程。主要内容包括：1）利用特定配置启动和调试应用；2）使用maven插件管理依赖库与资源配置；3）调整资源路径排除特定文件，如不在类路径下放置`application.yml`；4）通过maven-assembly-plugin自定义构建过程，将资源、依赖及配置整合成zip或单个jar包；5）最终实现全自动化打包流程。文章旨在简化Spring
    Boot项目的部署与发布步骤，提高开发和运维效率。
description: 本文介绍了从手动到自动化的Spring Boot项目打包过程。主要内容包括：1）利用特定配置启动和调试应用；2）使用maven插件管理依赖库与资源配置；3）调整资源路径排除特定文件，如不在类路径下放置`application.yml`；4）通过maven-assembly-plugin自定义构建过程，将资源、依赖及配置整合成zip或单个jar包；5）最终实现全自动化打包流程。文章旨在简化Spring
  Boot项目的部署与发布步骤，提高开发和运维效率。
---

## fat jar

## tomcat

## 自定义打包部署 暴露配置文件和静态资源文件

### 前言

SpringBoot 默认有 2 种打包方式，一种是直接打成 jar 包，直接使用 java -jar 跑起来，另一种是打成 war 包，移除掉 web starter 里的容器依赖，然后丢到外部容器跑起来。

第一种方式的缺点是整个项目作为一个 jar，部署到生产环境中一旦有配置文件需要修改，则过程比较麻烦  
linux 下可以使用 vim jar 包，找到配置文件修改后再保存  
window 下需要使用 解压缩软件打开 jar 再找到配置文件，修改后替换更新

第二种方式的缺点是需要依赖外部容器，这无非多引入了一部分，很多时候我们很不情愿这么做

> spring boot 项目启动时 指定配置有 2 种方式：一种是启动时修改配置参数，像 java -jar xxxx.jar –server.port=8081 这样；另外一种是 指定外部配置文件加载，像 java -jar xxxx.jar -Dspring.config.location=applixxx.yml 这样

### 目标

我们希望打包成 tomcat 或者 maven 那样的软件包结构，即

```
--- bin
    --- start.sh
    --- stop.sh
    --- restart.sh
    --- start.bat
    --- stop.bat
    --- restart.bat
--- boot
    --- xxxx.jar
--- lib
--- conf
--- logs
--- README.md
--- LICENSE
```

- `bin`  目录放一些我们程序的启动停止脚本
- `boot`  目录放我们自己的程序包
- `lib`  目录是我们程序的依赖包
- `conf`  目录是项目的配置文件
- `logs`  目录是程序运行时的日志文件
- `README.md`  使用说明
- `LICENSE`  许可说明

### 准备

- maven-jar-plugin ： 打包我们写的程序包和所需的依赖包，并指定入口类，依赖包路径和 classpath 路径，其实就是在 MANIFEST.MF 这个文件写入相应的配置
- maven-assembly-plugin ： 自定义我们打包的文件目录的格式

### pom.xml 配置

```xml
<build>
    <plugins>
        <!--<plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <fork>true</fork>
            </configuration>
        </plugin>-->

        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-jar-plugin</artifactId>
            <configuration>
                <archive>
                    <addMavenDescriptor>false</addMavenDescriptor>
                    <manifest>
                        <mainClass>com.ahtsoft.AhtsoftBigdataWebApplication</mainClass>
                        <addClasspath>true</addClasspath>
                        <classpathPrefix>../lib/</classpathPrefix>
                    </manifest>
                    <manifestEntries>
                        <Class-Path>../conf/resources/</Class-Path>
                    </manifestEntries>
                </archive>
                <excludes>
                    <exclude>static/**</exclude>
                    <exclude>*.yml</exclude>
                </excludes>
            </configuration>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-assembly-plugin</artifactId>
            <configuration>
                <descriptors>
                    <descriptor>src/main/assembly/assembly.xml</descriptor>
                </descriptors>
            </configuration>
            <executions>
                <execution>
                    <phase>package</phase>
                    <goals>
                        <goal>single</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

1. 将 spring boot 默认的打包方式 spring-boot-maven-plugin 去掉，使用现在的打包方式
2. maven-jar-plugin 配置中，制定了入口类，addClasspath 配置将所需的依赖包单独打包，依赖包打的位置在 lib 目录底下，在 MANIFEST.MF 这个文件写入相应的配置
3. 配置了 classpath 在 /conf/resources/ ,这个和后面的 assembly.xml 要相对应
4. 我单独把 spring boot 的配置文件 yml 文件 和 静态资源目录 static 单独拎了出来，在我们的源码包中并没有打进去，而是交给 assembly.xml 来单独打到一个独立的文件 conf 文件下
5. 这也是照应了 前面为什么要设置 classpath 为 /conf/resources/

下面重要的是 assembly.xml 配置文件了，这个文件才是把我们的程序打成标准的目录结构

### assembly.xml

```xml
<assembly>
    <id>assembly</id>
    <formats>
        <format>tar.gz</format>
    </formats>
    <baseDirectory>${project.artifactId}-${project.version}/</baseDirectory>

    <files>
        <file>
            <source>target/${project.artifactId}-${project.version}.jar</source>
            <outputDirectory>boot/</outputDirectory>
            <destName>${project.artifactId}-${project.version}.jar</destName>
        </file>
    </files>

    <fileSets>
        <fileSet>
            <directory>./</directory>
            <outputDirectory>./</outputDirectory>
            <includes>
                <include>*.txt</include>
                <include>*.md</include>
            </includes>
        </fileSet>
        <fileSet>
            <directory>src/main/bin</directory>
            <outputDirectory>bin/</outputDirectory>
            <includes>
                <include>*.sh</include>
                <include>*.cmd</include>
            </includes>
            <fileMode>0755</fileMode>
        </fileSet>
        <fileSet>
            <directory>src/main/resources/static</directory>
            <outputDirectory>conf/resources/static/</outputDirectory>
            <includes>
                <include>*</include>
            </includes>
        </fileSet>
        <fileSet>
            <directory>src/main/resources</directory>
            <outputDirectory>conf/resources</outputDirectory>
            <includes>
                <include>*.properties</include>
                <include>*.conf</include>
                <include>*.yml</include>
            </includes>
        </fileSet>
    </fileSets>

    <dependencySets>
        <dependencySet>
            <useProjectArtifact>true</useProjectArtifact>
            <outputDirectory>lib</outputDirectory>
            <scope>runtime</scope>
            <includes>
                <include>*:*</include>
            </includes>
            <excludes>
                <exclude>${groupId}:${artifactId}</exclude>
                <exclude>org.springframework.boot:spring-boot-devtools</exclude>
            </excludes>
        </dependencySet>
    </dependencySets>
</assembly>

```

- 将最终的程序包打成 tar.gz ,当然也可以打成其他的格式如 zip,rar 等，fileSets 里面指定我们源码里的文件和路径打成标准包相对应的目录
- 需要注意的是，在最终的依赖库 lib 下 去掉我们的程序和开发时 spring boot 的热部署依赖 spring-boot-devtools，否则的会出问题
- 代码里的启动和停止脚本要赋予权限，否则在执行的时候可能提示权限的问题

## jar 启动分离依赖 lib 和配置

### 前言

- 先前发布 boot 项目的时候，改动一点东西，就需要将整个项目重新打包部署，十分不便，故把依赖 lib 从项目分离出来，每次部署只需要发布代码即可。

### 半自动化步骤

#### 1. 更换 maven 的 jar 打包插件

- 先前使用的是 spring-boot-maven-plugin 来打包
  - 这个插件会将项目所有的依赖打入 BOOT-INF/lib 下
- 替换为 maven-jar-plugin
- addClasspath 表示需要加入到类构建路径
- classpathPrefix 指定生成的 Manifest 文件中 Class-Path 依赖 lib 前面都加上路径,构建出 lib/xx.jar

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-jar-plugin</artifactId>
    <version>${maven.jar.plugin.version}</version>
    <configuration>
        <archive>
            <manifest>
                <addClasspath>true</addClasspath>
                <classpathPrefix>lib/</classpathPrefix>
                <mainClass>com.xxx.Start</mainClass>
            </manifest>
        </archive>
    </configuration>
</plugin>
```

#### 2. 拷贝依赖到 jar 外面的 lib 目录

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-dependency-plugin</artifactId>
    <version>${maven.dependency.plugin.version}</version>
    <executions>
        <execution>
            <id>copy-lib</id>
            <phase>prepare-package</phase>
            <goals>
                <goal>copy-dependencies</goal>
            </goals>
            <configuration>
                <outputDirectory>${project.build.directory}/lib</outputDirectory>
                <overWriteReleases>false</overWriteReleases>
                <overWriteSnapshots>false</overWriteSnapshots>
                <overWriteIfNewer>true</overWriteIfNewer>
                <includeScope>compile</includeScope>
            </configuration>
        </execution>
    </executions>
</plugin>
```

#### 3. 在和 jar 包同级的目录下新建一个 config 目录，放入 application.yml 文件

- 这里可能有小伙伴有疑问了，打包的 jar 里面不是应该有 application.yml 文件吗，这里为什么再放一份？
  - 这是因为 boot 读取配置有一个优先级，放在 jar 包外面 config 目录优先级最高，主要是便于从外部修改配置，而不是改 jar 包中的 application.yml 文件。优先级如下：
    - 当前目录的 config 目录下
    - 当前目录
    - classpath 的 config 目录下
    - classpath 的根目录

#### 4. 注意一个依赖的坑，

- 笔者多次通过 java -jar 的方式启动项目总是报如下错误：

```
ClassNotFoundException: org.springframework.boot.SpringApplication
```

- 后来发现时一个依赖的问题，问题详情可以见这个博客：  
   -[SpringBoot 使用 yaml 作为配置文件之坑](https://my.oschina.net/bfleeee/blog/879209)

```xml
<dependency>
    <groupId>org.yaml</groupId>
    <artifactId>snakeyaml</artifactId>
    <version>1.21</version>
</dependency>
```

#### 5. 愉快的启动项目

- 加入–debug 可以让你可以看到比较详细的启动日志

```
java -jar xxx-1.0.0.jar --debug
```

### 全自动化步骤

- 前面介绍的步骤中，需要手动的拷贝 application.yml 文件，并且 jar 包内外都存在配置，总感觉怪怪的（偷笑…）。这里引入一种自动化配置，将所有东西打成 zip 文件，直接发布到服务目录，解压后，即可启动。

#### 自动化步骤 1

- 还是同上面步骤 1，2 所示，指定打包插件和拷贝依赖的插件。

#### 自动化步骤 2

- 排除 resources 下面的 yml(因为我们需要把它放在 jar 外部,不能让 jar 打包插件将其打入 jar 包 classpath 下去)

```xml
<resources>
    <resource>
        <directory>src/main/resources</directory>
        <excludes>
            <exclude>**/application.yml</exclude>
        </excludes>
    </resource>
</resources>
```

#### 自动化步骤 3，使用 maven-assembly-plugin 自定义打包

- 具体打包详情在 assembly.xml 配置中指定

```xml
<plugin>
    <artifactId>maven-assembly-plugin</artifactId>
    <configuration>
        <appendAssemblyId>false</appendAssemblyId>
        <descriptors>
            <descriptor>src/main/resources/assembly.xml</descriptor>
        </descriptors>
    </configuration>
    <executions>
        <execution>
            <id>make-assembly</id>
            <phase>package</phase>
            <goals>
                <goal>single</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

- assembly.xml 具体配置如下：
- 将 application.yml 放在外部 config 目录下
- 所有依赖打成 zip 压缩包

```xml
<assembly xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.3"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.3 http://maven.apache.org/xsd/assembly-1.1.3.xsd">
<id>package</id>
<formats>
    <format>zip</format>
</formats>
<includeBaseDirectory>true</includeBaseDirectory>
<fileSets>
    <fileSet>
        <directory>${basedir}/src/main/resources</directory>
        <includes>
            <include>*.yml</include>
        </includes>
        <filtered>true</filtered>
        <outputDirectory>${file.separator}config</outputDirectory>
    </fileSet>

    <fileSet>
        <directory>src/main/resources/runScript</directory>
        <outputDirectory>${file.separator}bin</outputDirectory>
    </fileSet>
    <fileSet>
        <directory>${project.build.directory}/lib</directory>
        <outputDirectory>${file.separator}lib</outputDirectory>
        <includes>
            <include>*.jar</include>
        </includes>
    </fileSet>
    <fileSet>
        <directory>${project.build.directory}</directory>
        <outputDirectory>${file.separator}</outputDirectory>
        <includes>
            <include>*.jar</include>
        </includes>
    </fileSet>
</fileSets>
</assembly>
```

#### 自动化步骤 4，解压 zip，启动

- 美滋滋的自动化
