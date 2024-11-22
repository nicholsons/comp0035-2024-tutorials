# 4. Review the design

This is not easy as you are trying to critically evaluate our own work against a general design principle or pattern.

As a starting point, look at the diagram you have created and consider:

- Are the relationships between classes, modules, functions only those that are needed?
- Are the attributes and methods/functions within a class or module cohesive? If not do you need to split them into more
  classes, functions, modules.
- Does the structure seem clear (simple as possible)?
- Would the structure allow you to reuse components in another application?
- Is the same business logic represented in more than one place? If so then remove the duplication. You don't have code
  at this point however you may have similar functions (methods, operations) that indicate duplicated logic.

This is not an exhaustive list of questions. This aspect is challenging.

[Next activity](7-5-design-medals.md)