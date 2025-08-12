# Code layout
## Indentation
Use 4 spaces per indentation level.
Continuation lines should align wrapped elements either vertically using Python’s implicit line joining inside parentheses, brackets and braces, or using a hanging indent (Hanging indentation is a type-setting style where all the lines in a paragraph are indented except the first line. In the context of Python, the term is used to describe a style where the opening parenthesis of a parenthesized statement is the last non-whitespace character of the line, with subsequent lines being indented until the closing parenthesis).

```
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```
```
# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

For if statements, all of these are correct:
```
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

The closing brace/bracket/parenthesis on multiline constructs may either line up under the first non-whitespace character of the last line of list, as in:
```
# Yuck. Don't do this.
# It's permitted style, but just don't.
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
```
or it may be lined up under the first character of the line that starts the multiline construct, as in:
```
# This version is much nicer imo and will be how I style things.
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

## Tabs or Spaces?
Spaces are the preferred indentation method.

## Maximum Line Length
Limit all lines to a maximum of 79 characters.

For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters.
Some teams strongly prefer a longer line length. For code maintained exclusively or primarily by a team that can reach agreement on this issue, it is okay to increase the line length limit up to 99 characters, provided that comments and docstrings are still wrapped at 72 characters.

The Python standard library is conservative and requires limiting lines to 79 characters (and docstrings/comments to 72).

The preferred way of wrapping long lines is by using Python’s implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses. These should be used in preference to using a backslash for line continuation.
Backslashes may still be appropriate at times. For example, long, multiple with-statements could not use implicit continuation before Python 3.10, so backslashes were acceptable for that case:
```
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

## Should a Line Break Before or After a Binary Operator?
Following the tradition from mathematics usually results in more readable code:
```
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```
In Python code, it is permissible to break before or after a binary operator, as long as the convention is consistent locally. For new code Knuth’s style (above) is suggested.

## Blank Lines
Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank line.

Extra blank lines may be used (sparingly) to separate groups of related functions.

Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).

Use blank lines in functions, sparingly, to indicate logical sections.

## Source File Encoding
Code in the core Python distribution should always use UTF-8 and should not have an encoding declaration.

All identifiers in the Python standard library MUST use ASCII-only identifiers.

Imports should usually be on separate lines:
```
# Correct:
import os
import sys
```
```
# Wrong:
import sys, os
```
It’s okay to say this though:
```
# Correct:
from subprocess import Popen, PIPE
```

Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

Imports should be grouped in the following order:
1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.
You should put a blank line between each group of imports.

Absolute imports are recommended:
```
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```
However, explicit relative imports are an acceptable alternative to absolute imports, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose:
```
from . import sibling
from .sibling import example
```
Standard library code should avoid complex package layouts and always use absolute imports.

When importing a class from a class-containing module, it’s usually okay to spell this:
```
from myclass import MyClass
from foo.bar.yourclass import YourClass
```
If this spelling causes local name clashes, then spell them explicitly:
```
import myclass
import foo.bar.yourclass
```
and use myclass.MyClass and foo.bar.yourclass.YourClass.

Wildcard imports (from <module> import *) should be avoided
There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API (for example, overwriting a pure Python implementation of an interface with the definitions from an optional accelerator module and exactly which definitions will be overwritten isn’t known in advance).

## Module Level Dunder Names
Module level “dunders” (i.e. names with two leading and two trailing underscores) such as `__all__`, `__author__`, `__version__`, etc. should be placed after the module docstring but before any import statements except from `__future__` imports. Python mandates that future-imports must appear in the module before any other code except docstrings:
```
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

# String Quotes
In Python, single-quoted strings and double-quoted strings are the same.
When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string.

For triple-quoted strings, always use double quote characters.

# Whitespace in Expressions and Statements
Avoid extraneous whitespace in the following situations:

* Immediately inside parentheses, brackets or braces:
```
# Correct:
spam(ham[1], {eggs: 2})
```
```
# Wrong:
spam( ham[ 1 ], { eggs: 2 } )
```
* Between a trailing comma and a following close parenthesis:
```
# Correct:
foo = (0,)
```
```
# Wrong:
bar = (0, )
```
* Immediately before a comma, semicolon, or colon:
```
# Correct:
if x == 4: print(x, y); x, y = y, x
```
```
# Wrong:
if x == 4 : print(x , y) ; x , y = y , x
```
However, in a slice the colon acts like a binary operator, and should have equal amounts on either side (treating it as the operator with the lowest priority). In an extended slice, both colons must have the same amount of spacing applied. Exception: when a slice parameter is omitted, the space is omitted:
```
# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
```
```
# Wrong:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : step]
ham[ : upper]
```
* Immediately before the open parenthesis that starts the argument list of a function call:
```
# Correct:
spam(1)
```
```
# Wrong:
spam (1)
```
* Immediately before the open parenthesis that starts an indexing or slicing:
```
# Correct:
dct['key'] = lst[index]
```
```
# Wrong:
dct ['key'] = lst [index]
```
* More than one space around an assignment (or other) operator to align it with another:
```
# Correct:
x = 1
y = 2
long_variable = 3
```
```
# Wrong:
x             = 1
y             = 2
long_variable = 3
```

Avoid trailing whitespace anywhere.

Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <=, >=, in, not in, is, is not), Booleans (and, or, not).

If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies).
```
# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
```
# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

Function annotations should use the normal rules for colons and always have spaces around the -> arrow if present.
```
# Correct:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...
```
```
# Wrong:
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

