# Project 2: Todo List Application

A command-line todo list application that demonstrates file handling, data structures, and user interaction.

## 📋 Project Overview

This project creates a fully functional todo list application that allows users to:
- Add new tasks with descriptions and priorities
- Mark tasks as complete
- Delete tasks
- View all tasks with filtering options
- Save and load tasks from a file
- Search for specific tasks

## 🎯 Learning Objectives

By completing this project, you will learn:
- **File I/O Operations**: Reading and writing data to files
- **Data Structures**: Working with lists, dictionaries, and JSON
- **User Input Handling**: Processing and validating user input
- **Error Handling**: Managing exceptions and edge cases
- **Data Persistence**: Saving application state between sessions
- **Command-Line Interface**: Creating interactive CLI applications

## 🚀 Features

### Core Features
- ✅ Add new tasks with description and priority
- ✅ Mark tasks as complete/incomplete
- ✅ Delete tasks
- ✅ List all tasks with various filters
- ✅ Search tasks by description
- ✅ Save tasks to file automatically
- ✅ Load tasks from file on startup

### Advanced Features
- 🔄 Priority levels (High, Medium, Low)
- 📅 Due dates for tasks
- 🏷️ Task categories/tags
- 📊 Task statistics and progress
- 🔍 Advanced search and filtering
- 📤 Export tasks to different formats

## 📁 Project Structure

```
02_todo_list/
├── README.md              # This file
├── todo_app.py            # Main application file
├── task_manager.py        # Task management logic
├── file_handler.py        # File I/O operations
├── utils.py               # Utility functions
├── tests/                 # Test files
│   ├── test_todo_app.py
│   └── test_task_manager.py
└── data/                  # Data storage
    └── tasks.json         # Tasks data file
```

## 🔧 Implementation Details

### Data Structure
Each task is represented as a dictionary:
```python
{
    'id': 1,
    'description': 'Complete Python tutorial',
    'completed': False,
    'priority': 'High',
    'created_date': '2023-12-01',
    'due_date': '2023-12-15',
    'category': 'Learning'
}
```

### File Format
Tasks are stored in JSON format for easy reading and writing:
```json
[
    {
        "id": 1,
        "description": "Complete Python tutorial",
        "completed": false,
        "priority": "High",
        "created_date": "2023-12-01",
        "due_date": "2023-12-15",
        "category": "Learning"
    }
]
```

## 🎮 Usage Examples

### Basic Usage
```bash
# Run the application
python todo_app.py

# Add a new task
> add "Buy groceries" -p High -d 2023-12-10

# List all tasks
> list

# Mark task as complete
> complete 1

# Delete a task
> delete 2

# Search for tasks
> search "groceries"
```

### Advanced Usage
```bash
# Add task with category
> add "Read Python docs" -p Medium -c Learning

# List tasks by priority
> list --priority High

# List incomplete tasks
> list --status incomplete

# Export tasks to CSV
> export csv
```

## 📊 Sample Output

```
=== Todo List Application ===

Commands:
  add <description> [options]    - Add a new task
  list [options]                 - List all tasks
  complete <id>                  - Mark task as complete
  delete <id>                    - Delete a task
  search <query>                 - Search tasks
  stats                          - Show statistics
  help                           - Show this help
  quit                           - Exit application

Options for add:
  -p, --priority <level>         - Priority (High/Medium/Low)
  -d, --due-date <date>          - Due date (YYYY-MM-DD)
  -c, --category <category>      - Task category

Options for list:
  --priority <level>             - Filter by priority
  --status <status>              - Filter by status
  --category <category>          - Filter by category

> add "Complete Python project" -p High -d 2023-12-15
Task added successfully! ID: 1

> list
ID | Status | Priority | Due Date  | Description
1  | [ ]    | High     | 2023-12-15| Complete Python project
2  | [x]    | Medium   | 2023-12-10| Buy groceries

> complete 1
Task marked as complete!

> stats
Total tasks: 2
Completed: 1 (50%)
Pending: 1 (50%)
High priority: 1
Medium priority: 1
```

## ✅ Success Criteria

- [ ] Application starts and shows menu
- [ ] Can add new tasks with description
- [ ] Can mark tasks as complete/incomplete
- [ ] Can delete tasks
- [ ] Can list all tasks
- [ ] Can search for tasks
- [ ] Tasks are saved to file automatically
- [ ] Tasks are loaded from file on startup
- [ ] Handles invalid input gracefully
- [ ] Shows helpful error messages
- [ ] Code is well-organized and documented

## 🚀 Bonus Features

1. **Due Date Reminders**: Alert user about upcoming due dates
2. **Task Categories**: Organize tasks by categories
3. **Priority Levels**: Different priority levels with color coding
4. **Task Statistics**: Progress tracking and analytics
5. **Data Export**: Export tasks to CSV or other formats
6. **Undo/Redo**: Ability to undo recent actions
7. **Task Templates**: Predefined task templates
8. **Bulk Operations**: Select and modify multiple tasks

## 💡 Implementation Tips

1. **Start Simple**: Begin with basic add/list/complete functionality
2. **Use JSON**: Store data in JSON format for easy handling
3. **Error Handling**: Add try-except blocks for file operations
4. **Input Validation**: Validate user input before processing
5. **Modular Design**: Separate concerns into different modules
6. **User Experience**: Provide clear feedback and help text

## 🔗 Related Topics

- File I/O Operations
- JSON Data Handling
- User Input Processing
- Error Handling
- Data Structures
- Command-Line Interfaces

## 📚 Additional Resources

- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [Command-Line Interface Design](https://clig.dev/)

---

**Ready to build your todo list application? Let's get started!** 📝 