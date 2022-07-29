import csv
import json
import random


def books_csv():
    with open("../test_data/books.csv") as f:
        reader = csv.reader(f)
        header = next(reader)
        books = [dict(zip(header, row)) for row in reader]
        custom_books = []
    for book in books:
        book = {
            'title': book['Title'],
            'author': book['Author'],
            'pages': book['Pages'],
            'genre': book['Genre']
        }
        custom_books.append(book)


def users_json():
    with open("../test_data/users.json", "r") as file:
        users = json.loads(file.read())
        res_users = []
        for user in users:
            res_user = {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age']
            }
    res_users += [res_user]
    return res_users


def distribute_books(books_list, users_list):
    if not isinstance(custom_books, list) or not isinstance(res_users, list):
        raise ValueError('Аргуметры должны быть в формате списка.')

    for book in custom_books:
        for user in res_users:
            if len(custom_books) == 0:
                break
            book = random.choice(books_list)
            user.books += [book.__dict__]
            custom_books.remove(book)
    return res_users




def write_to_json(books_list, users_list):
    """
    Записать данные в json-файл
    :param file: название файла, в который требуется записать данные
    :param data: данные в формате словаря, которые требуется записать в файл
    """
    with open("result.json", "w") as f:
        s = json.dumps(custom_books, res_users, indent=4)
        f.write(s)
