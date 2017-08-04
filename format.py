import sys

s = sys.argv[1]

s_copy = s
results = s

un_format_words = []
while True:
    # print('s', s, un_format_words)
    start_index = s.find('{')
    end_index = s.find('}')
    if start_index != -1 and end_index != -1:
        word = s[start_index + 1: end_index]
        if word and word not in un_format_words:
            un_format_words.append(word)
        s = s[end_index + 1:]
    else:
        break

if un_format_words:

    format_args = ''
    for word in un_format_words:
        format_args += '{word}={word}, '.format(word=word)

    format_args = format_args[:-2]

    results = '{s_copy}.format({format_args})'.format(s_copy=s_copy, format_args=format_args)

sys.stdout.write(results)