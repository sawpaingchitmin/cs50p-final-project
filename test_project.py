from datetime import datetime
import pytest
from project import display_tasks, add_task, edit_task, delete_task, search_tasks
    
def test_display_tasks(monkeypatch, capsys):
     # Sample tasks for testing
    tasks = {
        "19 February 2025": ["Breakfast", "Eat Dinner"],
        "20 February 2025": ["Breakfast", "Lunch"],
    }

    # Simulate user selecting "View Tasks"
    monkeypatch.setattr("builtins.input", lambda _: "1")  

    display_tasks(tasks)

    # Capture printed output
    captured = capsys.readouterr()

    # Check if tasks are printed correctly
    assert "19 February 2025" in captured.out
    assert "Breakfast" in captured.out
    assert "Eat Dinner" in captured.out
    assert "20 February 2025" in captured.out
    assert "Lunch" in captured.out

def test_add_task(monkeypatch):
    # Sample tasks before adding a new task
    tasks = {
        "19 February 2025": ["Breakfast", "Eat Dinner"],
        "20 February 2025": ["Breakfast", "Lunch"],
    }

    # Get today's date in the same format
    date = datetime.today().strftime("%d %B %Y")

    # Simulate user input for date and task
    inputs = iter([date, "Study Time"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_task(tasks)

    # Check if the new task was added
    assert date in tasks
    assert "Study Time" in tasks[date]

def test_edit_task(monkeypatch):
    # Sample tasks before editing
    tasks = {
        "19 February 2025": ["Breakfast", "Eat Dinner"],
        "20 February 2025": ["Breakfast", "Lunch"],
    }

    # Simulate user editing the second task on 19 February 2025
    inputs = iter(["19 February 2025", "2", "Watch Movie"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    edit_task(tasks)

    # Check if the task was updated
    assert tasks["19 February 2025"][1] == "Watch Movie" 

def test_delete_task(monkeypatch):
    # Sample tasks before deletion
    tasks = {
        "19 February 2025": ["Breakfast", "Eat Dinner"],
        "20 February 2025": ["Homework", "Lunch"],
    }

    # Simulate user deleting the second task on 19 February 2025
    inputs = iter(["2", "19 February 2025", "2", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    delete_task(tasks)

    # Simulate user deleting the first task on 19 February 2025
    inputs = iter(["2", "19 February 2025", "2", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    delete_task(tasks)

    # Check if all tasks on 19 February 2025 were deleted
    assert "19 February 2025" not in tasks
    assert "Breakfast" not in tasks
    assert "Eat Dinner" not in tasks
    assert "20 February 2025" in tasks  # Other tasks should still exist


def test_search_tasks(monkeypatch, capsys):
    # Sample tasks for searching
    tasks = {
        "19 February 2025": ["Breakfast", "Eat Dinner"],
        "20 February 2025": ["Study Time", "Lunch"],
    }

    # Simulate user searching for "lunch"
    monkeypatch.setattr("builtins.input", lambda _: "lunch")
    search_tasks(tasks)

    # Capture printed output
    captured = capsys.readouterr()

    # Check if "Lunch" was found on 20 February 2025
    assert "Search Results:" in captured.out
    assert "20 February 2025" in captured.out
    assert "Lunch" in captured.out 
    assert "19 February 2025" not in captured.out

    # Simulate user searching for "homework" (not in tasks)
    monkeypatch.setattr("builtins.input", lambda _: "homework")
    search_tasks(tasks)

    # Capture output again
    captured = capsys.readouterr()

     # Check if the correct message is shown
    assert "No tasks found matching the keyword." in captured.out   

   