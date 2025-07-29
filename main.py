from linear_search_tool.search import linear_search

if __name__ == "__main__":
    data = [3, 8, 12, 4, 6]
    target = 4
    result = linear_search(data, target)
    print(f"Index de {target} : {result}")
