from geopy import distance
# этот код создает csv файл из ребер с весами
with open("European_countries.txt") as european_countries:
    with open("worldcities.csv", encoding='utf-8-sig') as cities:
        country_coord = dict()
        european_countries = european_countries.read()
        for i in cities.readlines()[1:]:
            country = i.split('","')[4]
            if country in european_countries and i.split('","')[8] == "primary":
                lat = float(i.split('","')[2])
                lng = float(i.split('","')[3])
                country_coord[country] = (lat, lng)
        country_coord["Moldova (the Republic of)"] = country_coord["Moldova"]
        country_coord["North Macedonia"] = country_coord["Macedonia"]
        country_coord["Russian Federation"] = country_coord["Russia"]
        country_coord["United Kingdom of Great Britain and Northern Ireland"] = country_coord["United Kingdom"]

        with open("list.csv") as edges:
            result = open("edges_with_w.csv", "w")
            result.write('"Source","Target","Weight"\n')
            for i in edges.read().split('\n'):
                u = i.split(',')[0][1:-1]
                v = i.split(',')[-1][1:-1]
                if u < v:
                    result.write(f'"{u}","{v}","{int(distance.geodesic(country_coord[u], country_coord[v]).km)}"\n')
            result.write('"Italy","Vatican City","4"')
            result.close()
