def format_res_to_str(movie: dict) -> str:
    msg = (
        f"Название: {movie.get('film_name', 'N/A')}\n"
        f"Описание: {movie.get('film_descr', 'N/A')}\n"
        f"Рейтинг: {movie.get('film_rating', 'N/A')}\n"
        f"Год производства: {movie.get('film_created_at', 'N/A')}\n"
        f"Жанр: {movie.get('film_genre', 'N/A')}\n"
        f"Возрастной рейтинг: {movie.get('age_rating', 'N/A')}\n"
        f"Постер: {movie.get('poster', 'N/A')}\n"
    )
    return msg
