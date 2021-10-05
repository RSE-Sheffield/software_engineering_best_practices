## Testing

<style> .reveal { font-size: 2em; } </style>

### How do we know our code is reliable?

### How do we know it returns an expected response?

### How de we know our code plays nicely with other modules and scripts?

### We test!

## Why do we Test?

- When we produce new code, we want to know it is fit for purpose. However, it can be difficult to test new code in isolation when at runtime it will form part of a larger software package.

- Just as with any other scientific/research endeavour, we want to ensure that our results are reliable, reproducible and trustworthy.

- As software grows, our codebase becomes bigger and our dependencies become more complex. When we rewrite and update code, we want to know that our new code works as intended, both in its basic functionality and as part of a bigger web of dependencies.

- Writing tests for your software will save you time and headaches in the long run

## When do we test?

- Tests should be written alongside code, one test per 'unit' of code

- In Python, a 'unit' would generally be considered to be a function or class

- We begin the next workshop by producing a unit test for function we have written

- But! Test can be written *before* we write any code, this is known as Test Driven Development (TDD)

- By writing tests alongside your code, we know that as long as our tests are passing, our previously written code doesn't need to revisited
