---
title: SSM 实现注册功能
keywords:
  - Spring
categories:
  - Spring
tags:
  - HTML
  - AJAX
  - JSON
  - 服务器端编程
  - 数据分页
abbrlink: 22eab19d
date: 2013-04-20 00:00:00
ai:
  - 该代码文件是一个HTML页面和JavaScript混合的模板，用于显示用户数据表并实现分页功能。网页设计简单，提供了一个表格来展示用户的用户名、年龄、性别以及居住城市，并提供了上一页、下一页和跳转到指定页面的功能以浏览数据。通过服务器端的`limitPage.spring`接口来获取特定页面的数据进行渲染。当点击删除按钮时，会调用服务器端的接口处理删除请求。HTML中使用了CSS类如`.col-md-2`等为表格列分配宽度，并在JavaScript代码段中利用AJAX与服务器交互，实现了分页和数据动态加载功能。尽管页面中显示了乱码问题，这是由于编码未正确配置导致的。”，
description: 该代码文件是一个HTML页面和JavaScript混合的模板，用于显示用户数据表并实现分页功能。网页设计简单，提供了一个表格来展示用户的用户名、年龄、性别以及居住城市，并提供了上一页、下一页和跳转到指定页面的功能以浏览数据。通过服务器端的`limitPage.spring`接口来获取特定页面的数据进行渲染。当点击删除按钮时，会调用服务器端的接口处理删除请求。HTML中使用了CSS类如`.col-md-2`等为表格列分配宽度，并在JavaScript代码段中利用AJAX与服务器交互，实现了分页和数据动态加载功能。尽管页面中显示了乱码问题，这是由于编码未正确配置导致的。”，
---

SSH 整合时实现了简单的登录功能,这次实现简单的注册功能.  
需要改动的地方下面会提到,没有提到的地方就不改动

## 要求

1.登录 register.jsp 页面,填入必要信息,点击注册;  
2.如果成功,跳转到 success.jsp,并显示出所有的用户信息;  
3.如果注册失败,则跳转到 error.jsp 页面  
4.实现分页功能,实现删除功能

## 实现

1.新建 t_user 表

```sql
-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_name` varchar(255) DEFAULT NULL,
  `f_password` varchar(255) DEFAULT NULL,
  `f_age` int(11) DEFAULT NULL,
  `f_sex` varchar(255) DEFAULT NULL,
  `f_city` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES ('14', 'rooterger', 'dus', '23', 'rth', 'jngfnm');