Don’t use spaces around the = sign when used to indicate a keyword argument, or when used to indicate a default value for an unannotated function parameter:
```
# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```
```
# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```
When combining an argument annotation with a default value, however, do use spaces around the = sign:
```
# Correct:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```
```
# Wrong:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```

Do not use compound statements (i.e. multiple statements on a single line separated by a semicolon)

Do not put an if/for/while on the same line as the body text:
```
# Wrong:
if foo == 'blah': do_blah_thing()
```

# When to Use Trailing Commas
Trailing commas are usually optional, except they are mandatory when making a tuple of one element. For clarity, it is recommended to surround the latter in (technically redundant) parentheses:
```
# Correct:
FILES = ('setup.cfg',)
```
```
# Wrong:
FILES = 'setup.cfg',
```
When trailing commas are redundant, they are often helpful when a version control system is used, when a list of values, arguments or imported items is expected to be extended over time. The pattern is to put each value (etc.) on a line by itself, always adding a trailing comma, and add the close parenthesis/bracket/brace on the next line. However it does not make sense to have a trailing comma on the same line as the closing delimiter (except in the above case of singleton tuples):
```
# Correct:
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
```
```
# Wrong:
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)
```

# Comments
Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter.

Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period.

You should use one or two spaces after a sentence-ending period in multi-sentence comments, except after the final sentence.

## Block Comments
Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).

Paragraphs inside a block comment are separated by a line containing a single #.

## Inline Comments
Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space. Example:
```
x = x + 1                 # Compensate for border
```

## Documentation Strings
Conventions for writing good documentation strings (a.k.a. “docstrings”) are immortalized in PEP 257.

* Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.

* PEP 257 describes good docstring conventions. Note that most importantly, the """ that ends a multiline docstring should be on a line by itself:
```
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```

* For one liner docstrings, please keep the closing """ on the same line:
```
"""Return an ex-parrot."""
```

# Naming Conventions
New modules and packages (including third party frameworks) should be written to these standards, but where an existing library has a different style, internal consistency is preferred.

## Overriding Principle
Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.

## Descriptive: Naming Styles
There are a lot of different naming styles. It helps to be able to recognize what naming style is being used, independently from what they are used for.

The following naming styles are commonly distinguished:
* `b` (single lowercase letter)
* `B` (single uppercase letter)
* `lowercase`
* `lower_case_with_underscores`
* `UPPERCASE`
* `UPPER_CASE_WITH_UNDERSCORES`
* `CapitalizedWords` (or `CapWords`, or `CamelCase` – so named because of the bumpy look of its letters [4]). This is also sometimes known as `StudlyCaps`. \
Note: When using acronyms in CapWords, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError.
* `mixedCase` (differs from CapitalizedWords by initial lowercase character!)
* `Capitalized_Words_With_Underscores` (ugly!)

There’s also the style of using a short unique prefix to group related names together. This is not used much in Python, but it is mentioned for completeness. For example, the os.stat() function returns a tuple whose items traditionally have names like st_mode, st_size, st_mtime and so on.

The X11 library uses a leading X for all its public functions. In Python, this style is generally deemed unnecessary because attribute and method names are prefixed with an object, and function names are prefixed with a module name.

In addition, the following special forms using leading or trailing underscores are recognized (these can generally be combined with any case convention):
* `_single_leading_underscore`: weak “internal use” indicator. E.g. from M import * does not import objects whose names start with an underscore.
* `single_trailing_underscore_`: used by convention to avoid conflicts with Python keyword, e.g. :
```
tkinter.Toplevel(master, class_='ClassName')
```
* `__double_leading_underscore`: when naming a class attribute, invokes name mangling (inside `class FooBar`, `__boo` becomes `_FooBar__boo`; see below).
* `__double_leading_and_trailing_underscore__`: “magic” objects or attributes that live in user-controlled namespaces. E.g.`__init__`, `__import__` or `__file__`. Never invent such names; only use them as documented.

## Prescriptive: Naming Conventions
### Names to Avoid
Never use the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names.

