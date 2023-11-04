def is_spam_words(text, spam_words, space_around=False):

    text = text.lower()
    for word in spam_words:
        if space_around:
            words = text.split()
            if word in words:
                return True
        else:
            if word in text:
                return True
    return False