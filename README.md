# Essentials module

## Intention
Essentials is a bundle of useful chunks of code. Simply copy it and use in your projects.

## Content

### Classes module
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

### Unit testing
Use pytest for module unit testing