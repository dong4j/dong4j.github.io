<!-- markdownlint-disable-next-line MD033 -->
<meta name="referrer" content="no-referrer"/>

![random-pic-api](https://api.dong4j.ink:1024/cover?spm={{spm}})

## Maven 添加 IntelliJ IDEA 项目文件

在使用 Maven 构建 Java 项目时，若需生成与 IntelliJ IDEA 兼容的项目文件，可以通过以下命令进行：

```bash
mvn idea:idea
```

**`idea:idea`** 插件的目标执行了另外三个目标：project、module 和 workspace。

- **`idea:project`**: 用于生成 IntelliJ IDEA 项目的配置文件（`*.ipr`）。
- **`idea:module`**: 用于生成 IntelliJ IDEA 模块的配置文件（`*.iml`）。
- **`idea:workspace`**: 用于生成工作区文件（`*.iws`），此目标在大多数情况下不会直接使用，因为默认会包含在 `idea:idea` 中。

## 删除指定依赖

如果你想从本地仓库中删除特定版本的依赖，可以使用以下命令：

```bash
mvn com.xxx:xxx-assist-maven-plugin:2.0.0-SNAPSHOT:delete-v5-dependence -Dversion=1.7.1
```

或者首先下载指定的依赖项，然后删除它：

```bash
mvn dependency:get -Dartifact=com.xxx:xxx-assist-maven-plugin:2.0.0-SNAPSHOT
mvn com.xxx:xxx-assist-maven-plugin:2.0.0-SNAPSHOT:delete-v5-dependence -Dversion=1.7.1

# 对于另一个版本的依赖项也适用：
mvn dependency:get -Dartifact=com.xxx:xxx-assist-maven-plugin:1.8.0-SNAPSHOT
mvn com.xxx:xxx-assist-maven-plugin:1.8.0-SNAPSHOT:delete-v5-dependence -Dversion=1.7.1
```

## 设置日志级别

如果你想调整 Maven 的日志输出级别，可以在执行 Maven 命令时添加 `-Dorg.slf4j.simpleLogger.defaultLogLevel` 参数。例如：

```bash
mvn clean install -Dorg.slf4j.simpleLogger.defaultLogLevel=warn
```

若要永久设置日志级别，编辑 Maven 执行脚本（通常是 `${MAVEN_HOME}/bin/mvn`），并新增以下配置行：

```shell
MAVEN_OPTS="-Dorg.slf4j.simpleLogger.defaultLogLevel=info"
```

或者在执行 `mvn` 命令时使用参数 `-q`, 但这样只会输出错误信息。

## Maven 参数说明

Maven 提供了丰富的命令行参数，以支持不同的构建需求：

- **指定 settings 文件**:

```bash
mvn install --settings xxx.xml
```

上述命令中 `xxx.xml` 是自定义的 settings 配置文件路径。

- **指定 pom.xml 文件**：

```bash
mvn install --file pom.xml
```

## 不改变原有依赖，引入新依赖

有时需要在不修改现有项目配置的基础上新增一个依赖，可以通过以下示例 XML 结构来实现：

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <!-- 父项目的定义 -->
    <parent>
        <groupId>org.mapstruct</groupId>
        <artifactId>mapstruct-parent</artifactId>
        <version>1.1.0.RC1</version>
        <relativePath>../parent/pom.xml</relativePath>
    </parent>

    <!-- 当前项目的定义 -->
    <artifactId>mapstruct-jdk7</artifactId>
    <name>MapStruct Core JDK 7</name>
    <description>已弃用的 MapStruct 艺术品，包含用于 JDK 8 及更高版本的注释 - 移至 mapstruct 中。</description>

    <!-- 分发管理 -->
    <distributionManagement>
        <relocation>
            <artifactId>mapstruct</artifactId>
        </relocation>
    </distributionManagement>

</project>
```

## 依赖的版本范围说明

在 Maven 中，可以通过使用特定的符号来指定依赖项的版本范围。以下是一些常见的版本范围及其含义：

- `[1.0]`：表示精确匹配 `1.0` 版本。
- `[1.0,)` 或者 `[1.0,`：表示从 1.0 及其之后的所有版本，即 >= 1.0。
- `(1.0,)` 或者 `(1.0,` ： 表示从大于 1.0 的所有版本。

例如：

```xml
<dependency>
    <groupId>org.twitter4j</groupId>
    <artifactId>twitter4j-core</artifactId>
    <version>[2.2,)</version>
</dependency>

<dependency>
    <groupId>org.twitter4j</groupId>
    <artifactId>twitter4j-stream</artifactId>
    <version>[2.2,)</version>
</dependency>
```

上述依赖项表示我们使用 `twitter4j` 的核心库和流媒体库的版本均必须大于等于 2.2。

## Maven 帮助命令

### 检查 Maven 配置

- **查看当前 Maven 环境启用的文件**:
  ```bash
  mvn help:effective-settings
  ```
- **查看当前项目的 pom.xml 配置，包括所有依赖项**：

  ```bash
  mvn help:effective-pom
  ```

- **查看当前处于激活状态的 profile**:
  ```bash
  mvn help:active-profiles
  ```

### 执行 Maven 命令时指定配置文件

若你有一个自定义的 `settings.xml` 文件，可以使用以下命令来执行带有特定设置的 Maven 目标：

```bash
mvn -s <filepath> <goal>
```

例如：

```bash
mvn -s ~/.m2/settings_local.xml clean deploy
```

### 查看环境详细信息

- **查看当前项目的所有 mvn 配置**:
  ```bash
  mvn -X
  ```
- **打印所有可用的环境变量和 Java 系统属性**：
  ```bash
  mvn help:system
  ```

## 依赖分析与树状展示

为了更好地理解项目的依赖关系，可以使用以下命令来生成依赖项树：

```bash
mvn -X dependency:tree>tree.txt
```

这将输出项目的所有依赖项并将其保存到 `tree.txt` 文件中。

## Maven 环境变量引用

### settings.xml 属性

Maven 支持通过 `settings.xml` 文件中的属性来引用设置值，例如：

```xml
${settings.localRepository}
```

表示本地仓库的地址。

### Java 系统属性

所有 Java 系统属性都可以在 Maven 中使用如下语法引用：

- 使用 `mvn help:system` 命令查看所有的 Java 系统属性。
- 通过 `System.getProperties()` 方法获取所有 Java 属性。

例如：

```xml
${user.home}
```

表示用户目录。

### 环境变量

可以通过以 `env.` 开头的属性引用环境变量。同样地，可以使用以下命令查看所有可用的环境变量：

```bash
mvn help:system
```

如:

```xml
${env.JAVA_HOME}
```

代表 JAVA_HOME 环境变量值。

## 解决缓存依赖问题

Maven 有时会将远程依赖项缓存在本地仓库中，这可能导致无法正确更新依赖。为了解决这个问题，可以采取以下措施：

- **删除缓存目录**：
  删除 `~/.m2/repository/` 目录或其子目录下的所有 `.lastUpdated` 文件。
- **强制更新快照版本插件或依赖项**:
  在执行 Maven 命令时加上 `-U` 参数，如：

  ```bash
  mvn package -U
  ```

  此参数会强制从远程仓库中获取最新版本。

- **调整 updatePolicy 属性**:
  可以在 `repository` 的配置中新增或修改 `updatePolicy` 属性值来改变更新策略。例如，设置为 `always`、`daily`（默认）、`interval:XXX` 或 `never`。

## Maven 命令下载 jar

使用以下命令可以从远程仓库下载特定的 Jar 文件：

```bash
mvn dependency:get -DremoteRepositories=http://repo1.maven.org/maven2/ -DgroupId=org.benf -DartifactId=cfr -Dversion=0.139
```

### Maven 依赖配置示例

```xml
<!-- https://mvnrepository.com/artifact/org.benf/cfr -->
<dependency>
    <groupId>org.benf</groupId>
    <artifactId>cfr</artifactId>
    <version>0.139</version>
</dependency>
```

## 安装第三方 jar 包到本地仓库

### 命令安装

将第三方 Jar 包添加至本地 Maven 仓库，可以使用以下命令：

```bash
mvn install:install-file -Dfile=jar包的位置 -DgroupId=上面的groupId -DartifactId=上面的artifactId -Dversion=上面的version -Dpackaging=jar

# 示例安装 Java Memcached Jar 包:
mvn install:install-file -Dfile=F:\comm\youboy\java_memcached-release_2.6.6\java_memcached-release_2.6.6.jar -DpomFile=F:\comm\youboy\java_memcached-release_2.6.6\pom.xml
```

### 安装到私有服务器（私服）

若需将 Jar 包部署至内部的 Maven 仓库，可使用以下命令：

```bash
mvn deploy:deploy-file -DgroupId=com.xy.oracle -DartifactId=ojdbc14 -Dversion=10.2.0.4.0 -Dpackaging=jar -Dfile=E:\ojdbc14.jar -Durl=http://localhost:9090/nexus-2.2-01/content/repositories/thirdparty/ -DrepositoryId=thirdparty
```

其中：

- `groupId` 和 `artifactId` 构成该 Jar 包在 pom.xml 文件中的唯一标识。
- `file` 参数表示需要上传的 Jar 包的绝对路径。
- `url` 为私有仓库的位置，可在 Nexus 界面中找到相关路径配置。
- `repositoryId` 是服务器 ID，在 Nexus 配置中可以看到。

### 快速安装或略过测试

1. 使用命令跳过测试：

   ```bash
   mvn install -Dmaven.test.skip=true
   ```

2. 在 pom.xml 文件中通过 `<properties>` 标签指定是否进行测试编译，如：

```xml
<properties>
    <skipTests>true</skipTests>
</properties>
```

或

```xml
<properties>
    <maven.test.skip>true</maven.test.skip>
</properties>
```

3. 使用插件配置跳过测试：

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>2.18.1</version>
  <configuration>
    <skipTests>true</skipTests>
  </configuration>
</plugin>
```

## Maven 依赖分析

- 查看项目已解析的依赖：

```bash
mvn dependency:list
```

这会输出所有经过 Maven 解析后的依赖列表。

- 输出项目的完整依赖树至文件 `tree.txt` 中:

```bash
mvn dependency:tree > tree.txt
```

- 分析依赖项并显示未声明但已使用的依赖或已声明但未使用的依赖：

```bash
mvn dependency:analyze
```

该命令的输出通常会分为两部分：

1. **Used undeclared dependencies**: 表示项目中使用到却未在 pom.xml 中声明的依赖。
2. **Unused declared dependencies**: 表示项目中虽声明但并未使用的依赖。

- 分析冲突的 jar 包路径：

```bash
mvn dependency:tree -Dverbose -Dincludes=commons-logging:commons-loggging
```

此命令将输出所有涉及特定依赖包（如 `commons-logging`）的完整依赖路径，这对于解决版本冲突特别有用。

### Maven 使用 systemPath 警告

当使用 `<systemPath>` 时会收到警告：“jar should not point at files within the project directory”。为避免这种警告及潜在问题，应考虑将第三方 jar 包部署到公司仓库或安装到本地仓库。

## dependencies 和 dependencyManagement 的区别

在顶层 pom 中定义的 `<dependencies>` 和 `<dependencyManagement>` 是两个不同的概念：

- **`<dependencies>`**：直接管理项目的依赖项。
- **`<dependencyManagement>`**：主要用来统一管理子模块中不同版本的问题，指定子模块所使用的依赖项的具体版本号。

### Maven Scope 解释

在 Maven 中，通过 `scope` 属性来控制依赖的范围。以下是常用的几种类型及其使用场景：

1. **compile**: 默认情况下编译、测试和运行时都可见。
2. **provided**: 容器已提供，适用于如 servlet-api 等容器内建组件，在打包时不会包含这些 jar 包。
3. **runtime**: 运行时需要的依赖项在编译阶段不需要，但打包时要包括进去（例如 JDBC 驱动）。
4. **test**: 测试场景使用，只用于测试代码，并不在最终的构建输出中。
5. **system**: 类似于 provided，但系统范围的依赖必须通过 `<systemPath>` 明确指定本地路径。由于这种机制不推荐使用，因此通常建议将库添加到本地或组织级的 Maven 仓库。

### 实践心得

- `provided` 的依赖没有传递性。
- `provided` 具有继承性，在多模块项目中可以统一配置通用的 provided 依赖来简化子项目的 pom.xml 文件内容。

## 继承 jar 包示例

在父 pom 中定义依赖管理：

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>3.9</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

在子模块 pom.xml 文件中，只需引用：

```xml
<dependencies>
  <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
  </dependency>
</dependencies>
```

### 添加外部依赖包

```xml
<dependency>
    <groupId>ldapjdk</groupId>
    <artifactId>ldapjdk</artifactId>
    <scope>system</scope>
    <version>1.0</version>
    <systemPath>${basedir}\src\lib\ldapjdk.jar</systemPath>
</dependency>
```

### 创建 Maven Web 项目

使用以下命令创建一个基本的 web 项目的骨架：

```bash
mvn archetype:generate -DgroupId=com.code -DartifactId=spring-web-project -DarchetypeArtifactId=maven-archetype-webapp

# 或者，创建一个简单的 Java 应用程序模板:
mvn archetype:generate -DgroupId=com.code -DartifactId=redis-java -DarchetypeArtifactId=maven-archetype-helloworld
```