In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use ‘l’, use ‘L’ instead.

### ASCII Compatibility
Identifiers used in the standard library must be ASCII compatible as described in the policy section of PEP 3131.

### Package and Module Names
Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. _socket).

### Class Names
Class names should normally use the CapWords convention.

The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.

### Type Variable Names
Names of type variables introduced in PEP 484 should normally use CapWords preferring short names: `T`, `AnyStr`, `Num`. It is recommended to add suffixes `_co` or `_contra` to the variables used to declare covariant or contravariant behavior correspondingly:
```
from typing import TypeVar

VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)
```

### Exception Names
Because exceptions should be classes, the class naming convention applies here. However, you should use the suffix “Error” on your exception names (if the exception actually is an error).

### Global Variable Names
(Global variables are meant for use inside one module only.) \
The conventions are about the same as those for functions.

Modules that are designed for use via `from M import *` should use the `__all__` mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are “module non-public”).

### Function and Variable Names
Function names should be lowercase, with words separated by underscores as necessary to improve readability.

Variable names follow the same convention as function names.

### Function and Method Arguments
Always use `self` for the first argument to instance methods.

Always use `cls` for the first argument to class methods.

If a function argument’s name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus `class_` is better than `clss`. (Perhaps better is to avoid such clashes by using a synonym.)

### Method Names and Instance Variables

Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.

Use one leading underscore only for non-public methods and instance variables.

To avoid name clashes with subclasses, use two leading underscores to invoke Python’s name mangling rules.

Python mangles these names with the class name: if class Foo has an attribute named `__a`, it cannot be accessed by `Foo.__a`. (An insistent user could still gain access by calling `Foo._Foo__a`.) Generally, double leading underscores should be used only to avoid name conflicts with attributes in classes designed to be subclassed.

### Constants
Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include `MAX_OVERFLOW` and `TOTAL`.

### Designing for Inheritance
Always decide whether a class’s methods and instance variables should be public or non-public. If in doubt, choose non-public.

Public attributes are those that you expect unrelated clients of your class to use, with your commitment to avoid backwards incompatible changes. Non-public attributes are those that are not intended to be used by third parties; you make no guarantees that non-public attributes won’t change or even be removed.

No attribute is really private in Python so do not use the key word private.

With this in mind, here are the Pythonic guidelines:

* Public attributes should have no leading underscores.

* If your public attribute name collides with a reserved keyword, append a single trailing underscore to your attribute name. This is preferable to an abbreviation or corrupted spelling. (However, notwithstanding this rule, ‘cls’ is the preferred spelling for any variable or argument which is known to be a class, especially the first argument to a class method.) \
Note 1: See the argument name recommendation above for class methods.

* For simple public data attributes, it is best to expose just the attribute name, without complicated accessor/mutator methods. Keep in mind that Python provides an easy path to future enhancement, should you find that a simple data attribute needs to grow functional behavior. In that case, use properties to hide functional implementation behind simple data attribute access syntax. \
Note 1: Try to keep the functional behavior side-effect free, although side-effects such as caching are generally fine. \
Note 2: Avoid using properties for computationally expensive operations; the attribute notation makes the caller believe that access is (relatively) cheap.

* If your class is intended to be subclassed, and you have attributes that you do not want subclasses to use, consider naming them with double leading underscores and no trailing underscores. This invokes Python’s name mangling algorithm, where the name of the class is mangled into the attribute name. This helps avoid attribute name collisions should subclasses inadvertently contain attributes with the same name. \
Note 1: Note that only the simple class name is used in the mangled name, so if a subclass chooses both the same class name and attribute name, you can still get name collisions. \
Note 2: Name mangling can make certain uses, such as debugging and `__getattr__()`, less convenient. However the name mangling algorithm is well documented and easy to perform manually. \
Note 3: Not everyone likes name mangling. Try to balance the need to avoid accidental name clashes with potential use by advanced callers.

## Public and Internal Interfaces
Any backwards compatibility guarantees apply only to public interfaces.

Documented interfaces are considered public, unless the documentation explicitly declares them to be provisional or internal interfaces exempt from the usual backwards compatibility guarantees. All undocumented interfaces should be assumed to be internal.

To better support introspection, modules should explicitly declare the names in their public API using the `__all__` attribute. Setting `__all__` to an empty list indicates that the module has no public API.

Even with `__all__` set appropriately, internal interfaces (packages, modules, classes, functions, attributes or other names) should still be prefixed with a single leading underscore.

An interface is also considered internal if any containing namespace (package, module or class) is considered internal.

# Programming Recommendations
* Code should be written in a way that does not disadvantage other implementations of Python (PyPy, Jython, IronPython, Cython, Psyco, and such). \
E.g. do not rely on CPython’s efficient implementation of in-place string concatenation for statements in the form `a += b` or `a = a + b`

