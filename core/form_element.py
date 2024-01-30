class FormElement:
    def __init__(self, by: str, value: str, name: str):
        """
        Args:
            by (str): ID, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, NAME, TAG_NAME, CLASS_NAME, CSS_SELECTOR
        """
        self.__by = by
        self.__value = value
        self.__name = name

    @property
    def by(self) -> str:
        return self.__by

    @property
    def value(self) -> str:
        return self.__value

    @property
    def name(self) -> str:
        return self.__name
