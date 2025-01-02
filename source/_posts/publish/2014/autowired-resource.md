---
title: '@Autowired 和 @Resource：哪种方式更适合你的项目？'
keywords:
  - Spring
  - '@Autowired'
  - '@Resource'
  - 依赖注入
categories:
  - 新时代码农
tags:
  - Spring
  - '@Autowired'
  - '@Resource'
  - 依赖注入
abbrlink: 499585b
date: 2014-05-10 00:00:00
ai:
  - 本文对比了Spring框架中的两个注解@Autowired和@Resource在装配bean时的异同。@Autowired默认按类型注入，而@Resource默认按名称注入；@Autowired可以设置required属性允许null值，而@Resource找不到匹配的bean会抛出异常。此外，两者都可以指定bean的名称进行注入。根据使用场景和个人偏好选择合适的注解。
description: 本文对比了Spring框架中的两个注解@Autowired和@Resource在装配bean时的异同。@Autowired默认按类型注入，而@Resource默认按名称注入；@Autowired可以设置required属性允许null值，而@Resource找不到匹配的bean会抛出异常。此外，两者都可以指定bean的名称进行注入。根据使用场景和个人偏好选择合适的注解。
---

1. **作用**: 两者都可以用来装配 bean，可以写在字段上或写在 setter 方法上。
2. **默认注入方式**:
   - **@Autowired (Spring 注解)**: 默认按类型 (byType) 注入。
   - **@Resource (J2EE 注解)**: 默认按名称 (byName) 注入。
3. **required 属性**:
   - **@Autowired**: 默认要求依赖对象必须存在，可以设置 required=false 允许 null 值。
   - **@Resource**: 默认情况下，找不到匹配的 bean 会抛出异常。
4. **指定名称**:
   - **@Autowired**: 可以结合 @Qualifier 注解指定 bean 的名称。
   - **@Resource**: 可以直接在注解中通过 name 属性指定 bean 的名称。
5. **代码示例**:

```java
// 使用 @Autowired
@Autowired
@Qualifier("baseDao")
private BaseDao baseDao;
// 使用 @Resource
@Resource(name="baseDao")
private BaseDao baseDao;
```

## Spring 注解 @Resource 和 @Autowired 区别对比

1. **共同点**:
   - 两者都可以写在字段和 setter 方法上。
   - 如果都写在字段上，则不需要再写 setter 方法。
2. **不同点**:
   - **@Autowired**:
     - 默认按类型 (byType) 注入。
     - 可以设置 required 属性允许 null 值。
     - 可以结合 @Qualifier 注解指定 bean 的名称。
   - **@Resource**:
     - 默认按名称 (byName) 注入。
     - 可以直接在注解中通过 name 属性指定 bean 的名称。
     - 也可以通过 type 属性按类型注入。
     - 如果既不指定 name 也不指定 type，则默认按 byName 注入。
3. **注入顺序**:
   - **@Resource**:
     1. 如果指定了 name 和 type，则查找唯一匹配的 bean。
     2. 如果指定了 name，则查找名称匹配的 bean。
     3. 如果指定了 type，则查找类型匹配的 bean。
     4. 如果既不指定 name 也不指定 type，则先按 byName 注入，找不到则按 byType 注入。

## 总结

- **选择建议**:
  - 如果更倾向于按类型注入，建议使用 @Autowired。
  - 如果更倾向于按名称注入，或者希望减少与 Spring 的耦合，建议使用 @Resource。
- **使用场景**:
  _ @Autowired 适用于大多数情况，尤其是在依赖类型明确的场景下。
  _ @Resource 适用于依赖名称明确的场景，或者希望减少与 Spring 耦合的场景。
  希望以上信息对您有所帮助！
