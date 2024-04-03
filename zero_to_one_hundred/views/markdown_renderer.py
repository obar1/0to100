from abc import ABC, abstractmethod


class MarkdownRenderer(ABC):
    """
    render as md
    """

    @abstractmethod
    def asMarkDown(self) -> str:
        pass

    @staticmethod
    def render_path_local(raw_path, root_path):
        """
        use relative path and convert " " to %20 
        """
        return raw_path.replace(root_path, "./").replace(" ", "%20")
