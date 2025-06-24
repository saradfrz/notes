# Common Regex Patterns for Text Processing

A quick reference table of useful regular expressions for common text editing and cleanup tasks.

| Description                                      | Pattern                                      | Replace With           |
|--------------------------------------------------|----------------------------------------------|------------------------|
| Enter                                            | `\r\n`                                         |                          |
| Trailing white spaces                            | `[ \t]+$`                                    |                          |
| Duplicates                                       | `^(.*)(\R(?=.*^\1$))`                        |                          |
| Remove Leading Whitespace                        | `^[ \t]+`                                     |                          |
| Remove Blank Lines                               | `^\s*\r?\n`                                   |                          |
| Convert Multiple Blank Lines to a Single Blank Line | `(\r?\n){2,}`                              | `\r\n\r\n`              |
| Multiple spaces → One space                       | `[ ]{2,}`                                    |                          |
| Remove All Numbers                                | `\d+`                                         |                          |
| Remove All Non-Alphanumeric Characters (except spaces) | `[^\w\s]`                              |                          |
| Delete Lines Matching a Pattern                   | `^.*unwanted_word.*\r?\n`                   |                          |
| Normalize All Line Endings to Windows             |                                               | `Menu: Edit > EOL Conversion > Windows (CR LF)` |