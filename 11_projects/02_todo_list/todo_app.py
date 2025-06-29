#!/usr/bin/env python3
"""
Todo List Application
A command-line todo list manager with file persistence.
"""

import json
import os
from datetime import datetime, date
from typing import List, Dict, Optional
import sys


class Task:
    """Represents a single task in the todo list."""
    
    def __init__(self, description: str, priority: str = "Medium", 
                 due_date: Optional[str] = None, category: str = "General"):
        self.id = None  # Will be set by TaskManager
        self.description = description
        self.completed = False
        self.priority = priority
        self.created_date = date.today().isoformat()
        self.due_date = due_date
        self.category = category
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed,
            'priority': self.priority,
            'created_date': self.created_date,
            'due_date': self.due_date,
            'category': self.category
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary."""
        task = cls(data['description'], data['priority'], data['due_date'], data['category'])
        task.id = data['id']
        task.completed = data['completed']
        task.created_date = data['created_date']
        return task
    
    def __str__(self) -> str:
        """String representation of task."""
        status = "[x]" if self.completed else "[ ]"
        priority_icon = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(self.priority, "⚪")
        due_info = f" (Due: {self.due_date})" if self.due_date else ""
        return f"{self.id:2d} | {status} | {priority_icon} {self.priority:6s} | {self.due_date or 'No due date':10s} | {self.description}"


class TaskManager:
    """Manages the collection of tasks."""
    
    def __init__(self, data_file: str = "data/tasks.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()
    
    def add_task(self, description: str, priority: str = "Medium", 
                 due_date: Optional[str] = None, category: str = "General") -> Task:
        """Add a new task to the list."""
        task = Task(description, priority, due_date, category)
        task.id = self.next_id
        self.next_id += 1
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def complete_task(self, task_id: int) -> bool:
        """Mark a task as complete."""
        task = self.get_task(task_id)
        if task:
            task.completed = True
            self.save_tasks()
            return True
        return False
    
    def uncomplete_task(self, task_id: int) -> bool:
        """Mark a task as incomplete."""
        task = self.get_task(task_id)
        if task:
            task.completed = False
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False
    
    def list_tasks(self, priority: Optional[str] = None, 
                   status: Optional[str] = None, 
                   category: Optional[str] = None) -> List[Task]:
        """List tasks with optional filtering."""
        filtered_tasks = self.tasks.copy()
        
        if priority:
            filtered_tasks = [t for t in filtered_tasks if t.priority.lower() == priority.lower()]
        
        if status:
            if status.lower() == "complete":
                filtered_tasks = [t for t in filtered_tasks if t.completed]
            elif status.lower() == "incomplete":
                filtered_tasks = [t for t in filtered_tasks if not t.completed]
        
        if category:
            filtered_tasks = [t for t in filtered_tasks if t.category.lower() == category.lower()]
        
        return filtered_tasks
    
    def search_tasks(self, query: str) -> List[Task]:
        """Search tasks by description."""
        query = query.lower()
        return [task for task in self.tasks if query in task.description.lower()]
    
    def get_statistics(self) -> Dict:
        """Get task statistics."""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.completed])
        pending = total - completed
        
        priorities = {}
        for task in self.tasks:
            priorities[task.priority] = priorities.get(task.priority, 0) + 1
        
        categories = {}
        for task in self.tasks:
            categories[task.category] = categories.get(task.category, 0) + 1
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending,
            'completion_rate': (completed / total * 100) if total > 0 else 0,
            'priorities': priorities,
            'categories': categories
        }
    
    def save_tasks(self):
        """Save tasks to file."""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)
    
    def load_tasks(self):
        """Load tasks from file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
                    if self.tasks:
                        self.next_id = max(task.id for task in self.tasks) + 1
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
            self.next_id = 1


