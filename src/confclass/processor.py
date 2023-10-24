from dataclasses import dataclass


class SampleConfClass(object):
    def __init__(self, file_path: str) -> None:
        print("hi")

    def whoknows(self):
        ...


class ClassProcessor:
    def process(self, cls: object):
        return type(cls.__class__, (SampleConfClass,), {})
