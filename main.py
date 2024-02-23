AROUND_BASE_BORDER = 1
ELLIPSIS = "..."

def pagination_list_to_str(pagination_list: list):
    return " ".join([str(element) if isinstance(element, int) else element for element in pagination_list])

def pagination_generator(current_page: int, total_pages: int, boundaries: int, around: int) -> str:
    pagination_list = []
    total_pages_without_curtent_page = total_pages - 1
    if (around >= total_pages_without_curtent_page or boundaries * 2 >= total_pages - 1):
        pagination_list += range(1, total_pages + 1)
        pagination_str = pagination_list_to_str(pagination_list)
        print(pagination_str)
        return pagination_str


    around_left_border = current_page - around if current_page - around >= AROUND_BASE_BORDER else AROUND_BASE_BORDER 
    around_right_border = current_page + around
    left_boundary_end = boundaries if boundaries > 0 else 0
    righ_boundary_start = total_pages - boundaries + 1

    if around_left_border <= left_boundary_end + 1:
        pagination_list += range(1, around_right_border + 1)
        pagination_str = pagination_list_to_str(pagination_list)

    if around_left_border > left_boundary_end + 1:
        # print(around_left_border, left_boundary_end)
        pagination_list += range(1, left_boundary_end + 1)
        pagination_list.append(ELLIPSIS)
        pagination_list += range(around_left_border, around_right_border + 1)
    
    if around_right_border + 1 < righ_boundary_start:
        pagination_list.append(ELLIPSIS)
        pagination_list += range(righ_boundary_start, total_pages + 1)
        pagination_str = pagination_list_to_str(pagination_list)
        print(pagination_str)
        return pagination_str
    

    pagination_list += range(around_right_border + 1, total_pages + 1)
    pagination_str = pagination_list_to_str(pagination_list)
    print(pagination_str)
    return pagination_str

    # if around_right_border <= righ_boundary_start
    # print(pagination)
    # return pagination
