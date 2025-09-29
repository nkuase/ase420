# Replace Constructor with Factory Method - Refactoring Examples

This directory demonstrates three different approaches to creating shape objects, showcasing the evolution from a problematic direct constructor to two different factory method patterns.

## Overview

The "Replace Constructor with Factory Method" refactoring is used when:
- Object creation logic is complex
- You want to control object creation
- You need to return different types or subclasses
- Constructor parameters are unclear or error-prone

## Three Approaches Compared

### 1. Before Refactoring (`/before/`)
**Problem**: Direct constructor with type codes

```python
# Problematic usage
shape1 = Shape(0, 10, 20, 30, 40)  # What does 0 mean?
shape2 = Shape(Shape.TYPECODE_LINE, 10, 20, 30, 40)  # Better but still awkward
```

**Issues:**
- Magic numbers (typecodes) make code unclear
- Easy to pass wrong typecode
- Constructor does too much work
- All shape logic in one class
- Client must know internal typecodes

### 2. After Refactoring (`/after/`)
**Solution**: Factory method pattern with single class

```python
# Clear and safe usage
line = Shape.create(Shape.TYPECODE_LINE, 10, 20, 30, 40)
rectangle = Shape.create(Shape.TYPECODE_RECTANGLE, 10, 20, 30, 40)
```

**Benefits:**
- Factory method name is descriptive
- Still uses constants but in a controlled way
- Constructor is private (conceptually)
- Centralized object creation logic

**Limitations:**
- Still has typecodes internally
- Single class with multiple responsibilities
- Switch statements for different behaviors

### 3. Subclass Pattern (`/subclass/`)
**Advanced Solution**: Inheritance with specialized factory methods

```python
# Type-safe and clear usage
line = Shape.create_line(10, 20, 30, 40)
rectangle = Shape.create_rectangle(10, 20, 30, 40)
oval = Shape.create_oval(10, 20, 30, 40)

# Or direct instantiation
line = ShapeLine(10, 20, 30, 40)
```

**Benefits:**
- Type-safe - no magic numbers
- Each shape type is a separate class
- Polymorphic behavior through inheritance
- Open/Closed Principle - easy to add new shapes
- Clear method names for each shape type
- Proper separation of concerns

**Trade-offs:**
- More complex with multiple files
- Requires understanding of inheritance
- More overhead for simple cases

## Design Patterns Demonstrated

### Factory Method Pattern
- Encapsulates object creation logic
- Provides clear interface for creating objects
- Allows for future extension without changing client code

### Abstract Factory Pattern (in subclass version)
- Creates families of related objects
- Each factory method creates a specific type
- Client code depends on abstractions, not concrete classes

### Template Method Pattern (in subclass version)
- Base class defines common structure
- Subclasses implement specific behaviors
- Shared `__str__` method with abstract `get_name()`

## Code Quality Improvements

| Aspect | Before | After | Subclass |
|--------|--------|--------|----------|
| **Clarity** | ❌ Magic numbers | ✅ Clear factory method | ✅ Type-safe methods |
| **Safety** | ❌ Wrong typecodes possible | ⚠️ Still uses typecodes | ✅ Compile-time safety |
| **Extensibility** | ❌ Modify existing class | ⚠️ Add to switch statements | ✅ Add new subclass |
| **Maintainability** | ❌ Monolithic class | ⚠️ Single class with all logic | ✅ Separated concerns |
| **Polymorphism** | ❌ Switch-based dispatch | ❌ Switch-based dispatch | ✅ True polymorphism |

## Running the Tests

Each version has comprehensive unit tests:

```bash
# Test before refactoring
cd before/
python MainTest.py

# Test after refactoring (factory method)
cd ../after/
python MainTest.py

# Test subclass pattern
cd ../subclass/
python MainTest.py
```

## Key Learning Points

1. **Refactoring is iterative**: The evolution from direct constructor → factory method → inheritance shows how design can be progressively improved.

2. **Choose the right level of complexity**: 
   - Simple factory method for basic needs
   - Inheritance for complex polymorphic behavior

3. **Trade-offs exist**: Each approach has benefits and costs. Consider your specific requirements:
   - Code complexity vs. type safety
   - Number of types vs. maintenance overhead
   - Team experience with design patterns

4. **SOLID Principles in action**:
   - **Single Responsibility**: Each shape class has one reason to change
   - **Open/Closed**: Easy to add new shapes without modifying existing code
   - **Liskov Substitution**: All shapes can be used interchangeably
   - **Dependency Inversion**: Client depends on Shape abstraction, not concrete classes

## When to Use Each Approach

- **Before pattern**: Never (this is what we're refactoring away from)
- **Factory method**: When you have 2-5 related types and moderate complexity
- **Subclass pattern**: When you have complex behavior differences, need true polymorphism, or expect frequent additions of new types

## Extension Exercise

Try adding a new shape type (e.g., Circle, Triangle) to each version and observe:
- How much code needs to change?
- Where are the changes located?
- How error-prone is the process?

This will demonstrate why the subclass pattern scales better for complex scenarios.
