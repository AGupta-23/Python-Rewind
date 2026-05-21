# Variable type hint
age: int = 25
# age. -- will directly show all operations we can add in int functions


# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
# Usage
print(greeting("Alice"))