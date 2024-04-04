from abc import ABC, abstractmethod


class MarkdownRenderer(ABC):
    """
    render as md
    """

    @abstractmethod
    def asMarkDown(self) -> str:
        pass

    @staticmethod
    def text_lf_as_br(txt):
        return txt.replace(",", ",<br/>")  # trick to have LF in MD tables :P