class TodoApp:
    """Main application class."""
    
    def __init__(self):
        self.task_manager = TaskManager()
        self.running = True
    
    def display_help(self):
        """Display help information."""
        help_text = """
=== Todo List Application ===

Commands:
  add <description> [options]    - Add a new task
  list [options]                 - List all tasks
  complete <id>                  - Mark task as complete
  uncomplete <id>                - Mark task as incomplete
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
  --status <status>              - Filter by status (complete/incomplete)
  --category <category>          - Filter by category

Examples:
  add "Buy groceries" -p High -d 2023-12-10
  list --priority High
  list --status incomplete
  complete 1
  search "groceries"
"""
        print(help_text)
    
    def parse_command(self, command: str) -> tuple:
        """Parse user command and return (action, args, options)."""
        parts = command.strip().split()
        if not parts:
            return None, [], {}
        
        action = parts[0].lower()
        args = []
        options = {}
        
        i = 1
        while i < len(parts):
            if parts[i].startswith('-'):
                if parts[i] in ['-p', '--priority']:
                    if i + 1 < len(parts):
                        options['priority'] = parts[i + 1]
                        i += 2
                    else:
                        print("Error: Priority level required")
                        return None, [], {}
                elif parts[i] in ['-d', '--due-date']:
                    if i + 1 < len(parts):
                        options['due_date'] = parts[i + 1]
                        i += 2
                    else:
                        print("Error: Due date required")
                        return None, [], {}
                elif parts[i] in ['-c', '--category']:
                    if i + 1 < len(parts):
                        options['category'] = parts[i + 1]
                        i += 2
                    else:
                        print("Error: Category required")
                        return None, [], {}
                elif parts[i] == '--status':
                    if i + 1 < len(parts):
                        options['status'] = parts[i + 1]
                        i += 2
                    else:
                        print("Error: Status required")
                        return None, [], {}
                else:
                    print(f"Error: Unknown option {parts[i]}")
                    return None, [], {}
            else:
                args.append(parts[i])
                i += 1
        
        return action, args, options
    
    def handle_add(self, args: List[str], options: Dict):
        """Handle add command."""
        if not args:
            print("Error: Task description required")
            return
        
        description = ' '.join(args)
        priority = options.get('priority', 'Medium')
        due_date = options.get('due_date')
        category = options.get('category', 'General')
        
        # Validate priority
        if priority not in ['High', 'Medium', 'Low']:
            print("Error: Priority must be High, Medium, or Low")
            return
        
        # Validate due date format
        if due_date:
            try:
                datetime.strptime(due_date, '%Y-%m-%d')
            except ValueError:
                print("Error: Due date must be in YYYY-MM-DD format")
                return
        
        task = self.task_manager.add_task(description, priority, due_date, category)
        print(f"Task added successfully! ID: {task.id}")
    
    def handle_list(self, args: List[str], options: Dict):
        """Handle list command."""
        priority = options.get('priority')
        status = options.get('status')
        category = options.get('category')
        
        tasks = self.task_manager.list_tasks(priority, status, category)
        
        if not tasks:
            print("No tasks found.")
            return
        
        print(f"\n{'ID':2s} | {'Status':6s} | {'Priority':8s} | {'Due Date':10s} | Description")
        print("-" * 80)
        
        for task in tasks:
            print(task)
    
    def handle_complete(self, args: List[str], options: Dict):
        """Handle complete command."""
        if not args:
            print("Error: Task ID required")
            return
        
        try:
            task_id = int(args[0])
            if self.task_manager.complete_task(task_id):
                print("Task marked as complete!")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError:
            print("Error: Task ID must be a number")
    
    def handle_uncomplete(self, args: List[str], options: Dict):
        """Handle uncomplete command."""
        if not args:
            print("Error: Task ID required")
            return
        
        try:
            task_id = int(args[0])
            if self.task_manager.uncomplete_task(task_id):
                print("Task marked as incomplete!")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError:
            print("Error: Task ID must be a number")
    
    def handle_delete(self, args: List[str], options: Dict):
        """Handle delete command."""
        if not args:
            print("Error: Task ID required")
            return
        
        try:
            task_id = int(args[0])
            if self.task_manager.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError:
            print("Error: Task ID must be a number")
    
    def handle_search(self, args: List[str], options: Dict):
        """Handle search command."""
        if not args:
            print("Error: Search query required")
            return
        
        query = ' '.join(args)
        tasks = self.task_manager.search_tasks(query)
        
        if not tasks:
            print(f"No tasks found matching '{query}'")
            return
        
        print(f"\nSearch results for '{query}':")
        print(f"{'ID':2s} | {'Status':6s} | {'Priority':8s} | {'Due Date':10s} | Description")
        print("-" * 80)
        
        for task in tasks:
            print(task)
    
    def handle_stats(self, args: List[str], options: Dict):
        """Handle stats command."""
        stats = self.task_manager.get_statistics()
        
        print("\n=== Task Statistics ===")
        print(f"Total tasks: {stats['total']}")
        print(f"Completed: {stats['completed']} ({stats['completion_rate']:.1f}%)")
        print(f"Pending: {stats['pending']}")
        
        if stats['priorities']:
            print("\nBy Priority:")
            for priority, count in stats['priorities'].items():
                print(f"  {priority}: {count}")
        
        if stats['categories']:
            print("\nBy Category:")
            for category, count in stats['categories'].items():
                print(f"  {category}: {count}")
    
    def run(self):
        """Run the main application loop."""
        print("=== Todo List Application ===")
        print("Type 'help' for available commands, 'quit' to exit.")
        
        while self.running:
            try:
                command = input("\n> ").strip()
                if not command:
                    continue
                
                action, args, options = self.parse_command(command)
                
                if action == 'quit':
                    print("Goodbye!")
                    self.running = False
                elif action == 'help':
                    self.display_help()
                elif action == 'add':
                    self.handle_add(args, options)
                elif action == 'list':
                    self.handle_list(args, options)
                elif action == 'complete':
                    self.handle_complete(args, options)
                elif action == 'uncomplete':
                    self.handle_uncomplete(args, options)
                elif action == 'delete':
                    self.handle_delete(args, options)
                elif action == 'search':
                    self.handle_search(args, options)
                elif action == 'stats':
                    self.handle_stats(args, options)
                elif action is None:
                    continue
                else:
                    print(f"Error: Unknown command '{action}'. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                self.running = False
            except Exception as e:
                print(f"Error: {e}")


def main():
    """Main entry point."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main() 