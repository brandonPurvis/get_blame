import elasticsearch

INDEX = 'get_blame'
CLIENT = elasticsearch.Elasticsearch()
BLAME_DOC = 'blame'


def build_query(search_text):
    query = {
        'query': {
            'query_string': {
                'default_field': '_all',
                'query': search_text,
                'analyze_wildcard': True,
                'lenient': True,
            }
        }
    }
    return query


def create_index():
    CLIENT.indices.create(INDEX, ignore=400)


def delete_index():
    CLIENT.indices.delete(INDEX, ignore=400)


def add(doc):
    CLIENT.create(INDEX, BLAME_DOC, body=doc)


def find(text):
    return CLIENT.search(INDEX, BLAME_DOC, body=build_query(text))


if __name__ == '__main__':
    INDEX = 'test_blame'
    doc = {
        'name': 'Test',
        'code': 'This is just a test'
    }
    create_index()
    add(doc)
    print(find('test'))
    delete_index()