INSERT INTO `t_user` VALUES ('31', 'root2', 'dus010', '234', 'erh', 'tyjty');
INSERT INTO `t_user` VALUES ('32', 'er', 'du010', '23', 'rth', 'tym');
INSERT INTO `t_user` VALUES ('33', 'rootehr', 'trj', '23', 'segv', 'rtj');
INSERT INTO `t_user` VALUES ('34', 'refw', 'dus82010', '23', 'erg', 'tg');
INSERT INTO `t_user` VALUES ('45', 'ergrth', 'tyj', '2', 'tyj', 'erh');
INSERT INTO `t_user` VALUES ('53', 'ergfgnfgn', 'erg', '213', 'erg', 'gfnfg');
INSERT INTO `t_user` VALUES ('54', 'ghn', 'ghmghm', '213', 'ghm', 'fgn');
INSERT INTO `t_user` VALUES ('55', 'hj,', 'hj,', '324', 'jh,', 'rtbh');
INSERT INTO `t_user` VALUES ('56', 'erg', 'erg', '23', 'erg', 'fdbfgn');
INSERT INTO `t_user` VALUES ('74', 'tgym', 'ghm', '234', 'hgmghm', 'ghm');
INSERT INTO `t_user` VALUES ('76', 'dfbfd', 'dfb', '23', 'dfb', 'dfnb');
INSERT INTO `t_user` VALUES ('77', 'edhrtjytjk', 'hykm', '23', 'edb', 'dfb');
INSERT INTO `t_user` VALUES ('79', 'dfnb', 'fgn', '234', 'fgn', 'fn');
INSERT INTO `t_user` VALUES ('80', 'yuk', 'yukm', '32', 'db', 'fgn');
INSERT INTO `t_user` VALUES ('81', 'rthrthtrh', 'rth', '234', 'rthrt', 'rtnghm');
INSERT INTO `t_user` VALUES ('82', 'fgngffgn', 'fgnfgn', '23', 'sv', 'fgn');
INSERT INTO `t_user` VALUES ('84', 'dfbdf', 'dfnf', '32', 'gngfn', 'gfm');
INSERT INTO `t_user` VALUES ('85', 'ergergtyj', 'tyjkyk', '2', 'wefwe', 'rthntj');
INSERT INTO `t_user` VALUES ('86', 'fgnfgfgmhgm', 'hgmgh', '32', 'sdv', 'fgnghm');
```

2.新建 UserBean.java

```java
package com.code.ssm.bean;
import java.io.Serializable;
public class UserBean implements Serializable{
    private static final long serialVersionUID = -6971764181923020401L;
    private int id;
    private String username;
    private String password;
    private int age;
    private String sex;
    private String city;
    public UserBean() {}
    public UserBean(String username, String password, int age, String sex, String city) {
        this.username = username;
        this.password = password;
        this.age = age;
        this.sex = sex;
        this.city = city;
    }
    public int getId() {return id;}
    public void setId(int id) {this.id = id;}
    public String getUsername() {return username;}
    public void setUsername(String username) {this.username = username;}
    public String getPassword() {return password;}
    public void setPassword(String password) {this.password = password;}
    public int getAge() {return age;}
    public void setAge(int age) {this.age = age;}
    public String getSex() { return sex;}
    public void setSex(String sex) {this.sex = sex;}
    public String getCity() {return city;}
    public void setCity(String city) {this.city = city;}

    @Override
    public String toString() {
        return "UserBean{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                ", age=" + age +
                ", sex='" + sex + '\'' +
                ", city='" + city + '\'' +
                '}';
    }
}
```

3.新建 UserMapper.java

```java
package com.code.ssm.mapper;
import com.code.ssm.bean.UserBean;
import org.apache.ibatis.annotations.Param;
import java.util.List;
public interface UserMapper {
    List<UserBean> getUserByName(@Param("username")String username);
    int addUser(UserBean userBean);
    List<UserBean> getAllUsers();
    //分页实现
    List<UserBean> getAllUsersLimit(@Param("pageNow")int pageNow,@Param("pageSize")int pageSize);
    int getCounts();
    int delUser(@Param("id") int id);
}
```

4.新建 UserMapper.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >
<mapper namespace="com.code.ssm.mapper.UserMapper">

    <!-- 结果映射 -->
    <resultMap id="userMap" type="UserBean" >
        <id property="id" column="user_id" javaType="int"/>
        <result property="username" column="f_name" javaType="java.lang.String"/>
        <result property="password" column="f_password" javaType="java.lang.String"/>
        <result property="age" column="f_age" javaType="int"/>
        <result property="sex" column="f_sex" javaType="java.lang.String"/>
        <result property="city" column="f_city" javaType="java.lang.String"/>
    </resultMap>

    <insert id="addUser">
        insert into t_user(f_name,f_password,f_age,f_sex,f_city) values(#{username},#{password},#{age},#{sex},#{city})
    </insert>
    <delete id="delUser">
        delete from t_user where user_id=#{id}
    </delete>
    <select id="getUserByName" resultType="com.code.ssm.bean.UserBean">
        select * from t_user where f_name=#{username}
    </select>
    <select id="getAllUsers" resultMap="userMap">
        select * from t_user
    </select>
    <select id="getAllUsersLimit" resultMap="userMap">
        select * from t_user limit #{pageNow},#{pageSize}
    </select>
    <select id="getCounts" resultType="java.lang.Integer">
        select count(*) from t_user
    </select>
</mapper>
```

