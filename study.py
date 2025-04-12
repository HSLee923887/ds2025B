def duplicate_city(cities):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        #집합에 도시 추가하기 전과 후의 길이를 비교함. 같다면 중복된 도시라는 뜻. list에 추가함
        if l1 == l2:
            result.append(city)
    return result


cities = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
#cities = {'Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul'}
cities.append('Anyang')
cities.append('Seoul')
print(cities)
print(set(duplicate_city(cities)))
