# Import Libraries #

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Define App Window #


class ToDoListApp:
    def __init__(self, root: tk.Tk = tk.Tk()) -> None:
        """
        Initializes the ToDoListApp object with the given root window.

        Args:
            root (tkinter.Tk): The root window of the application.

        Returns:
            None
        """

        self.root = root
        self.root.title("To-Do List App")

        self.todo_list = ToDoList()

        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Creates and initializes all the widgets needed for the ToDoListApp.

        This function creates and packs the following widgets:

        - task_entry: A ttk.Entry widget for the user to input a new task.

        - add_button: A ttk.Button widget that calls the add_task method when
        clicked.

        - tasks_listbox: A tk.Listbox widget that displays the list of tasks.

        - delete_button: A ttk.Button widget that calls the delete_task method
        when clicked.

        - complete_button: A ttk.Button widget that calls the
        mark_as_completed method when clicked.

        - save_button: A ttk.Button widget that calls the save_and_quit method
        when clicked.

        - load_button: A ttk.Button widget that calls the load_tasks method
        when clicked.

        This function does not take any parameters and does not return
        anything.
        """

        self.task_entry = ttk.Entry(self.root)
        self.task_entry.pack()

        self.add_button = ttk.Button(
            self.root,
            text="Add Task",
            command=self.add_task
        )
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(
            self.root,
            selectmode=tk.SINGLE
        )
        self.tasks_listbox.pack()

        self.delete_button = ttk.Button(
            self.root,
            text="Delete Task",
            command=self.delete_task
        )
        self.delete_button.pack()

        self.complete_button = ttk.Button(
            self.root, text="Mark as Completed",
            command=self.mark_as_completed
        )
        self.complete_button.pack()

        self.save_button = ttk.Button(
            self.root, text="Save and Quit",
            command=self.save_and_quit
        )
        self.save_button.pack()

        self.load_button = ttk.Button(
            self.root, text="Load Tasks",
            command=self.load_tasks
        )
        self.load_button.pack()

    def add_task(self) -> None:
        """
        Adds a task to the todo list if the task entry is not empty.

        This function retrieves the task from the task entry widget and checks
        if it is not empty. If the task is not empty, it adds the task to the
        todo list using the `add_task` method of the `todo_list` object.
        Finally, it updates the task list by calling the `update_task_list`
        method.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """

        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.update_task_list()

    def delete_task(self) -> None:
        """
        Deletes a task from the task list based on the selected index.

        This function retrieves the selected index from the tasks_listbox
        widget.
        If a valid index is selected, it deletes the corresponding task
        from the todo_list using the delete_task method of the todo_list
        object. Finally, it updates the task list by calling the
        update_task_list method.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """

        selected_index = self.tasks_listbox.curselection()

        if selected_index:
            index = selected_index[0]

            self.todo_list.delete_task(index)

            self.update_task_list()

    def mark_as_completed(self) -> None:
        """
        Marks the selected task as completed.

        This function retrieves the index of the selected task from the
        tasks_listbox widget. If a valid index is selected, it marks
        the corresponding task as completed in the todo_list using the
        mark_as_completed method of the todo_list object. Finally, it
        updates the task list by calling the update_task_list method.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """

        selected_index = self.tasks_listbox.curselection()

        if selected_index:
            index = selected_index[0]

            self.todo_list.mark_as_completed(index)

            self.update_task_list()

    def update_task_list(self) -> None:
        """
        Updates the task list by deleting all existing tasks and inserting new
        tasks from the todo_list object.

        This function deletes all existing tasks in the tasks_listbox widget
        using the delete method with the range from 0 to the last index.
        Then, it iterates over each task in the todo_list object and inserts
        a new task into the tasks_listbox widget. The status of each task is
        determined by checking the "completed" key in the task_info
        dictionary. If the task is completed, the status is set to " [X]",
        otherwise it is set to " [ ]". The task and its status are then
        inserted into the tasks_listbox widget using the insert method with
        the tk.END index.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """

        self.tasks_listbox.delete(0, tk.END)

        for task_info in self.todo_list.tasks:
            status = " [X]" if task_info["completed"] else " [ ]"

            self.tasks_listbox.insert(tk.END, f"{task_info['task']}{status}")

    def save_and_quit(self) -> None:
        """
        Saves the to-do list to a file named "todo.txt" and quits the
        application.

        This function saves the to-do list to a file named "todo.txt" by
        calling the `save_to_file` method of the `todo_list` object. It
        then displays an information message box using the `showinfo`
        method of the `messagebox` module to inform the user that the
        to-do list has been saved. Finally, it quits the application by
        calling the `quit` method of the `root` object.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """

        self.todo_list.save_to_file("todo.txt")
        messagebox.showinfo("Info", "To-Do List saved. Quitting...")
        self.root.quit()

    def load_tasks(self) -> None:
        """
        Load tasks from a file named "todo.txt" and update the task list.

        This function loads the tasks from a file named "todo.txt" using the
        `load_from_file` method of the `todo_list` object. After loading the
        tasks, it calls the `update_task_list` method to update the task list
        in the user interface.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """

        self.todo_list.load_from_file("todo.txt")
        self.update_task_list()

# To-Do List Class #


class ToDoList:
    def __init__(self):
        """
        Initializes a new instance of the ToDoList class.

        This constructor initializes a new instance of the ToDoList class,
        creating an empty list to store the tasks.

        Parameters:
            self (ToDoList): The instance of the ToDoList class.

        Returns:
            None
        """

        self.tasks = []

    def add_task(self, task):
        """
        Adds a new task to the list of tasks.

        Args:
            task (str): The task to be added.

        Returns:
            None
        """

        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        """
        Deletes a task from the list of tasks at the specified index.

        Parameters:
            index (int): The index of the task to be deleted.

        Returns:
            None
        """

        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_as_completed(self, index):
        """
        Marks a task as completed by updating the 'completed' field of the
        task at the specified index.

        Parameters:
            index (int): The index of the task to mark as completed.

        Returns:
            None
        """

        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def save_to_file(self, filename):
        """
        Save the tasks in the `self.tasks` list to a file.

        Parameters:
            filename (str): The name of the file to save the tasks to.

        Returns:
            None
        """

        with open(filename, "w") as file:
            for task_info in self.tasks:
                file.write(f"{task_info['task']},{task_info['completed']}\n")

    def load_from_file(self, filename):
        """
        Load tasks from a file and update the list of tasks.

        This method reads tasks from a file specified by `filename` and updates
        the list of tasks in the instance of the class. The tasks are expected
        to be in a comma-separated format, where the first element is the task
        description and the second element is a boolean indicating whether the
        task is completed or not.

        Parameters:
            filename (str): The name of the file to load tasks from.

        Returns:
            None
        """

        self.tasks.clear()

        try:
            with open(filename, "r") as file:
                for line in file:
                    task, completed = line.strip().split(",")
                    self.tasks.append({
                        "task": task,
                        "completed": completed == "True"
                    })
        except FileNotFoundError:
            pass


def main() -> None:
    app = ToDoListApp()
    app.root.mainloop()


if __name__ == "__main__":
    main()
