# этот файл создает два csv файла: с вершинами и ребрами без весов
with open("GEODATASOURCE-COUNTRY-BORDERS.CSV") as all_countries:
    with open("European_countries.txt") as european_countries:
        result = open("data.csv", "w")
        edges = open("edges.csv", "w")
        l = open("list.csv", "w") 
        result.write('"id","Label"\n')
        edges.write('"Source","Target"\n')
        # l.write('"Source","Target"\n')
        used = dict()
        cnt = 0
        european_countries = european_countries.read()
        all_countries = all_countries.readlines()
        for i in all_countries:
            country = i.split(',')[1][1:-1]
            border = i.split(',')[-1][1:-1]
            # print(country)
            if country in european_countries:
                if country not in used:
                    used[country] = cnt
                    result.write(f'"{cnt}","{country}"\n')
                    cnt += 1
                    # print(country)
        for i in all_countries:
            country = i.split(',')[1][1:-1]
            border = i.split(',')[-1][1:-2]
            if country in european_countries:
                if border in european_countries and len(border) > 1:
                    edges.write(f'"{used[country]}","{used[border]}"\n')
                    l.write(f'"{country}","{border}"\n')
        for i in european_countries.split('\n'):
            if i not in used:
                print(i)
        result.close()
        edges.close()
        l.close()
