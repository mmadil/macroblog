from django.shortcuts import render

from random import choice

from blog.models import Post
from widgets.models import Quote


# List of pairs (quotation, author).
quotations = [
    ("Focusing is about saying no.", "Steve Jobs"),
    ("First make it run, then make it run fast.", "Brian Kernighan"),
    ("It's easier to ask forgiveness than it is to get permission.", "Grace Hopper"),
    ("You must be the change you wish to see in the world.", "Mahatma Gandhi"),
    ("If I had eight hours to chop down a tree, I'd spend the first six of them sharpening my axe.", "Abraham Lincoln"),
    ("Sing like no one's listening, love like you've never been hurt, dance like nobody's watching, and live like its heaven on earth.", "Mark Twain"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Wiston Churchill"),
    ("A person who never made a mistake never tried anything.", "Albert Einstein"),
    ("Intelligence is the ability to adapt to change.", "Stephen Hawking"),
    ("I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion.", "Muhammad Ali"),
    ("Hope is a waking dream.", "Aristotle"),
    ("Innovation distinguishes between a leader and a follower.", "Steve Jobs"),
    ("If you do not change direction, you may end up where you were heading.", "Lao Tzu"),
    ("Education is the most powerful weapon which you can use to change the world.", "Nelson Mandela"),
    ("Don't judge each day by the harvest you reap but by the seeds that you plant.", "Robert Louis Stevenson"),
    # ... etc ...
]

def IndexView(request):

    recent_posts = Post.objects.filter(published='True').order_by('-updated_at')[:5]
    count = Post.objects.filter(published='True').count()
    all_quotation = Quote.objects.filter(use_it='True').values_list('quotation','quoted_by')
    quotation, author = choice(all_quotation)
    return render(request, 'index.html', {'quotation': quotation, 'author': author, 'recent_posts': recent_posts, 'count': count})

