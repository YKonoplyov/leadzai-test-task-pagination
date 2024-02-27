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
    if not all(
        [
            isinstance(pagination_argument, int)
            for pagination_argument in pagination_args
        ]
    ):
        raise TypeError("All arguments should be integers")
    if total_pages < 1:
        raise ValueError("`total_pages` shoud be > 0")
    if current_page < 1:
        raise ValueError(f"`current_page`({current_page}) shoud be > 0")
    if current_page > total_pages:
        raise ValueError("`current_page` should be in range (1, `total_pages`)")
    if around < 0:
        raise ValueError("Around should be >= 0")
    if boundaries < 0:
        raise ValueError("Boundaries arguments should be >= 0")


def generate_left_boundary_around_current_page(
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

    if left_boundary_end + 1 >= righ_boundary_start:
        pagination_list = range(1, total_pages + 1)
        pagination_str = pagination_list_to_str(pagination_list)
        print(pagination_str)
        return pagination_str

    generate_left_boundary_around_current_page(
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
