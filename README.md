# Examples of python mock

The examples in this repository cover some of the common correct and incorrect usage of  `unittest.mock`.

## Where to patch

> The basic principle is that you patch where an object is *looked up*, which is not necessarily the same place as where it is defined.

The examples contain multiple scenarios

- from ... import ...
- import ...

and show how imports in other module are affected by the mock.

### References

https://docs.python.org/3/library/unittest.mock.html#where-to-patch

http://www.voidspace.org.uk/python/mock/patch.html#where-to-patch



# References

https://docs.python.org/3/library/unittest.mock.html

https://breadcrumbscollector.tech/how-to-mock-in-python-almost-definitive-guide/
