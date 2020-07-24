

def to_snake_case(value: str) -> str:
    if not value:
        return value

    characters = [value[0].lower()]
    for previous_index, character in enumerate(value[1:]):
        previous_character = value[previous_index]
        was_lowercase = previous_character.lower() == previous_character
        is_lowercase = character.lower() == character
        characters.append(
            f'_{character.lower()}'
            if was_lowercase and not is_lowercase else
            character.lower()
        )

    return ''.join(characters)
