from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

""" La interfaz builder especifica metodos para crear un curso con sus diferentes extraes """
class Builder (ABC):
    
    @property
    @abstractmethod
    def curso(self) -> None:
        pass

    @abstractmethod
    def curso_certificados(self) -> None:
        pass

    @abstractmethod
    def curso_asesoramientos(self) -> None:
        pass

    @abstractmethod
    def curso_recursos(self) -> None:
        pass


class ConcreteBuilder(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank curso object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._curso = curso()

    @property
    def curso(self) -> curso:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different cursos that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another curso.
        That's why it's a usual practice to call the reset method at the end of
        the `getcurso` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        curso = self._curso
        self.reset()
        return curso

    def curso_certificados(self) -> None:
        self._curso.add("Cumplimiento")

    def curso_asesoramientos(self) -> None:
        self._curso.add("Tutoria en vivo")

    def curso_recursos(self) -> None:
        self._curso.add("Codigo de ejemplo")


class curso():
    """
    It makes sense to use the Builder pattern only when your cursos are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated cursos. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.extras = []

    def add(self, extra: Any) -> None:
        self.extras.append(extra)

    def list_extras(self) -> None:
        print(f"curso extras: {', '.join(self.extras)}", end="")


class Director:
    """
    The Director is only responsible for executing the building steps in a
    extraicular sequence. It is helpful when producing cursos according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled curso.
        """
        self._builder = builder

    """
    The Director can construct several curso variations using the same
    building steps.
    """

    def build_minimal_viable_curso(self) -> None:
        self.builder.curso_certificados()

    def build_full_featured_curso(self) -> None:
        self.builder.curso_certificados()
        self.builder.curso_asesoramientos()
        self.builder.curso_recursos()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print("Standard basic curso: ")
    director.build_minimal_viable_curso()
    builder.curso.list_extras()

    print("\n")

    print("Standard full featured curso: ")
    director.build_full_featured_curso()
    builder.curso.list_extras()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom curso: ")
    builder.curso_certificados()
    builder.curso_asesoramientos()
    builder.curso.list_extras()