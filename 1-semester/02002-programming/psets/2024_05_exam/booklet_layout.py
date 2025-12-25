def booklet_layout(content_pages: int) -> tuple:
    if content_pages % 4 == 0:
        return content_pages, 0
    
    # If not a multiple of 4, there will be up to 3 blank pages
    # Add amt of pages to the content_pages until we get a multiple of 4
    for i in range(1,4):
        if (content_pages+i) % 4 == 0:
            return (content_pages+i), i