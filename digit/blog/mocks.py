from django.http import Http404


class Post() : 
    POSTS = [
        {
            'id': 1,
            'title': 'Post 1',
            'content': 'Content 1',
            'author': 'Author 1',
            'created_at': '2019-01-01 00:00:00',
        },
        {
            'id': 2,
            'title': 'Post 2',
            'content': 'Content 2',
            'author': 'Author 2',
            'created_at': '2019-01-02 00:00:00',
        },
        {
            'id': 3,
            'title': 'Post 3',
            'content': 'Content 3',
            'author': 'Author 3',
            'created_at': '2019-01-03 00:00:00',
        },
    ]

    @classmethod
    def all(cls):
        return cls.POSTS
    
    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[id - 1]
        except IndexError:
            raise Http404('Sorry, post #{} not found'.format(id))