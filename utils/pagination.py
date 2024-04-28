import math
from fastapi import HTTPException


def pagination(form, page, limit):
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail="page yoki limit 0 dan kichik kiritilmasligi kerak")
    elif page and limit:
        return {"current_page": page, "limit": limit, "pages": math.ceil(form.count() / limit),
                "data": form.offset((page - 1) * limit).limit(limit).all()}
    else:
        return {"data": form.all()}

#
# def pagination(page, limit, items):
#     if page < 1 or limit < 1:
#         raise ValueError("Page and limit should be positive integers.")
#
#     total_items = len(items)
#     total_pages = math.ceil(total_items / limit)
#
#     start_index = (page - 1) * limit
#     end_index = start_index + limit
#
#     result_items = items[start_index:end_index]
#
#     return {
#         "current_page": page,
#         "limit": limit,
#         "pages": total_pages,
#         "data": result_items
#     }