5.UserService.java

```java
package com.code.ssm.service;
import com.code.ssm.bean.UserBean;
import java.util.List;
public interface UserService {
    public boolean register(UserBean userBean);
    public List<UserBean> getAllUsers(int pageNow, int pageSize);
    public boolean delUser(int id);
    int getCounts();
}
```

6.UserServiceImp.java

```java
package com.code.ssm.service.imp;

import com.code.ssm.bean.UserBean;
import com.code.ssm.mapper.UserMapper;
import com.code.ssm.service.UserService;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

@Service("userService")
public class UserServiceImp implements UserService {
    @Resource
    private UserMapper userMapper;
    @Override
    public boolean register(UserBean userBean) {
        if(userMapper.getUserByName(userBean.getUsername()).size() == 0){
            userMapper.addUser(userBean);
            return true;
        }else return false;
    }
    @Override
    public List<UserBean> getAllUsers(int pageNow,int pageSize) {
        int a = (pageNow - 1) * pageSize;
        return userMapper.getAllUsersLimit(a,pageSize);
    }
    @Override
    public boolean delUser(int id) {
        return 1 == userMapper.delUser(id);
    }
    @Override
    public int getCounts() {
        return userMapper.getCounts();
    }
}
```

7.导入 jQuery+bootstrap 包  
8.新建 register.jsp

```html
<%@ page contentType = "text/html;charset=UTF-8" pageEncoding = "UTF-8" language
= "java" %>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>注册</title>
    <link rel="stylesheet" href="css/style.css" />
    <link rel="stylesheet" href="css/fort.css" />
    <style>
      a {
        font-size: 16px;
        color: white;
      }
    </style>
  </head>

  <body>
    <h1>注册</h1>
    <div class="form-wrapper">
      <%--顶部颜色条--%>
      <div class="top"><div class="colors"></div></div>
      <form name="form" action="register.spring" method="POST">
        <div class="form">
          <div class="form-item">
            <input
              type="text"
              name="username"
              required="required"
              placeholder="用户名"
              autocomplete="off"
            />
          </div>
          <div class="form-item">
            <input
              type="password"
              name="password"
              required="required"
              placeholder="密码"
              autocomplete="off"
            />
          </div>
          <div class="form-item">
            <input
              type="text"
              name="sex"
              required="required"
              placeholder="性别"
              autocomplete="off"
            />
          </div>
          <div class="form-item">
            <input
              type="text"
              name="age"
              required="required"
              placeholder="年龄"
              autocomplete="off"
            />
          </div>
          <div class="form-item">
            <input
              type="text"
              name="city"
              required="required"
              placeholder="籍贯"
              autocomplete="off"
            />
          </div>
          <div class="button-panel">
            <input type="submit" class="button" title="Register" value="注册" />
          </div>
        </div>
      </form>
    </div>

    <script src="js/jquery-1.11.3.min.js"></script>
    <script src="js/fort.js"></script>
    <script>
      sections();
    </script>
  </body>
</html>
```

9.接下来开始 Controller 的书写  
由于使用了 ajax 异步加载表格数据,所以需要导入将 Bean 转换成 json 数据格式的工具包  
fastjson-1.1.15.jar  
jsoup-1.8.1.jar

