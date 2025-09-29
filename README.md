# QuackScript Documentation

## Introduction

QuackScript is a whimsical, duck-themed programming language with dynamic execution behavior. The language features a "duck mood" system that affects how your code runs, random weather events, and playful built-in functions.

## Basic Syntax

### Variables

Declare variables using the `VAR` keyword:

```
VAR x = 10
VAR name = "Duck"
VAR myList = [1, 2, 3]
```

### Data Types

- **Numbers**: Integers and floats (`42`, `3.14`)
- **Strings**: Text in double quotes (`"Hello"`)
- **Lists**: Collections in square brackets (`[1, 2, 3]`)
- **Functions**: Defined with `FUN` keyword
- **Eggs**: Special values that hatch into functions

### Comments

Use `#` for single-line comments:

```
# This is a comment
VAR x = 5  # Comments can be inline too
```

### Operators

**Arithmetic**: `+`, `-`, `*`, `/`, `^` (power)

**Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`

**Logical**: `AND`, `OR`, `NOT`

**List Operations**:
- `list + item` - Append item to list
- `list - index` - Remove item at index
- `list * otherList` - Concatenate lists
- `list / index` - Get item at index

## Control Flow

### If Statements

**Single-line**:
```
IF x > 10 THEN PRINT("Big") ELSE PRINT("Small")
```

**Multi-line**:
```
IF x > 10 THEN
    PRINT("Big number")
    VAR y = x * 2
END
```

**With elif**:
```
IF x < 0 THEN
    PRINT("Negative")
ELIF x == 0 THEN
    PRINT("Zero")
ELSE
    PRINT("Positive")
END
```

### Loops

**For Loop**:
```
FOR i = 0 TO 10 THEN PRINT(i)

FOR i = 0 TO 100 STEP 10 THEN
    PRINT(i)
END
```

**While Loop**:
```
WHILE x < 10 THEN x = x + 1

WHILE x < 100 THEN
    PRINT(x)
    VAR x = x + 1
END
```

**Loop Control**:
- `CONTINUE` - Skip to next iteration
- `BREAK` - Exit loop

## Functions

### Function Definition

**Single-line (arrow syntax)**:
```
FUN add(a, b) -> a + b
```

**Multi-line**:
```
FUN greet(name)
    VAR message = "Hello, " + name
    PRINT(message)
    RETURN message
END
```

**Anonymous functions**:
```
VAR square = FUN(x) -> x * x
```

### Function Calls

```
add(5, 3)
greet("Duck")
square(4)
```

## Built-in Functions

### I/O Functions

- `PRINT(value)` - Print value (10% chance of adding "Quack!")
- `PRINT_RET(value)` - Return value as string
- `INPUT()` - Read string input
- `INPUT_INT()` - Read integer input
- `CLEAR()` / `CLS()` - Clear screen

### Type Checking

- `IS_NUM(value)` - Check if number
- `IS_STR(value)` - Check if string
- `IS_LIST(value)` - Check if list
- `IS_FUN(value)` - Check if function

### List Functions

- `APPEND(list, value)` - Add item to list
- `POP(list, index)` - Remove and return item
- `EXTEND(listA, listB)` - Add all items from listB to listA
- `LEN(list)` - Get list length

### Duck-Themed Functions

- `QUACK()` - Animated duck walks across screen and quacks
- `FLAP()` - Print flapping message
- `MOOD()` - Get current duck mood and weather
- `EGG(func, time)` - Create egg that hatches after `time` seconds
- `HATCH(egg)` - Hatch egg to get function inside

### Utility Functions

- `RUN(filename)` - Execute another QuackScript file

### Constants

- `NULL` - Null value (0)
- `TRUE` - Boolean true (1)
- `FALSE` - Boolean false (0)
- `MATH_PI` - Pi constant (3.14159...)

## Duck Mood System

The duck's mood affects execution speed:

- **Normal**: Standard execution speed
- **Energetic**: Faster (50+ operations)
- **Hyper**: Very fast (100+ operations)
- **Tired**: Slower (after 10 seconds of inactivity)

Check mood with: `PRINT(MOOD())`

## Weather System

Random weather affects your code:

- **Sunny**: Normal behavior
- **Rainy**: Adds `~` to errors, 💧 to strings, 20% slower
- **Stormy**: Numbers appear yellow, 50% slower
- **Cloudy**: Normal behavior

Weather changes randomly (1% chance per operation).

## Duck Memory (Variable Amnesia)

Variables unused for 30+ seconds have a 10% chance to be forgotten. Access them regularly to keep them in memory!

## Egg System

Create delayed functions using eggs:

```
# Create egg that hatches in 5 seconds
FUN myFunc() -> 42
VAR egg = EGG(myFunc, 5)

# Wait 5 seconds...
VAR hatched = HATCH(egg)
PRINT(hatched())  # Prints: 42
```

Eggs show countdown: `🥚 (2.3s)` → `🐥`

## Color Output

QuackScript uses colors in terminal output:

- **Errors**: Red
- **Strings**: Green (with 💧 in rain)
- **Lists**: Cyan
- **Numbers**: Yellow in storms
- **Print output**: Blue
- **Special messages**: Yellow/Magenta

## Examples

### Factorial Function
```
FUN factorial(n)
    IF n <= 1 THEN
        RETURN 1
    ELSE
        RETURN n * factorial(n - 1)
    END
END

PRINT(factorial(5))  # 120
```

### List Processing
```
VAR numbers = [1, 2, 3, 4, 5]
VAR sum = 0

FOR i = 0 TO LEN(numbers) THEN
    VAR sum = sum + (numbers / i)
END

PRINT(sum)
```

### Delayed Execution
```
FUN sayHello() -> PRINT("Hello from egg!")
VAR egg = EGG(sayHello, 3)
PRINT("Waiting for egg to hatch...")
PRINT(egg)  # Shows countdown
# Wait 3 seconds
VAR func = HATCH(egg)
func()  # Prints: Hello from egg!
```

### Interactive Program
```
PRINT("What's your name?")
VAR name = INPUT()
PRINT("Hello, " + name + "!")

QUACK()  # Duck animation
PRINT("Current mood: " + MOOD())
```

## Tips

1. **Keep variables active** - Access them regularly to prevent amnesia
2. **Watch the weather** - Check `MOOD()` to see current conditions
3. **Use eggs wisely** - Great for timed events
4. **Enjoy the quacks** - Random "Quack!" messages add personality
5. **Multi-line is safer** - Use `END` for complex functions

## Common Errors

**"Duck forgot about variable"** - Variable unused too long, reassign it

**"Expected 'END'"** - Missing `END` keyword in multi-line block

**"Egg not ready to hatch"** - Wait for countdown to finish

**"Expected ',' or ')'"** - Syntax error in function call/definition

## Running QuackScript

**Interactive shell**:
```bash
python shell.py
```

**Run file**:
```bash
# In QuackScript:
RUN("myprogram.qs")
```

---

Quack responsibly! 🦆