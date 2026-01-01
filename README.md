# :dragon: DragonTree :deciduous_tree:

![Python](https://img.shields.io/badge/python-3.14%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

### :smiley: Author: [**Trifonov Yaroslav**](https://github.com/d1nozavr)

> [!WARNING]
> **Status**: Work in Progress.

## :books: About

**:dragon: DragonTree :deciduous_tree:**

> The programming language written in Python 3.14.
> The language was created for data science, automation with scripts.

## :round_pushpin: Versions

### :white_check_mark: v0.0.2-alpha - Stable

- Added:
  - New expression signs;
  - Float numbers;
  - Keywords:
    - if,
    - else,
    - getline.
  - Conditions;

### :alarm_clock: v0.0.3-alpha - In Development

- Plans:
  - Code refactoring;

  - Data types:
    - int,
    - float,
    - double,
    - string,
    - bool,
    - null/none.
  
  - Add block statements (prototype);
  - Add deleting of variables (memory management prototype);

  - Loops:
    - for,
    - while,
    - ? loop ?.

## :pencil: Installation

### :unlock: Requirements

- **Python 3.14+** — required to run the project.

### :penguin: Linux/Mac OS :apple:

```shell
git clone --depth 1 https://github.com/d1nozavr/DragonTree.git
cd DragonTree
rm -rf .git

make
```

### :computer: Windows (Powershell)

```pwsh
git clone --depth 1 https://github.com/d1nozavr/DragonTree.git
cd DragonTree
Remove-Item .git -Recurse -Force

make
```

## :large_blue_diamond: Examples. DragonTree v0.0.2-alpha

### Example 1

```ruby
# DragonTree
# Example

output: "Hello, World!"

x = 3.14
greeting = "Welcome, User!"

if (x == 3.14) { output: 2 ** (x * 5) // (2 + (22 + 20)) }
else { output: "x is not equal to 3.14" }

output: 2 ** 10
output: 10 % 5
```

```ruby
Hello, World!
1209.0
1024
0
```

### Example 2

```ruby
# DragonTree
# Example

output: "Hello, World!"

x = 3.12
greeting = "Welcome, User!"

if (x == 3.14) { output: 2 ** (x * 5) // (2 + (22 + 20)) }
else { output: "x is not equal to 3.14" }

output: 2 ** 10
output: 10 % 5
```

```ruby
Hello, World!
x is not equal to 3.14
1024
0
```
