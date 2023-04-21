import requests
from pytrends.request import TrendReq
import PySimpleGUI as sg
from string import ascii_lowercase

sg.theme('Dark Black')

sg.theme_input_text_color('black')

layout = [[sg.Text('\nEnter 2-3 keywords about your article topic:\n', font=25)],
          [sg.Input(key='-INPUT2-', background_color='white')], [sg.Button('SUBMIT')], [sg.Text('Results:', font=(100, 40))],
          [sg.Text('(Choose 1 keyword phrase from each category)', font=25)], [sg.Button('More LONG-TAIL', key='-MORE2-', visible=False, tooltip='Place these in a <title> tag\nIn the first 100 words\nIn an image alt text\nIn an <h1> tag\nIn an <h2> or <h3> tag\nIn the last 100 words of your page!')],
          [sg.Text('Sorry, you used all 25 searches', visible=False, text_color='red', key='-TEXT1-')],
          [sg.Multiline('', size=(40, 17), disabled=True, key='-RESULTS-', text_color='orange'), sg.Multiline('', size=(40, 17), disabled=True, key='-RESULTS1-', text_color='orange')]]

window = sg.Window('AutomaticSEO', layout, default_element_size=(65, 1), default_button_element_size=(100, 2),
                   icon=b'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',
                   size=(700, 600), element_justification='c')

current_letter = 'a'

while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED:
        break
    if event == 'SUBMIT':
        window['-MORE2-'].update(disabled=False)
        window['-TEXT1-'].update(visible=False)
        additional_queries = {
            "a": "",
            "b": "",
            "c": "",
            "d": "",
            "e": "",
            "f": "",
            "g": "",
            "h": "",
            "i": "",
            "j": "",
            "k": "",
            "l": "",
            "m": "",
            "n": "",
            "o": "",
            "p": "",
            "q": "",
            "r": "",
            "s": "",
            "t": "",
            "u": "",
            "v": "",
            "w": "",
            "x": "",
            "y": "",
            "z": "",
        }
        current_letter = 'a'
        window['-MORE2-'].update(visible=True)
        key_query = window['-INPUT2-'].get()

        # pytrends
        pytrends = TrendReq(hl='en-US', tz=360)
        kw_list = [key_query]
        pytrends.build_payload(kw_list)
        related_queries = pytrends.related_queries()
        top = list(related_queries.values())[0]['top']
        window['-RESULTS1-'].update('LSI KEYWORDS:\n\n')
        window['-RESULTS1-'].update(top, append=True)
        window['-RESULTS1-'].update('\n\nPLACE THESE:\n\nIn several places anywhere along your webpage', append=True)

        key_query = key_query.strip().replace(' ', '%20')
        for i in ascii_lowercase:
            response2 = requests.get(
                f"https://suggestqueries.google.com/complete/search?jsonp=jQuery22402686540572534406_040466655432741216&q={key_query}%20{i}&client=chrome&_=0005610362715791517")
            response_text2 = response2.text

            for x in range(48, len(response_text2)):
                if response_text2[x] == ']':
                    response_text2 = response_text2[48:x + 1]
                    break
            for x in range(len(response_text2)):
                if response_text2[x] == '[':
                    new_text2 = response_text2[x:len(response_text2)]
                    new_text2 = new_text2.replace('"', "")
                    new_text2 = new_text2.replace("[", "")
                    new_text2 = new_text2.replace("]", "")
                    new_text2 = new_text2.split(',')
                    break
            additional_queries[i] = new_text2

        response = requests.get(
            f"https://suggestqueries.google.com/complete/search?jsonp=jQuery22402686540572534406_040466655432741216&q={key_query}&client=chrome&_=0005610362715791517")

        response_text = response.text

        for x in range(48, len(response_text)):
            if response_text[x] == ']':
                response_text = response_text[48:x + 1]
                break

        for x in range(len(response_text)):
            if response_text[x] == '[':
                new_text = response_text[x:len(response_text)]
                new_text = new_text.replace('"', "")
                new_text = new_text.replace("[", "")
                new_text = new_text.replace("]", "")
                new_text = new_text.split(',')
                break

        window['-RESULTS-'].update('LONG-TAIL KEYWORDS: \n\n' + ', '.join(new_text) + '\n\nPLACE THESE:\n\nIn a <title> tag\nIn the first 100 words\nIn an image alt text\nIn an <h1> tag\nIn an <h2> or <h3> tag\nIn the last 100 words of your page!')

    if event == '-MORE2-':

        if current_letter == '{':
            window['-TEXT1-'].update(visible=True)
            window['-MORE2-'].update(disabled=True)
        else:
            window['-RESULTS-'].update('LONG-TAIL KEYWORDS: \n\n' + ', '.join(additional_queries.get(current_letter)) + '\n\nPLACE THESE:\n\nIn a <title> tag\nIn the first 100 words\nIn an image alt text\nIn an <h1> tag\nIn an <h2> or <h3> tag\nIn the last 100 words of your page!')
            current_letter = chr(ord(current_letter) + 1)

window.close()
