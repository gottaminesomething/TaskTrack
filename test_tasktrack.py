from tasktrack import remove_task_by_number
def test_remove_first_task():
    """Removing task 1 should remove the first task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Study"

    # Act
    removed_task = remove_task_by_number(tasks, 1)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Exercise", "Read"]

def test_remove_middle_task():
    """Removing task 1 should remove the first task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Exercise"

    # Act
    removed_task = remove_task_by_number(tasks, 2)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Study", "Read"]

def test_remove_last_task():
    """Removing task 1 should remove the first task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Read"

    # Act
    removed_task = remove_task_by_number(tasks, len(tasks))

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Study", "Exercise"]

def test_remove_zero():
    """Removing task 1 should remove the first task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_tasks = ["Study", "Exercise", "Read"]

    # Act
    removed_task = remove_task_by_number(tasks, 0)

    # Assert
    assert removed_task is None
    assert tasks == expected_tasks

def test_remove_task_number_too_large():
    """A number beyond the list length should not change the list."""
    # Arrange
    tasks = ["Study", "Exercise"]
    expected_tasks = ["Study", "Exercise"]

    # Act
    removed_task = remove_task_by_number(tasks, 5)

    # Assert
    assert removed_task is None
    assert tasks == expected_tasks

def test_remove_negative_task():
    # Arrange
    tasks = ["Study", "Exercise"]
    expected_tasks = ["Study", "Exercise"]
    
    # Act
    removed_task = remove_task_by_number(tasks, -5)
    
    # Assert
    assert removed_task is None
    assert tasks == expected_tasks