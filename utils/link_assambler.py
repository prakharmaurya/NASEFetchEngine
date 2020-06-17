def assamble(constLinks):
    url_list = []
    for name in constLinks:
        for symbol in constLinks[name]['symbols']:
            url_list.append(constLinks[name]['link'] + symbol)
    return url_list
