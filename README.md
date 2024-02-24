# Essentials module

## Intention
Essentials is a bundle of useful chunks of code. Simply copy it and use in your projects.

## Content

### classes module
#### Singleton classes (singleton.py)

1. Singleton - class based on simple inheritance.

   Side effects: __init__ in derived classes called on every instantiation

2. SingletonMeta - metaclass implementation

   Side effects: undetected

#### TempDir (tempdir.py)

1. TempDir - class for temp dir creation with context manager feature

   Unlike tempfile.TemporaryDirectory returns class instance instead of temp dir path

2. NamedTempDir - context manager with Path interface in context manager

   Context manager acts as tempfile.TemporaryDirectory but returns Path like object

### decorators module

#### exception_wrapper

1. exception_catch - decorator to catch exceptions in wrapped code
   ##### decorator params:
   - exception_range: tuple[Type[Exception], ...] = (Exception,)
     Catch exception range, pass all necessary exception classes for catch
   - exception_value: Optional[T] = None
     What we should return on exception catch
   - callback: Callable[[str, Exception], None] = log_exception
     Callable to execute on exception fired
   ##### Usage patterns:
   - log an error and return nothing or default value (could be set in "exception_value")
   - log an error and raise expected exception in calling routine

#### Version from pyproject.toml

1. Application version from pyproject.toml

Place file in the root folder of your project. Version information could be obtained from pyproject.toml with:
```python
from version import get_version

def main():
    print(get_version())

```

Don't forget to deploy __pyproject.toml__ to deployment code!

### Unit testing
Use pytest for module unit testing
