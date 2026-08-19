#!/usr/bin/env python3

import os

def read_file_str(path):
    template_file = open(path, 'r')
    file_content = []
    for line in template_file:
        file_content.append(line)
    template_file.close()
    return file_content

def split_name(name):
    interpret = ''
    idx = 0
    try:
        idx = name.index(' - ')
        interpret = name[:idx]
        idx += 3
    except ValueError:
        pass
    song_name = name[idx:-4]
    return (interpret, song_name)

# load tabs
song_content = dict()
song_id = 0
interpret_list = []
song_list = []
for root, dirs, files in os.walk('../songs/czech'):
    for name in files:
        if name.endswith('.tab'):
            song_id += 1
            content = []
            content.append('\\newpage')
            content.append('\subsection*{' + name[:-4] + '}\\label{song_' + str(song_id) + '}')
            content.append('\\begin{lstlisting}\n')
            tab_file = root + '/' + name
            (interpret,song_name) = split_name(name)
            song_list.append((song_name,interpret,song_id))
            interpret_list.append((interpret,song_name,song_id))
            tab_file_content = read_file_str(tab_file)
            width = 0
            for t in tab_file_content:
                width = max(width,len(t))
            height = len(tab_file_content)
            to_line = len(tab_file_content)
            for (idx,line) in enumerate(tab_file_content):
                if line=='[Fingerstyle]\n': # ignore technical section
                    to_line = idx
                    break
            content.extend(tab_file_content[:to_line])
            content.append('\\end{lstlisting}\n')

            song_content[song_id] = content
            print('processed', tab_file)

# create lists of content
list_content = []

interpret_list = sorted(interpret_list)
list_content.append('\\subsection*{By interpret}')
list_content.append('\\begin{multicols}{2}')
list_content.append('\\begin{itemize}')
list_content.append('\\setlength\itemsep{-2mm}')
for (interpret,song_name,song_id) in interpret_list:
    list_content.append('\\item ' + interpret + ' -- ' + song_name + '\,\dotfill \\pageref{song_' + str(song_id) + '}')
list_content.append('\\end{itemize}')
list_content.append('\\end{multicols}')

list_content.append('\\newpage')

song_list = sorted(song_list)
list_content.append('\\subsection*{By song name}')
list_content.append('\\begin{multicols}{2}')
list_content.append('\\begin{itemize}')
list_content.append('\\setlength\itemsep{-2mm}')
for (song_name,interpret,song_id) in song_list:
    list_content.append('\\item ' + song_name + ' -- ' + interpret + '\,\dotfill \\pageref{song_' + str(song_id) + '}')
list_content.append('\\end{itemize}')
list_content.append('\\end{multicols}')

# add prepared tabs
final_content = []
for (song_name,interpret,song_id) in interpret_list:
    final_content.extend(song_content[song_id])

# load and alter template
new_content = ''.join(read_file_str('latex/template.tex'))
list_content = list(map(lambda x:x.replace('&','\&'), list_content))
final_content = list(map(lambda x:x.replace('&','\&'), final_content))
new_content = new_content.replace('%%% LIST %%%', ''.join(list_content))
new_content = new_content.replace('%%% CONTENT %%%', ''.join(final_content))

# save the final tab file
final_file = open('latex/main.tex', 'w')
final_file.write(new_content)
final_file.close()