```java
package com.code.ssm.controller;

import com.alibaba.fastjson.JSONArray;
import com.code.ssm.bean.UserBean;
import com.code.ssm.service.UserService;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
@Controller
public class UserController {
    //分页大小
    private static final int PAGESIZE = 5;
    @Resource(name="userService")
    private UserService userService;
    @RequestMapping("/register")
    //当请求register.spring时,自动将表单中的数据封装成UserBean对象,前提是控件name属性要和UserBean属性名相同
    public String register(UserBean userBean, HttpServletRequest request){
        //调用register()实现向数据库中添加数据
        //先执行查询,如果数据库中有同名的数据,则注册失败,跳转到error.jsp
        //如果没有相同数据,则执行insert语句,跳转到success.jsp
        //这时将再次查询数据库,返回所有的用户信息(分页)
        if(userService.register(userBean)){
            //初始化总页数
            int counts = userService.getCounts();
            int pageNum = (int)Math.ceil(counts / (PAGESIZE * 1.0));
            //得到分页数据
            List<UserBean> allUsers = userService.getAllUsers(1,PAGESIZE);
            //放requset
            //request.setAttribute("pageNum",pageNum);
            //放session都一样
            request.getSession().setAttribute("pageNum",pageNum);
            //初始化当前页为第一页
            request.setAttribute("pageNow",1);
            //将所有用户数据返回给jsp显示
            request.getSession().setAttribute("allUsers",allUsers);
            return "success";
        }else return "error";
    }

    //分页请求数据
    @RequestMapping("/limitPage")
    //当点击下一个/上一页/按页数跳转时调用此方法
    public void limitPage(HttpServletRequest request,HttpServletResponse response) throws IOException {
        //先得到当前页数
        int pageNow = Integer.parseInt(request.getParameter("pageNow"));
        //根据当前页在数据库中查询数据
        List<UserBean> allUsers = userService.getAllUsers(pageNow,PAGESIZE);
        PrintWriter out = response.getWriter();
        //将List转换成json格式数据
        out.print(JSONArray.toJSONString(allUsers,true));
    }

    //当点击"删除"是调用此方法
    @RequestMapping(value = "/delUser")
    public void delUser(HttpServletRequest request,HttpServletResponse response,  @RequestParam("id")int id) throws IOException {
        PrintWriter out = response.getWriter();
        if(userService.delUser(id)){
            //删除之后总页数要变
            int counts = userService.getCounts();
            int pageNum = (int)Math.ceil(counts / (PAGESIZE * 1.0));
            int pageNow = Integer.parseInt(request.getParameter("pageNow"));
            List<UserBean> allUsers = userService.getAllUsers(pageNow,PAGESIZE);
            //将总页数放到集合中的最后一个元素
            //因为是ajax局部加载表格,这里将变化后的总页数放到了数据集合中一起传回给jsp
            //在jsp中取集合最后一个元素,然后拆分数据就可以得到总页数
            UserBean pageNumBean = new UserBean();
            pageNumBean.setUsername("pageNum&" + pageNum);
            allUsers.add(pageNumBean);
            out.print(JSONArray.toJSONString(allUsers,true));
        }else out.print("'message':'failed'");
    }
}
```

10.新建 success.jsp

