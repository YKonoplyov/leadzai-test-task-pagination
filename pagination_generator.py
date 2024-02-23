AROUND_BASE_LEFT_BORDER = 1
ELLIPSIS = "..."


def pagination_list_to_str(pagination_list: list) -> str:
    return " ".join(
        [
            str(element) if isinstance(element, int) else element
            for element in pagination_list
        ]
    )


def validate_pagination_args(*pagination_args) -> None:
    current_page, total_pages, boundaries, around = pagination_args
    
    if total_pages < 1:
        raise ValueError("total pages shoud be > 0")
    if current_page < 1 or current_page > total_pages:
        raise ValueError(
            f"current page ({current_page}) shoud be in range (1, 'total_pages')"
        )


def generate_left_boundary_and_around(
    around_start: int,
    around_end: int,
    left_boundary_end: int,
    right_boundary_start: int,
    pagination_list: list,
) -> list[int, str]:

    if around_end <= left_boundary_end:
        pagination_list += range(1, left_boundary_end + 1)
        return

    if around_start <= left_boundary_end + 1:
        pagination_list += range(1, around_end + 1)
        return

    if around_start >= right_boundary_start:
        pagination_list += range(1, left_boundary_end + 1)
        return

    pagination_list += range(1, left_boundary_end + 1)
    pagination_list.append(ELLIPSIS)
    pagination_list += range(around_start, around_end + 1)
    return


def generate_right_boundary(
    righ_boundary_start: int, total_pages: int, pagination_list: list
) -> list[int, str]:

    if pagination_list[-1] + 1 >= righ_boundary_start:
        pagination_list += range(pagination_list[-1] + 1, total_pages + 1)
        return

    pagination_list.append(ELLIPSIS)
    pagination_list += range(righ_boundary_start, total_pages + 1)

    return

def pagination_generator(
    current_page: int, total_pages: int, boundaries: int, around: int
) -> str:
    validate_pagination_args(*locals().values())

    pagination_list = []

    around_start = (
        current_page - around
        if current_page - around >= AROUND_BASE_LEFT_BORDER
        else AROUND_BASE_LEFT_BORDER
    )
    around_end = (
        current_page + around if current_page + around <= total_pages else total_pages
    )
    left_boundary_end = boundaries if boundaries > 0 else 0
    righ_boundary_start = total_pages - boundaries + 1

    generate_left_boundary_and_around(
        around_start,
        around_end,
        left_boundary_end,
        righ_boundary_start,
        pagination_list,
    )

    generate_right_boundary(righ_boundary_start, total_pages, pagination_list)

    pagination_str = pagination_list_to_str(pagination_list)
    print(pagination_str)
    return pagination_str


if __name__ == "__main__":
    pagination_generator(14, 15, 6, 2)  # 1 ... 4 5
    pagination_generator(4, 10, 2, 2) # 1 2 3 4 5 6 ... 9 10
    pagination_generator(3, 5, 2, 2) # 1 2 3 4 5
    pagination_generator(10, 15, 2, 4)
    pagination_generator(3, 5, 0, 2)
    pagination_generator(1, 5, 0, 2)
    pagination_generator(3, 10, 2, 2) # 1 2 3 4 5 . . . 9 10
    pagination_generator(5, 20, 2, 2) # 1 2 3 4 5 6 7 . . . 19 20
    pagination_generator(10, 20, 2, 2) # 1 2 . . . 8 9 10 11 12 . . . 19 20
    pagination_generator(1, 20, 2, 2) # 1 2 3 . . . 19 20
    pagination_generator(50, 100, 20, 10)
    pagination_generator(4, 5, 0, 0)
    pagination_generator(4, 5, 0, 1)
    pagination_generator(11, 20, 0, 1)
    pagination_generator(11, 15, 0, 1)
    pagination_generator(19, 20, 0, 1)
    pagination_generator(18, 20, 2, 5)
    pagination_generator(1, 20, 9, 0)
    pagination_generator(20, 20, 9, 0)
    pagination_generator(1, 19, 9, 0)
    pagination_generator(10, 20, 5, 6)
    try:
        pagination_generator(0, 5, 0, 0)
    except ValueError as e:
        print("Value error:", e)
    try:
        pagination_generator(10, 9, 0, 0)
    except ValueError as e:
        print("Value error:", e)
    try:
        pagination_generator(1, 0, 0, 0)
    except ValueError as e:
        print("Value error:", e)
