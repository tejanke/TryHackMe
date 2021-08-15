# Room
https://tryhackme.com/room/rust

# Task 1 - Intro
Rust is fast, secure, and productive. It was created in 2015.  Rust is very similar to C++ in terms of performance.  It uses cargo as a package / library manager

# Task 2 - Installation
Rustup is used to install versions of Rust.  Rust has 3 flavors, stable, beta, and nightly.  Cargo uses a concept called crates.  The three main cargo commands are install, publish, and update.  You can also use cargo test, fmt, and clippy

# Task 3 - Hello World
* new folder
  * cargo init
    * file structure:
      * cargo.toml - config file for the project
      * src/
        * main.rs - main code file, required
          * fn main() - required main function
* curly braces denote code blocks
* printing
  * println!("Hello world");
* the ! character represents a macro
* execute this program
  * cargo run - compiles and runs the code
    * creates a new folder called target
      * target contains the binaries for the project
* build project without running it
  * cargo build
* build and optimize project
  * cargo build --release
    * the --release parameter tells the compiler to optimize
      * Rust has 4 release profiles, 0 to 4
      * binaries are stored in target/release

# Task 4 - Variables
* all variables are immutable in Rust by default
* let x = 5;
* to make a variable mutable append the mut keyword
* let mut x = 9;

* resources
  * https://play.rust-lang.org/