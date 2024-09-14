def format_res_to_str(movie: dict) -> str:
    print(movie)
    msg = (
        f"Название: {movie.get('Название', 'N/A')}\n"
        f"Описание: {movie.get('Описание', 'N/A')}\n"
        f"Рейтинг: {movie.get('Рейтинг', 'N/A')}\n"
        f"Год производства: {movie.get('Год производства', 'N/A')}\n"
        f"Жанр: {movie.get('Жанр', 'N/A')}\n"
        f"Возрастной рейтинг: {movie.get('Возрастной рейтинг', 'N/A')}\n"
        f"Постер: {movie.get('Постер', 'N/A')}\n"
    )
    return msg
