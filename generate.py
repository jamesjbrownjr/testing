
# coding: utf-8

# I'm adding another comment

def trumpSentence(text):
    import markovify
    with open(text) as f:
        text = f.read()
    text_model = markovify.Text(text)
    return(text_model.make_sentence())






