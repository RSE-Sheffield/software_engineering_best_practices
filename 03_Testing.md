# Testing
<style>
    .reveal section p {
    display: inline-block;
    font-size: 0.8em;
    line-height: 1em;
    vertical-align: top;
  }
</style>

#

### How do we know our code is reliable?

### How do we know it returns an expected response?

### How do we know our code plays nicely with other modules and scripts?

### We test!

# Why do we Test?
::: incremental
- To know that new code produces the expected results

- Just as with any research, we want to ensure our results are reliable, reproducible and trustworthy.

- As software grows, our codebase becomes bigger and more complex.

- When we rewrite and update code, we want to know that our new code works as intended, both in its basic functionality and as part of a bigger web of dependencies.

- *Writing* tests for your software will save you time and headaches in the long run
:::

# When do we test?
::: incremental
- Tests should be written alongside code, one test per 'unit' of code

- In Python, a 'unit' would generally be considered to be a function or class

- Any time that you manually run something and check the result

- But! Tests can be written *before* we write any code, this is known as Test Driven Development (TDD)

- By writing tests alongside your code, we know that as long as our tests are passing, our previously written code doesn't need to be revisited
:::

# Types of test

### Unit Test *

### Integration Test

### Regression Test

### Performance Test


# How to test

- In Python, `pytest` is the most popular framework

- In the next exercise we'll produce a unit test for a function, using `pytest`
