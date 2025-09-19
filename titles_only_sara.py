import sara_scrap_function

def get_titles():
    table = sara_scrap_function.scrap()
    titles_st = table['titles'].tolist()
    return titles_st

if __name__ == '__main__':
    print(get_titles())