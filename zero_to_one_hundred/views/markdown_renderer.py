from abc import ABC, abstractmethod


class MarkdownRenderer(ABC):
    """
    render as md
    """

    @abstractmethod
    def asMarkDown() -> str:
        pass
