# Lab-7-9-Lybrary
Stefan Lucian Gramada 

The objective of this project is to create an app that can gestionates a list of books, a list of clients and generate some statistics. The actions are:
* Adds / Removes / Modifies the list of books / clients
* Searches book / client
* Shows a list of books / clients / clients who borrowed books ordered by name / number of books
* Shows statistics like:
  * The most borrowed books
  * The first 20% of the most active clients
 
## Iteration plan
Iteration 1:
* Adds books / clients
* Shows the list of books / clients

Iteration 2:
* Removes / Modifies the list of books / clients
* Searches book / client

Iteration 3:
* Shows a list of clients who borrowed books ordered by name / number of books
* Show statistics

## Running Scenarios
### Iteration 1
The app is a command-line program it has to run in a terminal. Every action has to be typed and it is not case sensitive.
| User | Program | Description |
|:-    |:-       |:-           |
| "add book" | - | Tell program to add a book |
| - | "ID: Title: Description: Author:" | Program waits for the characteristics of the book |
|"1 Fire and Blood Fantasy Goerge Martin"|-|Adds the book with ID: 1, Title: Fire and Blood, Description: Fantasy, Author: George Martin|
| "show books" | - | Tell program to show the book list |
| - | "[{'id': '1', 'title': 'Fire and Blood', 'description': 'Fantasy', 'author': 'George Martin'}]" | Shows the books |
| "add client" | - | Tell program to add a client|
| - | "ID: Name: CNP:" | Program waits for the characteristics of the client |
| "1 Stefan Lucian Did you really thought I will put it here? =)" | - | Adds the client with ID: 1, Name: Stefan Lucian, CNP: You get it ;)|
| "show clients" | - | Tell program to show the clients |
| - | "[{'id': '1', 'name': 'Stefan Lucian', 'cnp': 'Did you really thought I will put it here? =)'}]" | Shows the clients |
| "exit" | - | Close the program |

### Iteration 2
### Iteration 3
