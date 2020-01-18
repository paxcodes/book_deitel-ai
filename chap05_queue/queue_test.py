from queue import Queue

import pytest


@pytest.fixture
def queue():
    return Queue()


def test_EmptyQueueShouldBeIdentifiedAsEmpty(queue):
    assert queue.IsEmpty() == True


def test_AddingItemToAQueueShouldIdentifyQueueAsNotEmpty(queue):
    queue.Add(2)
    assert queue.IsEmpty() == False


def test_RemovingItemShouldRemoveFirstItemAdded(queue):
    queue.Add(2)
    queue.Add(4)
    assert len(queue) == 2
    assert queue.Remove() == 2
    assert len(queue) == 1
