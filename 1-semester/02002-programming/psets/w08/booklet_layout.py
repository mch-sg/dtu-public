def booklet_layout(content_pages):
    nn = 0 # amt of white pages

    if content_pages % 4: # if its not perfect multiple of 4, then
        o_o_cp = content_pages # save the old amount of page
        content_pages = content_pages - (content_pages % 4) # remove the leftovers so i can add the multiple of 4
        old_cp = content_pages # save the new content pages
        content_pages += 4 # add the 4 
        nn = (content_pages - old_cp) - (o_o_cp % 4) # find the amount of white pages
    
    return content_pages, nn