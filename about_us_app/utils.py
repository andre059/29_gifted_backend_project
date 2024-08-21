def docs_path(instance, filename: str) -> str:
    """
    Создает путь для сохранения медиафайла в папке media в виде:
    /имя_приложения/класс/имя_файла
    """
    return f"{__name__.split(".", maxsplit=1)[0]}/{instance.__class__.__name__}/{filename}"
