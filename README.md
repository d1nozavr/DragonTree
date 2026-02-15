# :dragon: DragonTree :deciduous_tree:

#### :smiley: Author: [**d1nozavr**](https://github.com/d1nozavr)

> [!WARNING]
> **Status**: Work In Progress.


## :sparkles: Features

- Open-Source
- Dynamically Typed
- Interpreted Language

## :star: Requirements

- Python >= **3.14**
- GNU make

## :rocket: Getting started

<details><summary>Install the <a href="https://github.com/d1nozavr/DragonTree">DragonTree</a></summary>

- Clone the project

  ```sh
  git clone --depth 1 https://github.com/d1nozavr/DragonTree.git
  ```

- Change folder

  ```sh
  cd DragonTree
  ```

- Remove the `.git` folder

  ```sh
  rm -rf .git
  ```

- Start DragonTree!

  ```sh
  make
  ```

</details>

### Roadmap

- Keywords:
  - Loops:
    - for,
    - while,
    - *loop*.

- Add 'Block Statements'

  ```ruby
  if (condition) {
      statement...
  }
  ```

## :large_blue_diamond: Examples for DragonTree v0.0.2-alpha

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