* Comparisons to singletons like None should always be done with is or is not, never the equality operators. \
Also, beware of writing `if x` when you really mean `if x is not None` as the other value might have a type (such as a container) that could be false in a boolean context.

* Use `is not` operator rather than `not ... is`

* When implementing ordering operations with rich comparisons, it is best to implement all six operations (`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`) rather than relying on other code to only exercise a particular comparison. \
To minimize the effort involved, the `functools.total_ordering()` decorator provides a tool to generate missing comparison methods. \
PEP 207 indicates that reflexivity rules are assumed by Python. Thus, the interpreter may swap `y > x` with `x < y` or may swap the arguments of `x == y` and `x != y`. The `sort()` and `min()` operations are guaranteed to use the `<` operator and the `max()` function uses the `>` operator. However, it is best to implement all six operations so that confusion doesn’t arise in other contexts.

* Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier:
```
# Correct:
def f(x): return 2*x
```
```
# Wrong:
f = lambda x: 2*x
```

* Derive exceptions from `Exception` rather than `BaseException`. \
Class naming conventions apply here, although you should add the suffix “Error” to your exception classes if the exception is an error. Non-error exceptions that are used for non-local flow control or other forms of signaling need no special suffix.

* Use exception chaining appropriately. raise X from Y should be used to indicate explicit replacement without losing the original traceback. \
When deliberately replacing an inner exception (using raise X from None), ensure that relevant details are transferred to the new exception (such as preserving the attribute name when converting KeyError to AttributeError, or embedding the text of the original exception in the new exception message).

* When catching exceptions, mention specific exceptions whenever possible instead of using a bare except: clause:
```
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
```
    A good rule of thumb is to limit use of bare ‘except’ clauses to two cases:
    * If the exception handler will be printing out or logging the traceback; at least the user will be aware that an error has occurred.
    * If the code needs to do some cleanup work, but then lets the exception propagate upwards with raise. try...finally can be a better way to handle this case.

* When catching operating system errors, prefer the explicit exception hierarchy introduced in Python 3.3 over introspection of errno values.

* For all try/except clauses, limit the try clause to the absolute minimum amount of code necessary.

* When a resource is local to a particular section of code, use a with statement to ensure it is cleaned up promptly and reliably after use. A try/finally statement is also acceptable.

* Context managers should be invoked through separate functions or methods whenever they do something other than acquire and release resources:
```
# Correct:
with conn.begin_transaction():
    do_stuff_in_transaction(conn)
```
```
# Wrong:
with conn:
    do_stuff_in_transaction(conn)
```

* Be consistent in return statements - either all return statements in a function should return an expression, or none of them should. \
If any return statement returns an expression, any return statements where no value is returned should explicitly state this as return None, and an explicit return statement should be present at the end of the function (if reachable):
```
# Correct:

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)
```
```
# Wrong:

def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)
```

* Use `''.startswith()` and `''.endswith()` instead of string slicing to check for prefixes or suffixes.

* Object type comparisons should always use isinstance() instead of comparing types directly:
```
# Correct:
if isinstance(obj, int):
```
```
# Wrong:
if type(obj) is type(1):
```

* For sequences, (strings, lists, tuples), use the fact that empty sequences are false:
```
# Correct:
if not seq:
if seq:
```
```
# Wrong:
if len(seq):
if not len(seq):
```

* Don’t write string literals that rely on significant trailing whitespace. Such trailing whitespace is visually indistinguishable and some editors (or more recently, reindent.py) will trim them.

* Don’t compare boolean values to True or False using ==:
```
# Correct:
if greeting:
```
```
# Wrong:
if greeting == True:
```
```
# Wrong and worse:
if greeting is True:
```

* Use of the flow control statements `return/break/continue` within the finally suite of a `try...finally`, where the flow control statement would jump outside the finally suite, is discouraged. This is because such statements will implicitly cancel any active exception that is propagating through the finally suite:
```
# Wrong:
def foo():
    try:
        1 / 0
    finally:
        return 42
```

## Function Annotations
With the acceptance of PEP 484, the style rules for function annotations have changed.
* Function annotations should use PEP 484 syntax (there are some formatting recommendations for annotations in the previous section).

## Variable Annotations
PEP 526 introduced variable annotations. The style recommendations for them are similar to those on function annotations described above:
* Annotations for module level variables, class and instance variables, and local variables should have a single space after the colon.
* There should be no space before the colon.
* If an assignment has a right hand side, then the equality sign should have exactly one space on both sides:
```
# Correct:

code: int

class Point:
    coords: Tuple[int, int]
    label: str = '<unknown>'
```
```
# Wrong:

code:int  # No space after colon
code : int  # Space before colon

class Test:
    result: int=0  # No spaces around equality sign
```