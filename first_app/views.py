from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    context={
        'name' :'Rubayed Prodhan',
        'roll' : 67720,
        'title' :'My name is Rubayed Prodhan . Iam a Software Devoloper',
        'empty_var': 'hello sir',
        'Variable': None,
        'date': datetime.datetime.now(),
        'number':122,
        'addslashes':'I\'m Rubayed',
        'cap':'rubayed',
        'width' : 'Rubyed',
        'text': 'String with spaces',
        'people': [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
        ],
        'Value':15,
        'file_size' : 123456789,
        'first_value':['a', 'b', 'c'],
        'join_value': ['a','b','c'],
        'line' : "one\ntwo\nthree",
        'string_value' : "Rubayed" ,
        'integer_value':123,
        'blog_date': datetime.datetime(2006, 6, 1, 0, 0),
        'comment_date': datetime.datetime(2006, 6, 1, 8, 0),
        'valuee': 'my FIRST post',
        'varr': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
        'value1': datetime.datetime(2022, 12, 12, 10, 30, 0, 123),
        'value2': datetime.datetime(2023, 1, 12, 10, 30, 0, 123),
        'value11': 20,
        'value111': "Python is Fun",
        'value222': "January - February - March",
         'value12': "Happy coding",
        'value21': "Cloud computing",
        'html1': "<b>I</b> <button>love</button> <span>dogs</span>",
        'html2': "<b>This</b> is <em>a</em> <button>Button</button>",
        'num_messages': 4,
        'num_tomato': 2,
        'num_cherries': 3,
        'long_text1': "I remember as a child, and as a young budding naturalist, spending \
all my time observing and testing the world around me—moving pieces, \
altering the flow of things, and documenting ways the world responded \
to me. Now, as an adult and a professional naturalist, I've approached \
language in the same way, not from an academic point of view but as a \
curious child still building little mud dams in creeks and chasing after \
frogs. So this book is an odd thing: it is a naturalist's walk through the \
language-making landscape of the English language, and following in \
the naturalist's tradition it combines observation, experimentation, \
speculation, and documentation—activities we don't normally \
associate with language.",
        'long_text2': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Vivamus eleifend sagittis odio, vel ultrices tortor tincidunt id. Nulla nec \
ex nec erat ultricies consequat. Vestibulum ante ipsum primis in faucibus \
orci luctus et ultrices posuere cubilia curae; Pellentesque habitant morbi \
tristique senectus et netus et malesuada fames ac turpis egestas. Sed \
tincidunt odio sit amet metus rhoncus, ut vehicula est tempor. Donec \
nec justo sed nisi feugiat placerat. Sed in metus ultricies, interdum \
tortor id, molestie ipsum. Duis eu ante ac ante condimentum lacinia. \
Aenean a lorem malesuada, tincidunt ipsum at, fringilla nisi."

    }
    return render(request,'home.html',context)