```html
<%-- Created by IntelliJ IDEA. User: Code.Ai To change this template use File |
Settings | File Templates. --%> <%@ page contentType="text/html;charset=UTF-8"
pageEncoding="UTF-8" language="java" %> <%@ taglib prefix = "c" uri =
"http://java.sun.com/jsp/jstl/core" %>
<html>
  <head>
    <title>success</title>
    <link rel="stylesheet" href="./bootstrap/css/bootstrap.min.css" />
    <link
      href="./bootstrap/css/bootstrap-datetimepicker.css"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="./css/index.css" />
  </head>
  <body>
    <div class="container-fluid">
      <!--标题-->
      <div class="row-fluid">
        <div class="span12">
          <h3 class="text-center" style="color: white">全部用户信息</h3>
        </div>
      </div>
      <!--表格-->

      <div
        class="row-fluid table-responsive"
        style="border: solid;background-color: white"
      >
        <table class="table   table-bordered">
          <tr>
            <th class="col-md-2">姓名</th>
            <th class="col-md-2">年龄</th>
            <th class="col-md-2">性别</th>
            <th class="col-md-3">籍贯</th>
            <th class="col-md-3">操作</th>
          </tr>
        </table>

        <div
          id="tableTD"
          class="row-fluid"
          style="overflow-y: auto;height: 208px;margin-top: -20px;background-color: white"
        >
          <table id="table" class="table  table-bordered  table-condensed">
            <c:forEach
              items="${sessionScope.allUsers}"
              var="user"
              <%--点击表格行改变颜色--%
            >
              <tr onclick="select(this,'#selectID')">
                <input type="hidden" value="${user.id}" />
                <td class="col-md-2">${user.username}</td>
                <td class="col-md-2">${user.age}</td>
                <td class="col-md-2">${user.sex}</td>
                <td class="col-md-3">${user.city}</td>
                <td class="col-md-3">
                  <a href="#" id="${user.id}" onclick="delUser(this)">删除</a>
                </td>
              </tr>
            </c:forEach>
          </table>
          <input type="hidden" value="-1" id="selectID" name="selectID" />
        </div>

        <%--分页按钮--%>
        <div class="row-fluid">
          <div class="span12">
            <div>
              <button
                id="previousPage"
                class="btn btn-sm"
                type="button"
                style="line-height:0px"
              >
                <span class="glyphicon glyphicon-chevron-left"></span>
              </button>
              <input
                id="pageNow"
                type="text"
                style="width: 40px;height: 20px"
                value="${requestScope.pageNow}"
              />
              <label id="pageNum">/${sessionScope.pageNum}</label>
              <button
                id="go"
                class="btn btn-sm"
                type="button"
                style="line-height:0px"
              >
                <span class="glyphicon glyphicon-step-forward"></span>
              </button>
              <button
                id="nextPage"
                class="btn  btn-sm"
                type="button"
                style="line-height:0px"
              >
                <span class="glyphicon glyphicon-chevron-right"></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <script type="text/javascript" src="./js/jquery-1.11.3.min.js"></script>
    <script
      type="text/javascript"
      src="./bootstrap/js/bootstrap.min.js"
    ></script>
    <script
      type="text/javascript"
      src="./bootstrap/js/bootstrap-table.js"
    ></script>
    <script
      type="text/javascript"
      src="./bootstrap/js/bootstrap-datetimepicker.js"
      charset="UTF-8"
    ></script>
    <script
      type="text/javascript"
      src="./bootstrap/js/locales/bootstrap-datetimepicker.zh-CN.js"
      charset="UTF-8"
    ></script>
    <script type="text/javascript" src="./js/index.js"></script>

    <script type="text/javascript" src="./js/ajaxfileupload.js"></script>
    <script type="text/javascript" src="./js/uploadPreview.min.js"></script>

    <script type="text/javascript">
      //全局
      var pageNow = parseInt($("#pageNow").val());
      var pageNum = parseInt(${sessionScope.pageNum});

      function delUser(obj){
          var id = obj.id;
          $.ajax({
              type: 'POST',
              url: 'delUser.spring',
              data: {'id': id,'pageNow':pageNow},
              cache: false,
              //不能用json
              dataType: 'text',
              success: function (data) {
                  var jsonObj = eval("("+ data+")");
                  if(jsonObj.message == "failed"){
                      alert("删除失败");
                  }else{
                      //删除单行
                      //obj.parentNode.parentNode.parentNode.removeChild(obj.parentNode.parentNode);
                      //设置总页数 在集合中的最后一个元素的username中
                      var arrayObj =  jsonObj[jsonObj.length - 1].username.split("&");
                      pageNum = arrayObj[1];
                      $("#pageNum").text("/"+pageNum);
                      $("#table").empty();
                      for (var i = 0; i < jsonObj.length; i++) {
                          $("#table").append(
                                  "<tr>" +
                                  "<td class = 'col-md-2' >"+  jsonObj[i].username+"</td>" +
                                  "<td class = 'col-md-2' >"+  jsonObj[i].age+"</td>" +
                                  "<td class = 'col-md-2' >" + jsonObj[i].sex + "</td>" +
                                  "<td class = 'col-md-3' >" + jsonObj[i].city + "</td>" +
                                  "<td class = 'col-md-3' >" + "<a href='#' id= " + jsonObj[i].id +" onclick='delUser(this)'>删除</a>" + "</td>" +
                                  "</tr>");
                      }
                  }
              }
          });
          return false;
      }

      /**************************************************************************/

      //上一页事件
      $("#previousPage").click(function () {
          if (pageNow > 1){
              pageNow = pageNow -1 ;
              $.ajax({
                  type: "GET",
                  url: "limitPage.spring",
                  data: { "pageNow": pageNow},
                  dataType: 'text',
                  success: function (data) {
                      $("#pageNow").val(pageNow);
                      var jsonObj = eval("(" + data + ")");
                      $("#table").empty();
                      for (var i = 0; i < jsonObj.length; i++) {
                          $("#table").append(
                                  "<tr>" +
                                  "<td class = 'col-md-2' >"+  jsonObj[i].username+"</td>" +
                                  "<td class = 'col-md-2' >"+  jsonObj[i].age+"</td>" +
                                  "<td class = 'col-md-2' >" + jsonObj[i].sex + "</td>" +
                                  "<td class = 'col-md-3' >" + jsonObj[i].city + "</td>" +
                                  "<td class = 'col-md-3' >" + "<a href='#' id= " + jsonObj[i].id +" onclick='delUser(this)'>删除</a>" + "</td>" +
                                  "</tr>");
                      }
                  }
              })
          }
          else alert("已是第一页！");
      });

      //下一页事件
      $("#nextPage").click(function () {
          if (pageNow < pageNum){
              pageNow = pageNow + 1;
              $.ajax({
                  type: "GET",
                  url: "limitPage.spring",
                  data: { "pageNow": pageNow},
                  dataType: 'text',
                  success: function (data) {
                      $("#pageNow").val(pageNow);
                      var jsonObj = eval("(" + data + ")");
                      $("#table").empty();
                      for (var i = 0; i < jsonObj.length; i++) {
                          $("#table").append(
                                  "<tr>" +
                                  "<td class = 'col-md-2' >"+  jsonObj[i].username+"</td>" +
                                  "<td class = 'col-md-2' >"+  jsonObj[i].age+"</td>" +
                                  "<td class = 'col-md-2' >" + jsonObj[i].sex + "</td>" +
                                  "<td class = 'col-md-3' >" + jsonObj[i].city + "</td>" +
                                  "<td class = 'col-md-3' >" + "<a href='#' id= " + jsonObj[i].id +" onclick='delUser(this)'>删除</a>" + "</td>" +
                                  "</tr>");
                      }
                  }
              })
          }

          else alert("已是最后一页！");
      });

      //跳转到指定页点击事件
      $("#go").click(function () {
          var num = parseInt($("#pageNow").val());
          if(num <= pageNum){
              $.ajax({
                  type: "GET",
                  url: "limitPage.spring",
                  data: {"pageNow": num},
                  dataType: 'text',
                  success: function (data) {
                      pageNow = num;
                      var jsonObj = eval("(" + data + ")");
                      $("#table").empty();
                      for (var i = 0; i < jsonObj.length; i++) {
                          $("#table").append(
                                  "<tr>" +
                                  "<td class = 'col-md-2' >"+  jsonObj[i].username+"</td>" +
                                  "<td class = 'col-md-2' >"+  jsonObj[i].age+"</td>" +
                                  "<td class = 'col-md-2' >" + jsonObj[i].sex + "</td>" +
                                  "<td class = 'col-md-3' >" + jsonObj[i].city + "</td>" +
                                  "<td class = 'col-md-3' >" + "<a href='#' id= " + jsonObj[i].id +" onclick='delUser(this)'>删除</a>" + "</td>" +
                                  "</tr>");
                      }
                  }
              })
          }else alert("超出总页数");
      });
    </script>
  </body>
</html>
```

## 效果

由于没有配置编码过滤器,所以添加进去的是乱码
